from django.conf.urls import patterns, url
from .views import SearchListView, SearchDetailsView, SearchFormView

urlpatterns = patterns('',
    url(r'^$', SearchListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', SearchDetailsView.as_view(), name='detail'),
    url(r'^q/$', SearchFormView.as_view(), name='query'),
)
