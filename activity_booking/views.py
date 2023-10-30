
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Activity, Booking
from .forms import BookingForm

# Create your views here.


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    context_object_name = 'activities'


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'
    

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')
    
    def get_initial(self):
        initial = super(BookingCreateView, self).get_initial()
        activity_id = self.kwargs.get('activity_id')
        activity = get_object_or_404(Activity, pk=activity_id)
        initial['activity'] = activity
        return initial

    def get_context_data(self, **kwargs):
        context = super(BookingCreateView, self).get_context_data(**kwargs)
        activity_id = self.kwargs.get('activity_id')
        context['activity'] = get_object_or_404(Activity, pk=activity_id)
        return context

    def form_valid(self, form):
        activity_id = self.kwargs.get('activity_id')
        activity = get_object_or_404(Activity, pk=activity_id)
        form.instance.activity = activity
        return super(BookingCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('booking_list')
    
      
class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')
    
     
class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')