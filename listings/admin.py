from django.contrib import admin

from listings.views import listing

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'is_published', 'price', 'list_date', 'realtor')
    list_filter = ('realtor',)
    list_display_links = ('title','id',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'price')
    list_per_page = 10
admin.site.register(Listing, ListingAdmin)