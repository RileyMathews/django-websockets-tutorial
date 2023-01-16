from django.urls import path

from . import views

urlpatterns = {
    path("", views.index, name="index_view"),
    path("<str:room_name>/", views.room, name="room_view"),
}
