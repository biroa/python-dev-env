from django.contrib import admin

# .models = current folder
from .models import Question

# Register your models here.
admin.site.register(Question)
