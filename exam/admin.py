from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Clock)
admin.site.register(Solution)
admin.site.register(GroupQuestion)
admin.site.register(groupInlineQuestions)
