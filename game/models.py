from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100,default="Vakzhak")
    slug = models.SlugField(default='vakzhak-game')
    description = models.TextField(default='vakzhak')
    image = models.ImageField(upload_to='games/')
    marketplace_links = models.JSONField(default={"ozon":'url'})  # e.g. {"ozon": "url", "wb": "url"}