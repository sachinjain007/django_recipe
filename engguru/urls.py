from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from accounts.views import login_view, logout_view, register_view,homeIndex,allrecipe,commentrecipe
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homeIndex, name='index'),
    url(r'^allrecipe/', allrecipe, name='allrecipe'),
    url(r'^commentrecipe/(?P<recipeid>\w{0,50})$', commentrecipe, name='commentrecipe'),
    url(r'^login/', login_view, name='login'),
    url(r'^register/', register_view, name='login1'),
    url(r'^logout/', logout_view, name='login2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
