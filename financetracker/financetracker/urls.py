from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='finance/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', include('finance.urls')),  
]
