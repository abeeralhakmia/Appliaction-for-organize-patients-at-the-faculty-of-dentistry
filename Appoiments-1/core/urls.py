# core/urls.py
from django.urls import include, path

from .views import (
    AcceptReservationView,
    HomeView,
    RegisterDonorView,
    RegisterNurseView,
    RejectReservationView,
    ReserveView,
    TodayScheduleView,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("register/donor/", RegisterDonorView.as_view(), name="register_donor"),
    path("register/nurse/", RegisterNurseView.as_view(), name="register_nurse"),
    path("reserve/", ReserveView.as_view(), name="reserve"),
    path("schedule/", TodayScheduleView.as_view(), name="schedule"),
    path(
        "reservation/<int:pk>/accept/",
        AcceptReservationView.as_view(),
        name="reservation_accept",
    ),
    path(
        "reservation/<int:pk>/reject/",
        RejectReservationView.as_view(),
        name="reservation_reject",
    ),
]
