from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
  title = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  album = models.CharField(max_length=255, null=True, blank=True)
  duration = models.IntegerField()
  spotify_id = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return f"{self.title} - {self.artist}"

class ListeningHistory(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  track = models.ForeignKey(Track, on_delete=models.CASCADE)
  listening_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username} - listened to {self.track.title} on {self.listening_date}"
  
class Recommendation(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  recommended_tracks = models.ManyToManyField(Track)

class Session(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  ip_address = models.GenericIPAddressField(null=True, blank=True)
  user_agent = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return f"Session {self.id} for {self.user.username}"
