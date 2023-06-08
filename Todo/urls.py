from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="bosh_sahifa"),
    path('rejaochir/<int:son>/', rejaochir),
    path('reja_qoshish', rejaqoshish, name="qoshish"),
]
