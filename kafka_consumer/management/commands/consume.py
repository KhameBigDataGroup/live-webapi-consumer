import json

from confluent_kafka.cimpl import Consumer
from django.core.cache import cache
from django.core.management.base import BaseCommand

from liveapi.settings import KAFKA_GROUP_ID, KAFKA_BOOTSTRAP_SERVICE, BTC_BLOCK_TOPIC


class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        self.start()

    def start(self):

        c = Consumer({
            'bootstrap.servers': KAFKA_BOOTSTRAP_SERVICE,
            'group.id': KAFKA_GROUP_ID,
            'auto.offset.reset': 'earliest'
        })

        c.subscribe([BTC_BLOCK_TOPIC])

        while True:
            msg = c.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            data = json.loads(msg.value().decode('utf-8'))
            cache.set("latest_block", data, timeout=None)
