from django.shortcuts import render, get_object_or_404
from news.models.news_model import News


def index(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, news_id):
    news = get_object_or_404(News, id=news_id)
    context = {
        'news': news,
        'categories': news.categories.all()
    }
    return render(
        request, 'news_details.html', context)
