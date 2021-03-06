
from django.urls import path

from . import views
from .views import LinkListView, \
    UserProfileDetailView, UserProfileUpdateView, LinkCreateView, LinkDetailView, LinkUpdateView, LinkDeleteView, \
    VoteFormView, CommentCreateView

app_name = 'core'

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('user/<slug>', UserProfileDetailView.as_view(), name='profile'),
    path('edit-profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('create-link/', LinkCreateView.as_view(), name='create_link'),
    path('create-comment/<pk>', CommentCreateView.as_view(), name='create_comment'),
    path('link-detail/<pk>', LinkDetailView.as_view(), name='link_detail'),
    path('update-link/<pk>', LinkUpdateView.as_view(), name='update_link'),
    path('delete-link/<pk>', LinkDeleteView.as_view(), name='delete_link'),
    path('vote', VoteFormView.as_view(), name='vote'),

]