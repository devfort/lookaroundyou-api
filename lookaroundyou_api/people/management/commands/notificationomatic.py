from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from functools import wraps
import logging
from raven.contrib.django.raven_compat.models import sentry_exception_handler
import time
import traceback
from ...models import Person


logger = logging.getLogger(__name__)


def send_exceptions_to_sentry(f):
    """
    decorator to swallow exceptions raised within a function
    """
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            return f(*args, **kwds)
        except:
            traceback.print_exc()
            sentry_exception_handler()
    return wrapper


def resilient_loop(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        while True:
            try:
                f(*args, **kwds)
            except KeyboardInterrupt:
                raise
            except:
                traceback.print_exc()
                sentry_exception_handler()
    return wrapper


class Command(BaseCommand):
    help = 'Sends notifications.'

    def handle(self, *args, **options):
        logger.info('Starting notificationomatic...')
        self.send_notifications()

    @resilient_loop
    def send_notifications(self):
        notifications = []
        for person in Person.objects.all():
            notifications.extend(person.send_notifications())
        logger.info('Sent %s notifications' % len(notifications))
        time.sleep(60)


