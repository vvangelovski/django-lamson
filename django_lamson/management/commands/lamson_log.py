from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings as django_settings
from lamson import  commands, utils as lamson_utils


class Command(BaseCommand):
    help = 'Starts the lamson log server'

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

        make_option('--host',
            action='store',
            dest='host',
            default='127.0.0.1',
            help='The binding address',
        ),

        make_option('--port',
            action='store',
            dest='port',
            default=8825,
            help='The port to listen on',
        ),

        make_option('--pid',
            action='store',
            dest='pid',
            default='./run/log.pid',
            help='The file where the pid for the process should be stored',
        ),
        

     )
   
    def handle(self, *args, **options):
        commands.log_command(options['port'],
                            options['host'],
                            options['chroot'],
                            options['chdir'],
                            options['uid'],
                            options['gid'],
                            options['umask'], 
                            options['pid'],
                            options['force'], 
                                )
    								
    