from django.conf.urls import url
from .views import StudentList, StudentDetail, Download

urlpatterns = [
    url(r'^$', StudentList.as_view()),
    url(r'^(?P<pk>\d+)/$', StudentDetail.as_view()),
    url(r'^download/(?P<pk>\d+)/$', Download.as_view())
]
