from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from . import views 

urlpatterns = [
    path("", views.home, name ="home"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
