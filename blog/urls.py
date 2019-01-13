from django.urls import path, re_path, include

from blog import views

urlpatterns = [

    re_path(r'article/(\d{4})$',views.article_year),

    re_path(r'article/(?P<year>\d{4})/(?P<month>\d{2})',views.article_year_month),
    re_path(r'article/(?P<year>\d{4})/(?P<month>\d{2})/\d+',views.article_year_month),

    re_path(r"register",views.register,name="reg"),

]