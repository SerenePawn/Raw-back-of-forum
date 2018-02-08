from django.contrib import admin
from forum.models import Topic, TopicComments, Section, Category, PrivateMessage, Dialog # Последнее 2 удалить


class CommentsInline(admin.StackedInline):
    model = TopicComments


class TopicAdmin(admin.ModelAdmin):
    search_fields = ['topic_header', ]
    inlines = [CommentsInline]


class TopicInline(admin.StackedInline):
    model = Topic
    search_fields = ['topic_header', ]
    inlines = [CommentsInline]


class SectionAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


admin.site.register(Section, SectionAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(PrivateMessage) # To remove
admin.site.register(Dialog) # To remove
