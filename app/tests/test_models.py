from django.test import TestCase
from app.models import *
from model_bakery import baker

class TodoTestCase(TestCase):
    def test_create(self):
        obj = baker.make('app.Todo', title = "first task")
        self.assertTrue(isinstance(obj, Todo))
        self.assertEqual(1, obj.id)
    
        obj2 = baker.make('app.Todo', title = "second task")
        self.assertTrue(isinstance(obj2, Todo))
        self.assertEqual(2, obj2.id)
    
    def test_delete(self):
        obj = baker.make('app.Todo', title = "first task")
        obj2 = baker.make('app.Todo', title = "second task")
        get_todo = Todo.objects.get(title=obj.title)
        del_todo = get_todo.delete()
        self.assertFalse(Todo.objects.filter(title=obj.title).exists())
        get_todo2 = Todo.objects.get(title=obj2.title)
        self.assertEqual(1, get_todo2.id)