from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from .models import Github
from .models import *


class GithubAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ['title','click_me']
    search_fields = ['title', 'url']


    def click_me(selfs ,obj):
        return format_html(f'<a href="{obj.url}" class="default">{obj.url}</button>')


admin.site.register(Github,GithubAdmin)