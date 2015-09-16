from django.contrib import admin

# Register your models here.
from models import User, Info

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'full_name']
    class Meta:
        model = User

class InfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'gender', 'profile', 'phone']
    class Meta:
        model = Info

admin.site.register(User, UserAdmin)
admin.site.register(Info, InfoAdmin)