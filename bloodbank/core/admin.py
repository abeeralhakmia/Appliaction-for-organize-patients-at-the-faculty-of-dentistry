from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import BloodBag, CustomUser, HospitalSettings, Reservation, TermQuestion

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    exclude = ["password"]
    ordering = ("email",)
    list_display = ("email", "first_name", "middle_name", "last_name", "is_superuser")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_superuser",)
    readonly_fields = ("email",)


@admin.register(HospitalSettings)
class CustomUserAdmin(SingletonModelAdmin):
    pass


class ExpiredFilter(admin.SimpleListFilter):
    title = "expired"
    parameter_name = "expired"

    def lookups(self, request, model_admin):
        return (
            (True, "Expired"),
            (False, "Valid"),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(expired=value)
        return queryset


@admin.register(BloodBag)
class BloodBagAdmin(admin.ModelAdmin):
    list_filter = (ExpiredFilter, "blood_type")
    list_display = ("__str__", "blood_type", "donor", "source", "is_expired")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate_expired()
        return qs


@admin.register(TermQuestion)
class TermQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
