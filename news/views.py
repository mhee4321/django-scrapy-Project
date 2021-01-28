from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, FormView
from .models import News
from .forms import RefreshForm, PostSearchForm
from django.db.models import Q
from django.shortcuts import render
import os


class NewsLV(ListView):
    model = News
    template_name = "news/news_list.html"
    paginate_by = 10

 
class NewsDV(DetailView):
    model = News   

class RefreshFormView(FormView):
    template_name = "news/news_list.html"
    form_class = RefreshForm
    success_url = '/news/list'

    def form_valid(self, form):
        print(self.request)
        os.chdir('/Users/mhee4/cloud-project')
        os.system('scrapy crawl newsbot')
        return super().form_valid(form)

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = "news/news_search.html"

    def form_valid(self, form):
        find_word = self.request.POST['search_word']
        news_list = News.objects.filter(Q(title__icontains=find_word) | Q(content__icontains=find_word) | Q(company__icontains=find_word)).distinct()

        context = {}
        context['form'] = form
        context['search_keyword'] = find_word
        context['search_list'] = news_list

        return render(self.request, self.template_name,  context)