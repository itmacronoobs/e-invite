from django.contrib import admin
from .models import Customer, Group, Itinerary, Wish, Guestbook, Rsvp

admin.site.register(Customer)
admin.site.register(Group)
admin.site.register(Itinerary)
admin.site.register(Wish)
admin.site.register(Guestbook)
admin.site.register(Rsvp)
# Register your models here.
