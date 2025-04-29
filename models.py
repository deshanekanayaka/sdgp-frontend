from django.db import models


class LocalAccount(models.Model):
    ROLE_CHOICES = [
        ("enginner", "Engineer"),
        ("team leader", "Team Leader"),
        ("dept leader", "Dept Leader"),
        ("sr manager", "Sr Manager"),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    code = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
