from django.contrib import admin
from .models import UserProfile,student,teacher

admin.site.register(UserProfile)
admin.site.register(student)
admin.site.register(teacher)