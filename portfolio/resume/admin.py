from django.contrib import admin

from .models import Experience
from .models import Education

admin.site.register(Experience)
admin.site.register(Education)