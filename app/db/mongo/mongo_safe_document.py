"""
This is a safe document mixin module
"""
import logging
import time

from loguru import logger

from app.exceptions.exceptions import MongoObjectsException, MongoSaveException


class SafeDocument:
    def save_safe(self, *args, **kwargs):
        for attempt in range(5):
            try:
                return self.save(*args, **kwargs)
            except MongoSaveException as err:
                wait_t = 0.5 * pow(2, attempt)  # exponential back off
                logger.warning(
                    "PyMongo auto-reconnecting... %s. Waiting %.1f seconds.",
                    str(err),
                    wait_t,
                )
                time.sleep(wait_t)

    @classmethod
    def objects_safe(cls, *args, **kwargs):
        for attempt in range(5):
            try:
                return cls.objects(*args, **kwargs)
            except MongoObjectsException as err:
                wait_t = 0.5 * pow(2, attempt)  # exponential back off
                logging.warning(
                    "PyMongo auto-reconnecting... %s. Waiting %.1f seconds.",
                    str(err),
                    wait_t,
                )
                time.sleep(wait_t)
