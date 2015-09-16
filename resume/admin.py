from django.contrib import admin

# Register your models here.
from models import Education, Experience
 
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'degree', 'school', 'department']
    class Meta:
        model = Education
 
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity']
    class Meta:
        model = Experience
 
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
