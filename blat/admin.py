from django.contrib import admin
from blat.models import Blat, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class BlatAdmin(admin.ModelAdmin):
    list_display = ('text', 'create_on', 'total_likes')
    list_filter = ['create_on']
    search_fields = ['text']

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.register(Blat, BlatAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)