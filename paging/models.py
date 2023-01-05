from django.db import models


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
    duration = models.IntegerField()
    start_time = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=PROCESS_STATUS, max_length=3, default="NS")

    @classmethod
    def clear_table(cls):
        cls.objects.all().delete()

    @classmethod
    def generate_process(cls):
        import random

        process_array = []
        for i in range(cls.process_count):
            memory = random.randint(1, 10)
            duration = random.randint(1, 2)
            process_array.append(cls(memory=memory, duration=duration))
        cls.objects.bulk_create(process_array)

        return process_array

    @classmethod
    def update_process(cls, process_array):
        return list(cls.objects.bulk_create(process_array))

    @classmethod
    def get_json_data(cls):
        return list(cls.objects.all().values('memory', 'duration', 'status', 'page_count'))


class Log(models.Model):
    time = models.IntegerField()
    content = models.JSONField(default=dict)

    @classmethod
    def clear_table(cls):
        cls.objects.all().delete()

    @classmethod
    def get_all_process_memory(cls):
        cls.objects.aggregate()
