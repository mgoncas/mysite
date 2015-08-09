from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # ordenamos los campos a nuestro antojo
    # fields = ['pub_date', 'question_text']

    # dividir form en fieldsets
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # agregamos la gestion de Choice dentro de Question
    inlines = [ChoiceInline]
    # definimos las columnas que queremos que aparezcan en su listado en el admin
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text', 'pub_date']




admin.site.register(Question, QuestionAdmin)
# agregar Choice, django solo detecta que estan relacionados
# admin.site.register(Choice)
