from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from django.urls import path


urlpatterns=[
     url(r'^$',views.index,name='home'),
     url(r'^newproject/$',views.new_project,name='newproject'),
     path(r'profile/',views.profile,name = 'profile'),
     url(r'^search/',views.search_results,name = 'search_results'),
     path(r'comment/<int:id>/',views.comment,name='comment'),
     path(r'rate/<int:id>/',views.rate,name='rates'),
     url(r'^api/profile/$',views.ProfileList.as_view()),
     url(r'^api/projects/$',views.ProfileList.as_view()),
     url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
     url(r'^editprofile/$',views.edit_profile,name='editprofile'),
     url(r'^logout/$',views.logout_request,name='logout')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)