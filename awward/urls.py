from django.conf.urls import url,include
from . import views
# from django.urls import path
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static


urlpatterns=[
     url(r'^$',views.index,name='home'),
     url(r'^newproject/$',views.new_project,name='newproject'),
     # path('profile/',views.profile,name = 'profile'),
     url(r'^search/',views.search_results,name = 'search_results'),
     # path('comment/<int:id>/',views.comment,name='comment'),
     # path('rate/<int:id>/',views.rate,name='rates'),
     url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
     url(r'^editprofile/$',views.edit_profile,name='editprofile'),
     url(r'^logout/$',views.logout_request,name='logout')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)