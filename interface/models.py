from django.db import models

# Create your models here.
class AboutMe(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self) -> str:
        return super().__str__()
    
class Experience(models.Model):
    start = models.DateField()
    end =models.DateField()
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)

    def __str__(self) -> str:
        return super().__str__()

class Education(models.Model):
    start = models.DateField()
    end =models.DateField()
    industry = models.CharField(max_length=150)
    board = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

class Skill(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    subject=models.CharField()
    message=models.TextField()


    def __str__(self):
        return self.name

    @classmethod
    def create(cls,name,subject,message,email):
        contact = cls(name=name,subject=subject,message=message,email=email)
        return contact

class SocialLink(models.Model):
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()

    def __str__(self) -> str:
        return super().__str__()

class Projects(models.Model):
    projectName = models.CharField(max_length=150)
    image = models.ImageField(upload_to='interface/')
    languageUsed =models.CharField(max_length=300)
    features = models.CharField(max_length=350)

    def __str__(self) -> str:
        return super().__str__()