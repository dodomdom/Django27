# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from comments.models import Comment

from django.utils.safestring import mark_safe
from markdown_deux import markdown


def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

Classify_Choises = (
    ('잡담','잡담'),
    ('컴퓨터', '컴퓨터'),
    ('영화','영화'),
    ('게임','게임'),
    ('드라마','드라마'),
    ('문의','문의'),
)

class Post(models.Model):
	classify = models.CharField(max_length=10, choices=Classify_Choises, default='잡담')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to=upload_location,
			null=True,
			blank=True, 
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("main:detail", kwargs={'id': self.id})
		
	def get_absolute_delete(self):
		return reverse("main:delete", kwargs={'id': self.id})

	class Meta:
		ordering = ["-timestamp", "-updated"]

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)

	@property
	def comments(self):
		instance = self
		qs =Comment.objects.filter_by_instance(instance)
		return qs
		
	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

	


# Create your models here.
