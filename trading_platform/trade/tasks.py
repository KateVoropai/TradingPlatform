from celery import shared_task
from trade.services import find_matching_offers


@shared_task
def process_offers():
    find_matching_offers()