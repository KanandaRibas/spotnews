from django.db import models
from news.models.validators import validate_title


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_title])
    content = models.TextField(default="content")
    author = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(auto_now=True)
    image = models.ImageField(
        upload_to="img/", null=True, blank=True
        )
    categories = models.ManyToManyField(
        'Categories',
        related_name="News"
        )

    def __str__(self):
        return self.title
