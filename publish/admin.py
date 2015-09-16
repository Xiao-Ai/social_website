from django.contrib import admin
from models import Status
# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'message', 'picture', 'timestamp']

admin.site.register(Status, StatusAdmin)
