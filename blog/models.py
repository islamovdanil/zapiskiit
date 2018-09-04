from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикации')
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/post/%i" % self.id

