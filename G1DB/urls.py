"""G1DB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from G1DB_Site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.entry),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('top-locations/', views.topLocations, name="top-locations"),
    path('employee/', views.createEmployee, name="cE"),
    path('customer/', views.createCustomer, name="cC"),
    path('item/', views.item, name="item"),
    path('postLogin/', views.handleLogin),
    path('postSignUp/', views.handleSignUp),
    path('order/', views.order, name="order"),
    path('logout/', views.logout, name="logout")
]

handler404 = views.display404
handler403 = views.display403
handler400 = views.display400
handler500 = views.display500
