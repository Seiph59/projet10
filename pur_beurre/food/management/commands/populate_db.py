from django.core.management.base import BaseCommand
from food.openff_api import Database

class Command(BaseCommand):
    help = 'populate the database from openfoodfacts API'

    def handle(self, *args, **options):
        db = Database()
        db.populate()

        self.stdout.write(self.style.SUCCESS('Database has been successfully populated ! '))