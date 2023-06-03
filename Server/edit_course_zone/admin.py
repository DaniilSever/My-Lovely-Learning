from django.contrib import admin
from .views import *

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['owners']

# admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Subchapter)
admin.site.register(Lesson)
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()