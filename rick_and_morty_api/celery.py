import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rick_and_morty_api.settings")

app = Celery("rick_and_morty_api")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
