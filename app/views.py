from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Article




def index(request):
    articles = Article.objects.all()
    for article in articles:
        article.mins_read = article.mins_read()

    feat_article = Article.objects.filter(is_featured=True)
    for feat_article in feat_article:
        feat_article.mins_read = feat_article.mins_read()

    context = {
        'articles': articles,
        'feat_article': feat_article,
    }

    return render(request, 'index.html', context)


def article(request):
    return redirect('/')


def article_detail(request, url_hash):
    article_details = Article.objects.get(url_hash=url_hash)
    context = {
        'article_details': article_details,
    }

    return render(request, 'article_detail.html', context)


""" API Endpoint for 'appcron.netlify.app' """
def active(request):
    if request.method == "GET":
        return JsonResponse({'status': 'active'}, status=200)
    else:
        return JsonResponse({'status': 'error', 'message': 'Use GET request'}, status=400)
        