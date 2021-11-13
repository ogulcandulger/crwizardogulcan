from django.contrib import admin
from .models import (
    MyUser,
    XML
)

# Register your models here.
admin.site.register(MyUser)
admin.site.register(XML)
