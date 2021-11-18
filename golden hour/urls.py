
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from recognition import views as recog_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', recog_views.home, name='home'),
    
      path('dashboard/', recog_views.dashboard, name='dashboard'),
      path('train/', recog_views.train, name='train'),
    path('add_photos/', recog_views.add_photos, name='add-photos'),
    
     path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='recognition/home.html'),name='logout'),
     path('register/', users_views.register, name='register'),
     
     

]
