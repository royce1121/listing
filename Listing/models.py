from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=128)


    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=128)
    Section = models.ManyToManyField(Student, through='ClassList')

    def __str__(self):
        return self.name

class ClassList(models.Model):
    person = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Section, on_delete=models.CASCADE)