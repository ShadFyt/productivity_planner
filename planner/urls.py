from django.urls import path
from planner import views


urlpatterns = [path("", views.home_page, name="home")]
