from django.contrib import admin
from modelform.models import *

# Register your models here.
class customizewebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['name']
    list_editable=['email']
    search_fields=['url']
    list_filter=['name']
    list_per_page=3

admin.site.register(Topic)
admin.site.register(Webpage,customizewebpage)
admin.site.register(AccessRecord)