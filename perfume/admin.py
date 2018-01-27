from django.contrib import admin

# Register your models here.

from .models import Perfume, PerfumeComment, UserPerfume
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin





class PerfumeAdmin(ImportExportActionModelAdmin):
    list_display = ('code', 'tagtext')

class UserPerfumeAdmin(ImportExportActionModelAdmin):
    list_display = ('user', 'perfume', 'recommend_type', 'created_at')
    date_hierarchy = 'created_at'

admin.site.register(Perfume, PerfumeAdmin)
admin.site.register(PerfumeComment)
admin.site.register(UserPerfume, UserPerfumeAdmin)
