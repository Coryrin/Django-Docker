from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)

    def get_title(self):
        return self.title
