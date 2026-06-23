from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('C', 'C'),
    ('DSA', 'DSA'),
    ('Database', 'Database'),
    ('programming','programming')
]

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    quantity = models.IntegerField()

    def __str__(self):
        return self.title


class IssueBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book.title