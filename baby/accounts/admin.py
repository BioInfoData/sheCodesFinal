from django.contrib import admin
from .models import Profile, Details, Connection


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Details)
admin.site.register(Connection)