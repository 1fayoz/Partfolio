from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length = 100, verbose_name = "To'liq ism")
    bio = models.TextField()
    image = models.ImageField(upload_to='profile/')
    link = models.URLField()

    def __str__(self) -> str:
        return self.full_name

class Servies(models.Model):
    name = models.CharField(max_length = 100)
    icon = models.CharField(max_length = 100)
    order = models.IntegerField()
    discription = models.TextField()
   

    def __str__(self) -> str:
        return self.name
    


class Skils(models.Model):
    name = models.CharField(max_length = 70)
    percentage = models.IntegerField()
    order = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Catigory(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name

class About(models.Model):
    body = models.TextField()
    amount = models.FloatField()
    project_count = models.IntegerField()
    customer_count = models.IntegerField()

    def __str__(self) -> str:
        return self.body
    

class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    poster = models.ImageField(upload_to='project/')
    link = models.URLField()
    Catigory_id = models.ForeignKey(Catigory, on_delete = models.PROTECT)
    completed_at = models.DateField(null=True)

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    punlished_at =models.DateField(auto_now= True)
    poster =  models.ImageField(upload_to='blog/')
    author = models.CharField(max_length = 100)
    dicription = models.TextField()
    view = models.IntegerField(default=0) 

class Tool(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name






