# sounds/forms.py
import os
from django import forms
from .models import UserProfile, Sound

from django.core.exceptions import ValidationError

from audiofield.forms import AudioFormField, CustomerAudioFileForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )



"""
class SoundUploadForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            if file._size > 20 * 1024 * 1024:
                raise ValidationError("Audio file too large ( > 4mb) )")
            if not os.path.splitext(file.name)[1] in [".mp3", ".wav"]:
                raise ValidationError("Doesn't have proper extension")
            return file
        else:
            raise ValidationError("Couldn't read uploaded file")

    class Meta:
        model = Sound
"""