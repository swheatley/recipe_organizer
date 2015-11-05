"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
#from django.conf.urls.defaults import *
#from tips.models import Tip 
#from voting.views import vote_on_object
from django.contrib import admin
from main import views
from django.conf import settings 
from django.conf.urls.static import static

# #tip_dict = {
#     'model': Tip,
#     'template_object_name': 'tip',
#     'slug_field': 'slug'
#     #'allow_xmlhttprequest': 'true',
# }

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipe_list_view/$', 'main.views.recipe_list_view'),
    url(r'^recipe_detail_view/(?P<pk>\d+)/$', 'main.views.recipe_detail_view'),
    url(r'^common_ingredients/$', 'main.views.common_ingredients'),

    url(r'^main_page/$', 'main.views.main_view'),
    url(r'new_entries/$', 'main.views.new_entries'),
    url(r'^cookie/$', 'main.views.cookie'),
    url(r'^cakes/$', 'main.views.cakes'),
    url(r'^dessert_bars/$', 'main.views.dessert_bars'),

    #url(r'^(?P[-\w]+)/(?Pup|down|clear)vote/?$', vote_on_object, tip_dict, name="tip-voting"),

    #url(r'^create_view1/$', 'main.views.create_view1'),
    #url(r'^create_view2/$', 'main.views.create_view2'),
    #url(r'^update_view/(?P<pk>\d+)/$', 'main.views.update_view'),
    #url(r'^delete_view/(?P<pk>\d+)/$', 'main.views.delete_view'),
    #url(r'^signup/$', 'main.views.signup'),
    #url(r'^login_view/$', 'main.views.login_view'),
    #url(r'^logout_view/$', 'main.views.logout_view'),
    


] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

