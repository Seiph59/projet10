from django.core.management.base import BaseCommand
from food.update_db import update

class Command(BaseCommand):
    help = 'populate the database from openfoodfacts API'

    def handle(self, *args, **options):
        update()

        self.stdout.write(self.style.SUCCESS('Database has been successfully updated ! '))