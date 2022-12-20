import django_filters
from .models import Event
import datetime


class EventFilter(django_filters.FilterSet):

    CHOICES = (
    ('previous','Previous'),
    ('upcoming','Upcoming'),
    ('comming_soon','Comming soon'),
    )
    release_date = django_filters.ChoiceFilter(label='Filter by: Release Date',choices=CHOICES, method='filter_by_release')

    class Meta:
        model = Event
        fields = ['release_date']

    def filter_by_release(self, queryset, name, value):
        if value == 'previous':
            return queryset.filter(release_date__lt=datetime.date.today())
        else:
            future_date =(datetime.date.today() + datetime.timedelta(days=30))
            if value == 'upcoming':
                return queryset.exclude(release_date__lt=datetime.date.today()).filter(release_date__lte=future_date)
            elif value == 'comming_soon':
                return queryset.filter(release_date__gt=future_date)
