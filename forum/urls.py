from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^topics/(\d+)$', views.contopic),
    url(r'^topics/addlike/(\d+)$', views.addlike),
    url(r'^topics/adddislike/(\d+)$', views.adddislike),
    url(r'^topics/addcomment/(\d+)$', views.addcomment, name='add_comment'),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^view/(\S+)$', views.viewacc),
    url(r'^messages/new$', views.dialog_new, name='private_messages_new'),
    url(r'^messages$', views.dialogs, name='private_messages'),
    url(r'^pm_dialog-(\d+)$', views.dialog_read),
    url(r'^ajax$', views.ajaxtest),
    url(r'^$', views.indexpage),
]
