from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return "Task by {}".format(self.author)

    # def get_absolute_url(self):
    #     # refresh page
    #     return render(request, 'site/name.html', {})
