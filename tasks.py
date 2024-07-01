import time

from celery import shared_task


@shared_task(bind=True)
def hello_world(self, name: str):
    self.update_state(state="STARTED")
    time.sleep(20)
    return "Hello World, " + name
