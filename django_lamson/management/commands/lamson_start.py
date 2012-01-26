from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings as django_settings
from lamson import  commands, utils as lamson_utils


class Settings(object):
	pass

def _settings_loader():
    from lamson.routing import Router
    from lamson.server import Relay, SMTPReceiver
    from lamson import view, queue
    import logging
    import logging.config
    import jinja2

    settings = Settings()
    for attr_name in dir(django_settings):
    	if attr_name.startswith("LAMSON_"):
    		setattr(settings, attr_name.split("LAMSON_")[1].lower(),
             getattr(django_settings, attr_name))
    
    #logging.config.fileConfig("logging.conf")

    # the relay host to actually send the final message to
    #TODO make debug a parameter to the command
    if hasattr(settings, 'relay_config'):
        settings.relay = Relay(host=settings.relay_config['host'], 
                               port=settings.relay_config['port'], debug=1)

    # where to listen for incoming messages
    settings.receiver = SMTPReceiver(settings.receiver_config['host'],
                                     settings.receiver_config['port'])

    Router.defaults(**settings.router_defaults)
    Router.load(settings.handlers)
    #TODO make this a parameter to the command
    Router.RELOAD=True
    #TODO make run a parameter to the command
    Router.UNDELIVERABLE_QUEUE=queue.Queue("run/undeliverable")

    if hasattr(settings, 'template_config'):
        view.LOADER = jinja2.Environment(
            loader=jinja2.PackageLoader(settings.template_config['dir'], 
                                        settings.template_config['module']))
    	
    return settings

class Command(BaseCommand):
    help = 'Starts the lamson SMTP server'

    option_list = BaseCommand.option_list + (
        make_option('--force',
            action='store_true',
            dest='force',
            default=False,
            help='Force start'),

        make_option('--chroot',
            action='store',
            type='string',
            dest='chroot',
            default=False,
            help='chroot',
        ),
        make_option('--chdir',
            action='store',
            type='string',
            dest='chdir',
            default='.',
            help='chdir',
        ),

        make_option('--uid',
            action='store',
            type='int',
            dest='uid',
            default=False,
            help='uid',
        ),

        make_option('--umask',
            action='store',
            type='int',
            dest='umask',
            default=False,
            help='umask',
        ),

        make_option('--gid',
            action='store',
            type='int',
            default=False,
            help='gid',
        ),

        make_option('--pid',
            action='store',
            dest='pid',
            default='./run/smtp.pid',
            help='The file where the pid for the process should be stored',
        ),


 )

    def handle(self, *args, **options):
        lamson_utils.start_server(options['pid'],
                                options['force'],
                                options['chroot'],
                                options['chdir'],
                                options['uid'],
                                options['gid'], 
                                options['umask'],
                                _settings_loader)
    