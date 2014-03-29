from django.db import models
from django.conf import settings
from datetime import datetime

class KeywordData(models.Model):
	id=models.AutoField(primary_key=True)
	keyword = models.CharField(max_length=250, null=False)
	is_active = models.BooleanField(default=True)
	last_modified=models.DateTimeField(null=False,default=datetime.now())

	class Meta:
		app_label = "tweetlistener"
		verbose_name_plural = "keyword data"

