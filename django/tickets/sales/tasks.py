from celery import shared_task
from sales.models import Reserve

from django.utils import timezone
@shared_task
def auto_delete():
    reserve=Reserve.objects.all()
    for object in reserve:
        if (object.is_paid==False) and ((timezone.now() - object.date_create).total_seconds() > 30):
            object.delete()