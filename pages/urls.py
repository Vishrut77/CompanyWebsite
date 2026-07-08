from django.urls import path
from .views import home_page,AboutPage

urlpatterns = [
    path("",home_page,name="home"),
    path("about/",AboutPage.as_view(),name="about")
]