from django.core.management.base import NoArgsCommand, CommandError
import os

class Command(NoArgsCommand):
    help = 'Compiles coffeescript (from static/coffee/*.coffee) into javascript (to static/js/*.js)'
    
    def handle(self, **options):
        os.system("coffee --compile --output static/js/ static/coffee/")
