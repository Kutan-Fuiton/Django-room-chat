from django.contrib import admin
from .models import Room, Message

# username: admin
# password: admin

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
