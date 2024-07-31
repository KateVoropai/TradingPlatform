from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        "email",
        "first_name",
        "last_name"
    )
    list_display = fields
