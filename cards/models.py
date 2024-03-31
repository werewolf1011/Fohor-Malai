from django.db import models

# Create your models here.
from tinymce.models import HTMLField
from autoslug import AutoSlugField


# Create your models here.
class News_Blog(models.Model):
    news_image = models.FileField(
        upload_to="cards/", max_length=250, null=True, default=None
    )
    news_title = models.CharField(max_length=100)
    news_content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
