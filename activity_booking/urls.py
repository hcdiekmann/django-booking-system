from django.urls import path
from django.conf.urls.static import static
from .views import ActivityListView, ActivityDetailView
from booking_system.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', ActivityListView.as_view(), name='activity_list'),
    path('activity/<int:pk>', ActivityDetailView.as_view(), name='activity_detail'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)