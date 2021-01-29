from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.db.models import Q
from .models import Stock
from .forms import SearchForm
import os

class StockLV(ListView):
    model = Stock
    template_name = "stock/stock_list.html"
    paginate_by = 10

class StockDV(DetailView):
    model = Stock


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = "stock/stock_search.html"
    success_url = '/stock/search'

    def form_valid(self, form):
        seword = self.request.POST['search_word']

        os.chdir('/Users/mhee4/cloud-project')
        os.system('python stockParser.py {0}'.format(seword))

        stock_list = Stock.objects.filter(Q(name__icontains=seword)).distinct()

        context = {}
        context['search_keyword'] = seword
        context['search_list'] = stock_list

        return render(self.request, self.template_name,  context)
        # return super().form_valid(form)
