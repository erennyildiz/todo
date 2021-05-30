from django.db import models
from django.db.models import F, Max

class Todo(models.Model):
    title = models.CharField(max_length=50, verbose_name = "Title")
    completed = models.BooleanField(verbose_name= "State")

    def save(self, *args, **kwargs):
        try:
            todo_id = Todo.objects.last().id + 1
        except:
            todo_id = 1
        self.id = todo_id
        super(Todo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        objects = Todo.objects.filter(id__gt = self.id)
        super(Todo, self).delete(*args, **kwargs)
        objects.update(id=F('id') - 1)
