from django.db import models


class Student(models.Model):
    #id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.CharField( max_length=250)

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        ordering = ['id']


class Professor(models.Model):
    #id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.CharField( max_length=250)

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        ordering = ['id']


class Score(models.Model):
    #id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.CharField( max_length=250)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='+')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='+')
    value = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        ordering = ['id']
