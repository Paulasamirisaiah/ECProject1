from django.urls import path,include

from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('category/<int:categoryid>/',views.Category,name="Category"),
    path('product/<int:productid>/',views.Product,name="Product"),
    path('cart/',views.Cart,name="Cart"),
    path('addd/<int:productid>/<int:numb>/',views.addd,name="Addd"),
    path('remove/<int:proid>/',views.remove,name="Remove"),
]
