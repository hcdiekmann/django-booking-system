
from django.views.generic import ListView, DetailView
from .models import Activity

# Create your views here.


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    context_object_name = 'activities'


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'