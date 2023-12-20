from django.contrib import admin

from content_creator.models import Content, Creator

admin.site.register(Creator)
admin.site.register(Content)