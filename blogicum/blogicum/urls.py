from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
]

handler404 = 'pages.views.page_not_found'
handler403 = 'pages.views.page_not_found'
handler500 = 'pages.views.page_not_found'