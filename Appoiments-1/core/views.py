from braces.views import FormValidMessageMixin, UserFormKwargsMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from .forms import DonorForm, NurseForm, ReserveForm, ReserveStatusForm
from .models import Reservation, TermQuestion
from .permissions import IsDonor, IsNurse

User = get_user_model()


class HomeView(TemplateView):
    template_name = "home.html"


class RegisterDonorView(CreateView):
    form_class = DonorForm
    template_name = "register/donor.html"
    success_url = reverse_lazy("core:home")


class RegisterNurseView(CreateView):
    form_class = NurseForm
    template_name = "register/nurse.html"
    success_url = reverse_lazy("core:home")


class ReserveView(IsDonor, UserFormKwargsMixin, FormValidMessageMixin, CreateView):
    form_class = ReserveForm
    template_name = "reserve.html"
    success_url = reverse_lazy("core:home")
    form_valid_message = "You are now reserved"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["questions"] = TermQuestion.objects.all()
        return ctx


class ReservationNurseMixin(IsNurse):
    queryset = Reservation.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(
            status=Reservation.PENDING,
            date=timezone.now().date(),
        )
        return qs


class TodayScheduleView(ReservationNurseMixin, ListView):
    template_name = "schedule.html"
    queryset = Reservation.objects.all()


class AcceptReservationView(ReservationNurseMixin, UpdateView):
    template_name = "reservation_accept.html"
    form_class = ReserveStatusForm
    success_url = reverse_lazy("core:schedule")

    def get_initial(self):
        initial = super().get_initial()
        initial["status"] = Reservation.DONE
        return initial


class RejectReservationView(ReservationNurseMixin, UpdateView):
    template_name = "reservation_reject.html"
    form_class = ReserveStatusForm
    success_url = reverse_lazy("core:schedule")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop("blood_type")
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial["status"] = Reservation.MISSED
        return initial
