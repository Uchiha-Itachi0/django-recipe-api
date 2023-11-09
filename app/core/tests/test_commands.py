"""
Test custom managements command
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# This is the command that we are going to be mocking
# Mocked object is check method
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """Test commands"""

    # patched_check is provided by the patch
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for DB if it's ready"""

        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""

        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        self.assertEquals(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
