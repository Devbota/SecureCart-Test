from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views #imports Django's authentication views
from shop import views
from django.conf import settings
from django.conf.urls.static import static #handles media file delivery in program

urlpatterns = [
    path('admin/', admin.site.urls), #Django admin panel

    path('', include('shop.urls')), #all URLs defined in shop urls

    path('accounts/', include('django.contrib.auth.urls')),  #  login/logout/password-reset URLs

    path('signup/', views.signup, name='signup'),  #signup view 

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  #logout view, for user logging out
]

#For media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    


