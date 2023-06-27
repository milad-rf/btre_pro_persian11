from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email','is_mvp', 'hire_date')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10
    list_editable= ('is_mvp',)
admin.site.register(Realtor, RealtorAdmin)