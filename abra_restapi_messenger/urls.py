from django.contrib import admin
from django.urls import path, include
from abra_restapi_messenger import views

urlpatterns = [
    path('', views.api_home),
    path('admin/', admin.site.urls),
    path('', include('messenger_api.urls'))

]
