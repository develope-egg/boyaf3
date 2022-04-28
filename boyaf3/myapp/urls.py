from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
                  path(r'', views.index, name='index'),
                  path(r'show/', views.decument, name='decument'),
                  path(r'login/', views.login , name='login1'),
                  path(r'png/', views.png , name='png'),
                  path(r'merge/', views.merge ,name= 'name'),
                  path(r'word/', views.word ,name= 'word'),
                  path(r'tools/', views.tools , name= 'tools'),
                  path(r'success/', views.logging, name="thank"),
                  path(r'logout/', views.logout_view, name="logout1"),
                  path(r'accounts/', include('django.contrib.auth.urls')),
                  path('accounts/login/', auth_views.LoginView.as_view(template_name='log in.html')),
                  path(r'blogs/<str:id>', views.blog, name='blogs'),
                  path(r'blogs/',views.blogs, name='blog')
              ] + static(settings.MEDIA_URL, decument_root=settings.MEDIA_ROOT)
