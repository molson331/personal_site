from django.db import models


class Image(models.Model):
	filename = models.CharField(max_length=32)

	def __unicode__(self):
		return self.filename

	class Meta:
		ordering = ['id']


class Event(models.Model):
	title = models.CharField(max_length=16)
	image = models.ForeignKey(Image, on_delete=models.PROTECT)

	class Meta:
		ordering = ['id']


class Caption(models.Model):
	event = models.ForeignKey(Event, related_name='captions', on_delete=models.CASCADE)
	description = models.CharField(max_length=1024)

	class Meta:
		ordering = ['id']