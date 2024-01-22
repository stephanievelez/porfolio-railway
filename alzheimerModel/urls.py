from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [ #every url here, needs to start with cart/..ie cart/add/ as stated in the main urls.py
    
    path('', views.myModel, name='alzheimer-model'),
    # path('success', views.success, name='success'),
    path('prediction', views.make_prediction, name='make_prediction'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)