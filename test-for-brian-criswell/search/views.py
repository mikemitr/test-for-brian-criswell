from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from .forms import SearchForm
from .models import Search


class SearchListView(ListView):
    model = Search
    context_object_name = 'searches'


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'search/search_form.html'

    def get_success_url(self):
       return reverse('list')

    def form_valid(self, form):
        form.save()
        return super(SearchFormView, self).form_valid(form)


class SearchDetailsView(DetailView):
    model = Search
    context_object_name = 'search'
