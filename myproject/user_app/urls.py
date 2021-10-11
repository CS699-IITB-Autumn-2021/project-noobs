from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="loginUser"),
    path('logout/',views.logout,name="logout"),
    path('product/<int:product_id>/',views.product,name="product"),   
    path('category/<str:selCategory>/',views.getProductsCategory,name="category"),
    path('search/',views.search,name="search"),
    path('myProducts/',views.myProducts,name="myProducts"),
    path('myCart/',views.myCart,name="myCart"),
]