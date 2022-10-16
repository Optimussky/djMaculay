from django.urls import path
from . import views
#from .views import PostListView

urlpatterns =[
        path('', views.home ,name="home"),
        path('about/', views.about, name='about-de-mis-amores'),
        #path('blog/', views.blog, name='blog'),
        #path('blog/', PostListView.as_view(), name='blog'),
        path('blog/', views.blog, name='blog'),

        
        ]
