from django.urls import path
from django.conf.urls.static import static
from booking_system.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

from .views import ActivityListView, ActivityDetailView, BookingListView, BookingCreateView, BookingUpdateView, BookingDeleteView


urlpatterns = [
    path('', ActivityListView.as_view(), name='activity_list'),
    path('activity/<int:pk>', ActivityDetailView.as_view(), name='activity_detail'),
    path('booking/', BookingListView.as_view(), name='booking_list'),
    path('booking/create/<int:activity_id>/', BookingCreateView.as_view(), name='booking_create'),
    path('booking/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]

# Add media url and root for development
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)