from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, ListView
from utils import handle_uploaded_file
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Sound, UserProfile
from .forms import UserProfileForm, CustomerAudioFileForm

from audiofield.widgets import CustomerAudioFileWidget


def add_audio(request):
    template = 'sounds/add_audio.html'
    form = CustomerAudioFileForm()

    # Add audio
    if request.method == 'POST':
        form = CustomerAudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(username=request.user)
            obj.save()
            print 'sound saved'
            return HttpResponseRedirect('/')

        # To retain frontend widget, if form.is_valid() == False

        form.fields['audio_file'].widget = CustomerAudioFileWidget()

    data = {
       'audio_form': form,
    }

    return render_to_response(template, data,
           context_instance=RequestContext(request))


class SoundUploadView(CreateView):
    model = Sound
    fields = ['slug', 'audio_file', 'tags']

    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SoundUploadView, self).form_valid(form)




class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "sounds/user_detail.html"

    def get_object(self, queryset = None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "sounds/edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={'slug': self.request.user })


class UserListView(ListView):
    model = User



class SoundListView(ListView):
    model = Sound


class SoundDetailView(DetailView):
    model = Sound

