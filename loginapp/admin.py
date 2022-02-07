from django.contrib import admin

# Register your models here.
from django.contrib import admin
from loginapp.models import Customer
from room_managerapp.models import RoomManager
from bookingapp.models import Contact,Rooms,Booking
# Register your models here.
admin.site.register(Customer)
admin.site.register(RoomManager)
admin.site.register(Contact)
admin.site.register(Rooms)
admin.site.register(Booking)