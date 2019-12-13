from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from django.utils import timezone
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    passcard_user = Passcard.objects.get(passcode=passcode)
    visits_for_all_days = list(Visit.objects.filter(passcard=passcard_user))
    this_passcard_visits = []

    for visit_details in visits_for_all_days:
        entered_at = visit_details.entered_at
        duration = format_duration(get_duration(visit_details))
        is_strange = is_visit_long(visit_details)

        this_passcard_visits.append(
           {
              "entered_at": entered_at,
              "duration": duration,
              "is_strange": is_strange,
           }
        )

    context = {
        "this_passcard_visits": this_passcard_visits,  
    }
    return render(request, 'passcard_info.html', context)
