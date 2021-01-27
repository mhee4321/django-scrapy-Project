from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from .models import News
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def refresh(request):
    return render(request, 'news/news_list.html')


def news_list(request):
    news_list = News.objects.all()

    paginator = Paginator(news_list, 10)
    page_no = request.GET.get('page')

    try:
        news = paginator.page(page_no)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(Paginator.num_pages)

    return render(request, 'news/news_list.html', {'news':'news'})

class NewsLV(ListView):
    news_list
    model = News

 
class NewsDV(DetailView):
    model = News   