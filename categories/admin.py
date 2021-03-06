from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    """Custom Category Admin"""

    list_display = (
        "name",
        "kind",
    )

    list_filter = ("kind",)

    search_fields = ("name",)
