from django.db import models

# Create your models here.


class Vacancy(models.Model):
    name = models.CharField('Name',max_length=233,null=True)
    company_name = models.CharField('Company',max_length=50,null=True)
    salary = models.IntegerField('Salary',null=True)
    skills = models.CharField('Skill',max_length=100,null=True)
    duties = models.CharField('Duties',max_length=50,null=True)
    address = models.CharField('Address',max_length=100,null=True)

    def __str__(self):
        return self.name


class Rezume(models.Model):
    vacancy = models.ForeignKey(Vacancy,on_delete=models.CASCADE)
    name = models.CharField('Name',max_length=20)
    surname = models.CharField('Surname',max_length=20)
    patronymic = models.CharField('Patronymic',max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField('Email',max_length=255)
    skills = models.CharField('Skill', max_length=100, null=True)
    pro_experience = models.CharField('Experience',max_length=255)
    education = models.CharField('Educations',max_length=100)

    def __str__(self):
        return self.name
