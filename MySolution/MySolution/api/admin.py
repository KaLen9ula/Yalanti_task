from django.contrib import admin
from .models import Courses


# Register our model in admin.
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'lectures_num')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')


admin.site.register(Courses, CoursesAdmin)
