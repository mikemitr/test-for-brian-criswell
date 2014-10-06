from django.db import models
from django.core.urlresolvers import reverse

class Search(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    query = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    found = models.BooleanField(default=False)
    result = models.TextField(blank=True)

    def __str__(self):
        return self.query

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
