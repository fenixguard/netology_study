from django.contrib import admin
from phones.models import Phone, Feature


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


class FeatureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feature, FeatureAdmin)
