from django.db import models

# Create your models here.
class Post(models.Model):
	"""docstring for Blog"""
	title = models.CharField(max_length=50)
	data = models.DateField()
	text = models.TextField()
	image = models.ImageField(upload_to='event_images')
		