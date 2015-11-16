from django.db import models
class Excuse(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content
# Create your models here.
class Users(models.Model):
    NAME = models.CharField(u'name', max_length=50)
    MAILBOX = models.CharField(u'mailbox', max_length=50)
    CELL = models.CharField(u'cell', max_length=50)
    PW = models.CharField(u'pw', max_length=50)

    def __unicode__(self):
        return self.NAME