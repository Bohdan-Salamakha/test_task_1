from celery import shared_task

from clients.utils import save_clients_data, fetch_clients_data
from test_task_1.settings import AUTH_TOKEN


@shared_task
def fetch_and_save_clients():
    data: dict = fetch_clients_data(AUTH_TOKEN)
    save_clients_data(data)
