from django.contrib import admin

# Register your models here.
from .models import UserGroup
admin.site.register(UserGroup)

from .models import SysUser
admin.site.register(SysUser)