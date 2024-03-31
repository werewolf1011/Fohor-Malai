from django.contrib import admin

from .models import News_Blog
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_content','news_image')

admin.site.register(News_Blog,NewsAdmin)
