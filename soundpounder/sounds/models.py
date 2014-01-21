from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from django.conf import settings
from audiofield.fields import AudioField
import os.path

from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique= True)
    bio = models.TextField(null = True)

    def __unicode__(self):
        return "%s's profile" % self.user


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

    # Signal while saving user
    post_save.connect(create_profile, sender=User)


class Sound(models.Model):
    slug = models.SlugField(max_length=250)
    audio_file = AudioField(upload_to='sounds', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))

    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="sounds")

    tags = TaggableManager()


    def __unicode__(self):
        return self.slug

    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<ul class="playlist"><li style="width:250px;">\
            <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
            return player_string

    
    

#audio_file_player.allow_tags = True
#audio_file_player.short_description = _('Audio file player')
