from django.contrib import admin
from testsite.models import *



class QuestionsAdmin(admin.ModelAdmin):
    # form = NewsAdminForm
    list_display = ('id', 'question_text', 'question_number', 'professional')
    list_display_links = ('professional', 'question_text')
    search_fields = ('id','professional', 'question_text')
    list_filter = ('professional',)
    save_on_top = True
    fields = ('question_number', 'question_text', 'professional', 'a', 'b', 'c', 'd' )
    readonly_fields = ('id', 'created_at',)

class ChoiceAdmin(admin.ModelAdmin):
    # form = NewsAdminForm
    list_display = ('id', 'choice_text', 'question', )
    list_display_links = ('id', 'question')
    search_fields = ('id', 'choice_text')
    list_filter = ('choice_text', 'question')
    save_on_top = True

class ProfTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True


admin.site.register(ProfTest, ProfTestAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answers)
