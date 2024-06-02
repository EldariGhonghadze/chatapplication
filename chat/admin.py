from django.contrib import admin
from .models import Question, Option


admin.site.register([Question, Option])