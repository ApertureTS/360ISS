from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # rendering our url for signups views, and we also have to define home in the views.py file
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # redirecting URL for thank you, also define a view
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    # the admin parameter behavoir wouldnt change so if you change "admin" to "adminabc" it would still link to the admin page
    url(r'^admin/', include(admin.site.urls)),
    # for register.html 
    url(r'^register/$', 'drinker.views.DrinkerRegistration'),
    url(r'^login/$', 'drinker.views.LoginRequest'),
    url(r'^logout/$', 'drinker.views.LogOutRequest'),

    # work in progress
    # attempting to add security for profile page
    #url(r'^profile/$', 'drinker.views.LoginRequest'),

    # working with Dropzone
    #url(r'^$dragdrop/$', 'dragdrop.views.DraggingAndDropping'),
    url(r'^dropzone-drag-drop/$', include('dragdrop.urls', namespace="dragdrop", app_name="dragdrop")),   
)


if settings.DEBUG:
    # urlpatterns add STATIC_URL and serves the STATIC_ROOT file
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)