from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    ordering = '-published_at'
    context = {'object_list': Article.objects.select_related('author').order_by(ordering).only('title', 'text', 'image',
                                                                                               'published_at',
                                                                                               'author')}

    return render(request, template_name, context)
