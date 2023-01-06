import random
from django.db import models
from django.db.models import F


class Memory(models.Model):
    size = models.IntegerField(null=True)
    page_size = models.IntegerField(null=True)
    left_memory = models.IntegerField(null=True)
    page_count = models.IntegerField(null=True)
    left_page = models.IntegerField(null=True)

    @classmethod
    def get_memory(cls):
        if cls.objects.exists():
            return cls.objects.first()
        return cls.objects.create()


class Process(models.Model):
    process_count = 4

    PROCESS_STATUS = (
        ("P", "pending"),
        ("D", "done"),
        ("NS", "not started"),
    )
    memory = models.IntegerField()
    page_count = models.IntegerField(default=0)
    init_duration = models.IntegerField(null=True)
    duration = models.IntegerField()
    start_time = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=PROCESS_STATUS, max_length=3, default="NS")

    @classmethod
    def clear_table(cls):
        cls.objects.all().delete()

    @classmethod
    def generate_process(cls, process_count=None):
        process_array = []
        if process_count:
            cls.process_count = process_count
        for i in range(cls.process_count):
            memory = random.randint(1, 10)
            duration = random.randint(1, 2)
            process_array.append(cls(memory=memory, duration=duration, init_duration=duration))
        cls.objects.bulk_create(process_array)
        return process_array

    @classmethod
    def update_process(cls, process_array):
        return list(cls.objects.bulk_create(process_array))

    @classmethod
    def get_json_data(cls, paging=False):
        if paging:
            return list(cls.objects.all().values('status', 'memory', 'start_time', 'duration', 'init_duration').annotate(left_time=F('start_time') + F('duration')))
        return list(cls.objects.all().values('status', 'memory', 'start_time', 'duration', 'init_duration').annotate(left_time=F('start_time') + F('duration')))


class Log(models.Model):
    time = models.IntegerField(unique=True)
    content = models.JSONField(default=dict)
    type = models.CharField(max_length=10)

    @classmethod
    def get_object(cls, time):
        obj = cls.objects.filter(time=time)
        if obj:
            return obj.first()
        return None

    @classmethod
    def clear_table(cls):
        cls.objects.all().delete()

    @classmethod
    def get_all_process_memory(cls):
        cls.objects.aggregate()

    def get_len(self):
        return len(self.content)
