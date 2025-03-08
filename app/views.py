from django.shortcuts import render, redirect
from .models import Article, WebsiteDescription




def index(request):
    articles = Article.objects.all()
    featured_article = Article.objects.filter(is_featured=True)
    website_description = WebsiteDescription.objects.first()

    for article in articles:
        article.mins_read = article.mins_read()
        
        if article.image:
            article.image_url = article.image.url


    for featured_article in featured_article:
        featured_article.mins_read = featured_article.mins_read()

    context = {
        'articles': articles,
        'featured_article': featured_article,
        'website_description': website_description,
    }

    return render(request, 'index.html', context)


def article():
    return redirect('/')


def article_detail(request, url_hash):
    article_details = Article.objects.get(url_hash=url_hash)

    if not article_details.image:
        article_details.image.url = article_details.image_url

    context = {
        'article_details': article_details,
    }

    return render(request, 'article_detail.html', context)
        