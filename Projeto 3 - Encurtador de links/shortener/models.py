from django.db import models
from secrets import token_urlsafe
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Links(models.Model):
    redirect_link = models.URLField()
    token = models.CharField(max_length=12, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DurationField(null=True, blank=True)
    max_unique_clicks = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.redirect_link
    
    def save(self, *args, **kwargs):
        if not self.token:
            while True:
                self.token = token_urlsafe(6)
                if not Links.objects.filter(token=self.token).exists():
                    break
        super().save(*args, **kwargs)

    def expired(self):
        if self.expiration_time:
            return timezone.now() < self.created_at + timedelta(days=self.expiration_time.days)
        return False
        
class Clicks(models.Model):
    link = models.ForeignKey(Links, on_delete=models.CASCADE, related_name='clicks')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

