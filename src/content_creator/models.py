from django.db import models


class Creator(models.Model):

	PLATFORM_CHOICES = [
		("IG", "Instagram"),
		("TT", "TikTok"),
		("UG", "User Generated Content"),
	]

	name = models.CharField(max_length=50)
	username = models.SlugField(max_length=15, unique=True, blank=False)
	rating = models.DecimalField(decimal_places=2, max_digits=3)
	platform = models.CharField(max_length=3, choices=PLATFORM_CHOICES)

	def __str__(self):
		return str(self.username)


class Content(models.Model):
	creator = models.ForeignKey(Creator, on_delete=models.PROTECT)
	url = models.URLField(blank=False, null=False)

	def __str__(self):
		return str(f"Content from user -> {self.creator}")

