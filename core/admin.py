from django.contrib import admin
from .models import Registry
from Registry.models import Branch

class RegistryAdmin(admin.ModelAdmin):
    pass

class BranchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Registry, RegistryAdmin)
admin.site.register(Branch, BranchAdmin)
# Register your models here.
