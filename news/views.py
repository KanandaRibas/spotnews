from django.shortcuts import render, get_object_or_404, redirect
from news.models.news_model import News
from news.models.category_model import Categories
from news.forms import CreateCategoriesForm, CreateNewsForm


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


def categories_form(request):
    form = CreateCategoriesForm()
    if request.method == "POST":
        form = CreateCategoriesForm(request.POST)

        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, 'categories_form.html', context)


def news_form(request):
    form = CreateNewsForm()
    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form}
    return render(request, 'news_form.html', context)
