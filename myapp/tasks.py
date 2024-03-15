import time
from myapp.models import Event
from config.celery import app

TIME_DELAY = 60


@app.task(name='create_event_with_delay')
def create_event_with_delay(event_data):
    """
    Задача на создание мероприятия с задержкой
    """
    time.sleep(TIME_DELAY)
    Event.objects.create(**event_data)
