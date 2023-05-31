from django.contrib import admin
from django.utils.html import format_html
from cars.models import Car

# Register your models here.

class CarAdmin(admin.ModelAdmin):
        
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 5px;" />'.format(object.car_photo_1.url))
    thumbnail.short_description = "Photo"
    list_display=(
        "id",
        "thumbnail",
        "car_title",
        "state",
        "model",
        "color",
        "condition",
        "is_featured",
        "price",
    )

    list_display_links=("car_title", "state")
    list_filter=("car_title", "condition", "fuel_type")
    list_editable=("condition","is_featured")
    search_fields=("car_title", "model", "color", "fuel_type")
    

admin.site.register(Car, CarAdmin)