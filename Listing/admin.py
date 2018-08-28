from django.contrib import admin
from .models import Student
from .models import Section
from .models import ClassList

admin.site.register(Student)
admin.site.register(Section)
admin.site.register(ClassList)