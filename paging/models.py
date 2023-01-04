from django.db import models


class Memory(models.Model):  # ali
    size = models.IntegerField()
    page_count = models.IntegerField()


class Process(models.Model):
    PROCESS_STATUS = (
        ("P", "pending"),
        ("D", "done"),
        ("NS", "not started"),
    )
    memory = models.IntegerField()
    page_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    start_time = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=PROCESS_STATUS, max_length=3, default="NS")

    @classmethod
    def clear_process(cls):
        cls.objects.all().delete()

    @classmethod
    def generate_process(cls):
        import random

        array = []
        for i in range(10000):
            memory = random.randint(1, 10)
            duration = random.randint(1, 5)
            array.append(cls(memory=memory, duration=duration))
        cls.objects.bulk_create(array)
