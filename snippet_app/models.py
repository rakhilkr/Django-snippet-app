from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Tag(models.Model):
	"""Tag Model"""

	title = models.CharField(max_length=255, unique=True)


class Snippet(models.Model):
	"""Snippet Model"""

	tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now=True, db_index=True)
	title = models.CharField(max_length=255)
