from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from lamson import  commands, utils as lamson_utils


class Command(BaseCommand):
    help = 'Stops the lamson daemon'

    option_list = BaseCommand.option_list + (
        make_option('--kill',
            action='store_true',
            dest='kill',
            default=False,
            help='kill'),
        
        make_option('--all',
            action='store',
            dest='all',
            default=False,
            help='Give --all the name of a run directory and it will stop all pid files it finds there',
        ),
        make_option('--pid',
            action='store',
            dest='pid',
            default='./run/smtp.pid',
            help='The file where the pid for the process is stored',
        ),
        

     )
   
    def handle(self, *args, **options):
    	commands.stop_command(options['pid'],
    						  options['kill'],
    						  options['all'],
    							)