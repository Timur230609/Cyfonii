from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view,name='home-page'),
    path('contact/', contact_view, name='contact-page'),
    path('3dcarousel/', carousel_view, name='carusel-page'),
    path('about/',about_view,name='about-page'),
    path('advisor/',advisor_view,name='advisor-page'),
    path('autor02',author02_view,name='author-page'),
    path('blog-detail/',blogdetail_view,name='blogdetal-page'),
    path('blog/',blog_view,name='blog-page'),
    path('cardcarousel/',cardcarousel_view,name='card-page'),
    path('coverflowercarousel/',coverflowcarousel_view,name='cowerflow-page'),
    path('help-center/',helpcenter_view,name='help-page'),
    # path('home-v2/',homev2_view,name='home2-page'),
    # path('home-v3/',homev3_view,name='home3-page'),
    path('3dcarousel/',trid_view,name='trid-page'),
    path('iteamcarousel/',iteamcarousel_view,name='item-page'),
    path('nft/',nft_view,name='nft-page'),
    path('parti-asset/',partiasset_view,name='partiasset-page'),
    path('partner/',partner_view,name='partner-page'),
    path('roadmap/',roadmap_view,name='roadmap-page'),
    path('team/',team_view,name='team-page'),
    path('vision-mission/',visionmission_view,name='vision-page'),
    path('zigzagcarousel/',zigzagcarousel_view,name='zigzag-page'),
]
