
from django.contrib import admin
from .models import Nurse


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):

    list_display = (
        'nurse_id',
        'name',
        'age',
        'gender',
        'department',
        'phone',
    )

    search_fields = (
        'name',
        'nurse_id',
        'department',
    )

    list_filter = (
        'gender',
        'department',
    )
