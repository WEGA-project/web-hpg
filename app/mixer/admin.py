from django.contrib import admin

# Register your models here.
from .models import Mixer, MixerHistory
from django.contrib.auth.admin import UserAdmin


from import_export import resources


from import_export.admin import  ImportExportModelAdmin

admin.site.register(Mixer,ImportExportModelAdmin)
admin.site.register(MixerHistory,ImportExportModelAdmin)
