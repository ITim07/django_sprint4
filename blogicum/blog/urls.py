from django.urls import path
from . import views

app_name = 'blog'  

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit_comment/<int:post_id>/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:post_id>/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
