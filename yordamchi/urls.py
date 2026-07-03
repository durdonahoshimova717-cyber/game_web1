from django.urls import path
from.views import * 

urlpatterns = [
    path('', asosiy, name='asosiy'),
    path('mahsulot/', mahsulot, name='mahsulot'),
    path('haqida/', haqida, name='haqida'),
    path('product/', product, name='product'),
    path('reklama/', reklama, name='reklama'),
    path('video/', video, name='video'),
    path('contact/', contact, name='contact'),
    path('best/', product, name='best'),
    path('remot/', remot, name='remot'),
]

