from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view,name='home-page'),
    path('contact/', contact_view, name='contact-page'),
    path('about/',about_view,name='about-page'),
    path('blog-detail/',blogdetail_view,name='blogdetal-page'),
    path('blog/',blog_view,name='blog-page'),
    path('team/',team_view,name='team-page'),
    path('nft/',nft_view,name='nft-page'),
    path('api/posts/', PostList.as_view(), name='post-list'),
]
