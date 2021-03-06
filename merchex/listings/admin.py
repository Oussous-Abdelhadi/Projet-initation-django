import imp
from django.contrib import admin

# Register your models here.

from listings.models import Band
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):
    list_display= ('name', 'year_formed', 'genre')

class ListingAdmin(admin.ModelAdmin):
    list_display= ('title', 'sold', 'type', 'band')
    
admin.site.register(Band, BandAdmin )
admin.site.register(Listing, ListingAdmin)
