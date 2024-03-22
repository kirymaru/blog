from django.urls import path
from . import views

app_name = 'corp'

urlpatterns = [
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('Post/', views.listarPost, name='Post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/share/', views.SharePostView.as_view(), name='post_share'),
]
