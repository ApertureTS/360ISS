from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# for displaying images
# from django.views.generic.simple import direct_to_template
# import glob
# list_all_images = glob.glob("/static/media/user_123/*.jpg")

admin.autodiscover()

urlpatterns = patterns('',

    
    # url(r'^index/$', direct_to_template, 
    #                  { 'template':'index.html', 'extra_context': {'files':list_all_images} }
    #                  name='index' ),


    # url(r'^dropzone-drag-drop/$', include('drinker.urls', namespace="drinker", app_name="drinker")),   
    
    # Examples:
    # rendering our url for signups views, and we also have to define home in the views.py file
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     
    # redirecting URL for thank you, also define a view
    # not sure if we need this, this is a reference so we can look at the 
    # functionality
    # url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    # not sure if we need this, this is a reference so we can look at the 
    # functionality
    # url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    # the admin parameter behavoir wouldnt change so if you change "admin" to "adminabc" it would still link to the admin page
    url(r'^admin/', include(admin.site.urls)),
    # for register.html 
    url(r'^register/$', 'drinker.views.DrinkerRegistration'),
    url(r'^login/$', 'drinker.views.LoginRequest'),
    url(r'^logout/$', 'drinker.views.LogOutRequest'),

    # work in progress
    # attempting to add security for profile page
    # url(r'^profile/$', 'drinker.views.LoginRequest'),

    # working with Dropzone
    #url(r'^$dragdrop/$', 'dragdrop.views.DraggingAndDropping'),

    # url(r'^index/$', 'dragdrop.views.get_images'),
    # url(r'^index/$', 'dragdrop.views.get_image'),
    url(r'^dropzone-drag-drop/$', include('dragdrop.urls', namespace="dragdrop", app_name="dragdrop")),   
    
    # url(r'^image-upload/$', 'upload_image.views.indexer'),

    # this is for photologue
    # custom url that overides photologue urls (not working)
    # (r'^photologue/', include('photologue_custom.urls')),
    # url(r'^photologue/', include('photologue.urls', namespace='photologue')),

    # this is the url for the user to get images?
    # url(r'^get_images/$', 'drinker.views.get_images'),  

    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # url(r'^index/$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    

)


if settings.DEBUG:
    # urlpatterns add STATIC_URL and serves the STATIC_ROOT file
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # this is for photo-album
    # urlpatterns += patterns('', url(r'^accounts/', include(accounts_photo_site.urls)),)