from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=250, null=False)
    desc = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True)
    youtube_id = models.CharField(max_length=300, null=False)
    github_link = models.CharField(max_length=300, null=False)
    live_link = models.CharField(max_length=300, null=False)
    language = models.CharField(max_length=250, null=False)
    field = models.CharField(max_length=300, null=False)
    framework = models.CharField(max_length=250, null=False)
    skills = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        db_table = 'Project'

    def __str__(self):
        return self.title
