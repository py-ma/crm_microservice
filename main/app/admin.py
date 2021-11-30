from django.contrib import admin
from .models import ModelsForm
'''from django.contrib.admin.models import LogEntry
LogEntry.objects.all().delete()'''
'''for delete actions in admin_panel'''
admin.site.register(ModelsForm)