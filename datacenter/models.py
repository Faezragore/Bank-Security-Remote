from django.db import models
import datetime
from django.utils import timezone


def get_duration(visit):
    the_time_in_moscow = timezone.now() 
    if visit.leaved_at is None:
        time_spent = the_time_in_moscow - visit.entered_at
        return time_spent.total_seconds()
    else:
        time_spent = visit.leaved_at - visit.entered_at
        return time_spent.total_seconds()

def format_duration(duration):
    time_interval_in_minutes = datetime.timedelta(seconds = duration)
    return str(time_interval_in_minutes)

def is_visit_long(visit, minutes=60):
    return get_duration(visit) > minutes*60

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

