from django.contrib import admin, messages
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from .models import User

class UserAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'name_as_id', 'gender', 'age', 'color', 'job', 'hobby', 'food', 'fashion', 'introversion', 'heat', 'holiday', 'my_perfume', 'created_at')
    list_filter = ('created_at', 'gender', )
    date_hierarchy = 'created_at'
    search_fields = ['name']

admin.site.register(User, UserAdmin)
