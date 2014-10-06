from django.forms import ModelForm
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Search
from .utils import http_get, perform_search


class SearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('query')

        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        search = super().save(commit=False)
        search.found = False

        html = http_get(search.url)

        if html:
            begin, keywords, end = perform_search(search.query, html)

            if keywords:
                l = []

                l.extend(begin)
                l.extend(keywords)
                l.extend(end)

                search.result = ' '.join(l)
                search.found = True

        if commit:
            return search.save()
        else:
            return search

    class Meta:
        model = Search
        fields = ('query', 'url')
