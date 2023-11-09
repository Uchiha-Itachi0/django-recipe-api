"""
Django command to wait for DB to be available
"""
import time

# Shows error but the psycopg2 is successfully installed on docker
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django command to wait for db
    """

    def handle(self, *args, **options):

        self.stdout.write('Waiting for the Database to start....')
        db_up = False

        while db_up is False:

            try:
                self.check(databases=['default'])
                db_up = True

            except (Psycopg2Error, OperationalError):
                self.stdout.write("DB is unavailable right now. \
                 Waiting for 1 sec to restart the database")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB is UP '))
