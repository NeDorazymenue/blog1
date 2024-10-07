from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=127)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title
