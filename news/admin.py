from django.contrib import admin
from .models import category_model, user_model, news_model


admin.site.register(category_model.Categories)
admin.site.register(user_model.Users)
admin.site.register(news_model.News)
