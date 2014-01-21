from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required as auth

from django.conf import settings
from django.conf.urls.static import static

from registration.backends.simple.views import RegistrationView

from sounds.views import SoundUploadView, SoundDetailView, SoundListView, UserProfileDetailView, UserProfileEditView, UserListView, add_audio


admin.autodiscover()

urlpatterns = patterns('',
    # ADMIN VIEWS - Just BAREBONES atm
    url(r'^admin/', include(admin.site.urls), name='admin'),
    
    # HOME PAGE - LIST OF USERS
    url(r'^$', UserListView.as_view(), name='home'),

    # LIST VIEWS
    url(r'^browse/$', SoundListView.as_view(), name='sound-list'),

    # SOUND UPLOAD VIEW
    url(r'^upload/$', SoundUploadView.as_view(), name='add-audio'),

    # Utility Django-Registration Views (Login/Logout/Register)
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name="logout"),
    url(r'^accounts/', RegistrationView.as_view(), name='register'),

    # USER PROFILE VIEWS
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
