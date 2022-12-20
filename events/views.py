from django.shortcuts import render
from django.views.generic import (CreateView,UpdateView,ListView,DetailView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import *
from django.urls import reverse_lazy
from braces.views import SelectRelatedMixin
from django.shortcuts import get_object_or_404, render,redirect
from .forms import CommentForm
from .filters import  EventFilter
from django.db.models import Q

# Create your views here.

# Events view:

class CategoryList(ListView):
    model = Category


class CategoryEventsList(ListView):
    template_name = "events/category_events_list.html"

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Event.objects.filter(category=self.category)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilter(self.request.GET, queryset=self.get_queryset())
        return context

class EventList(ListView):
    model = Event

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilter(self.request.GET, queryset=self.get_queryset())
        return context

class SearchResultView(ListView):
    model = Event
    template_name = 'events/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Event.objects.filter(
        Q(title__contains=query) | Q(summary__contains=query)
        )
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

# class EventCreate(CreateView,LoginRequiredMixin):
#     model = Event
#     fields = ('title','text','image')

# class EventUpdate(UpdateView,LoginRequiredMixin):
#     model = Event
#     fields = ('title','text','image')

# class EventDelete(DeleteView,LoginRequiredMixin):
#     model = Event
#     success_url = reverse_lazy('events:all')


#
# class EventDetail(DetailView):
#     model = Event
#
# def new_comment(request, pk, category):
#     event = get_object_or_404(Event,pk=pk)
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             comment.event = event
#             # Save the comment to the database
#             comment.save()
#             return redirect('events:single', pk=pk, category=category)
#     else:
#         comment_form = CommentForm()
#
#     return render(request, 'events/comment_form.html', {'comment_form': comment_form})



def event_detail(request, pk, category):
    template_name = 'event_detail.html'
    event = get_object_or_404(Event, pk=pk)

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            comment.event = event
            # Save the comment to the database
            comment.save()

            return redirect('events:single', pk=pk, category=category)

    else:
        comment_form = CommentForm()

    return render(request, 'events/event_detail.html', {'event': event,
                                           'comment_form': comment_form})

# class  CommentDelete(DeleteView,LoginRequiredMixin):
#     model = Comment
#     success_url = reverse_lazy('events:single')
