from django.contrib import admin
from .models import Profile, Details, Connection, Search, SearchMessage


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Details)
admin.site.register(Connection)
admin.site.register(Search)
admin.site.register(SearchMessage)