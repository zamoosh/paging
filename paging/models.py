from django.db import models


class Process(models.Model):
    PROCESS_STATUS = (
        ("P", "pending"),
        ("D", "done"),
        ("NS", "not started"),
    )
    memory = models.IntegerField()
    duration = models.IntegerField()
    status = models.CharField(choices=PROCESS_STATUS, max_length=3)


class Pages(models.Model):
    size = models.IntegerField()
    status = models.BooleanField(default=False)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)


class Memory(models.Model): # ali
    size = models.IntegerField()
