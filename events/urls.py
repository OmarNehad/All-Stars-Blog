from django.urls import path
from .views import *


app_name = 'events'

# urls down

urlpatterns = [
    path('', EventList.as_view(), name='all'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<category>/', CategoryEventsList.as_view(), name='category_events'),
    path('categories/<category>/<int:pk>/', event_detail, name='single'),
    path('search/events', SearchResultView.as_view(), name='search_results')
    # path('new/', views.EventCreate.as_view(), name='new_event'),
    # path('<int:pk>/edit/',views.EventUpdate.as_view(), name='update'),
    # path('<int:pk>/remove',views.EventDelete.as_view(), name='delete'),
    # path('categories/<category>/<int:pk>/comment/new', new_comment, name='new_comment'),
    # path('/comment/<int:pk>/remove', views.CommentDelete.as_view(),name='delete')

]
