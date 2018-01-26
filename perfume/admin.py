from django.contrib import admin

# Register your models here.

from .models import Perfume, PerfumeComment, UserPerfume

admin.site.register(Perfume)
admin.site.register(PerfumeComment)
admin.site.register(UserPerfume)
