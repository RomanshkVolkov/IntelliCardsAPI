from django.contrib import admin
from .models import Muscle, Folder, CustomUser


class MuscleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Muscle, MuscleAdmin)
admin.site.register(Folder)
admin.site.register(CustomUser)
