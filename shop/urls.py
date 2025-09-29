from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    # path('', views.demo, name='demo'),
    path('', views.allProdCat, name='allProdCat'),
     path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('add/', views.add, name='add'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proDetail'),
]