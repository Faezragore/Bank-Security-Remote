from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from django.utils import timezone
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long

def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    now = timezone.now()
    for visit_details in visits:
        who_entered = visit_details.passcard
        entered_at = visit_details.entered_at
        store_time_timer = now - entered_at
        duration = str(store_time_timer)[:-7]
        is_strange = is_visit_long(visit_details)
    
    non_closed_visits = [
        {
            "who_entered": who_entered, 
            "entered_at": entered_at,   
            "duration": duration,       
            "is_strange": is_strange    
        }
    ]
    context = {
        "non_closed_visits": non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
