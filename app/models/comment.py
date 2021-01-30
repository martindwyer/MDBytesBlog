from django.db import models
from django.utils import timezone
from django.urls import reverse


class Comment(models.Model):
    class Meta: app_label = 'app'
    post = models.ForeignKey('app.Post', related_name='comments',
                             on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text


