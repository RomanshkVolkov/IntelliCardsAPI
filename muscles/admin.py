from django.contrib import admin
from .models import Muscle


class MuscleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Muscle, MuscleAdmin)
