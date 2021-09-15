from django.urls import path

from .views import AdminPageView

urlpatterns = [
    path("", AdminPageView.as_view(), name="adminsite")
]