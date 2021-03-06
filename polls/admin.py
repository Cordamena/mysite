from django.contrib import admin

from .models import Question, Choice

class ChoiceAdmin(admin.StackedInline):
    fieldsets = [
        ("Вариант ответа", {"fields" : ["text", "votes"]})
    ]

    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text of the question", {"fields" : ["text"]}),
        ("Date", {"fields" : ["pub_Date"]})
    ]
    inlines = [ChoiceAdmin]
    list_filter = ["pub_Date"]
    search_fields = ["text"]

admin.site.register(Question, QuestionAdmin)

