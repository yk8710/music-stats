from django.contrib import admin
from .models import Track, ListeningHistory, Recommendation, Session

admin.site.register(Track)
admin.site.register(ListeningHistory)
admin.site.register(Recommendation)
admin.site.register(Session)
