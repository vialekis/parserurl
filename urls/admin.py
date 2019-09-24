from django.contrib import admin

# Register your models here.
from urls.models import URLItem

@admin.register(URLItem)
class URLItemAdmin(admin.ModelAdmin):
    list_display = ('id','url','key_word','count_word','datestamp','date_create','status')
