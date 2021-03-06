from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.utils.text import slugify


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100) #colum
    # location
    job_type = models.CharField(max_length=60,choices=JOB_TYPE)
    discription = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy =models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug =models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title) 
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
   
class Category(models.Model):
    name =models.CharField(max_length=60)
    def __str__(self):
     return self.name

class Apply(models.Model):
     job = models.ForeignKey(Job,related_name='job_apply',on_delete=models.CASCADE)
     name = models.CharField(max_length=60)
     email = models.EmailField(max_length=100)
     website = models.URLField()
     cv = models.FileField(upload_to="apply")
     cover_lettre = models.TextField(max_length=500)
     created_at = models.DateTimeField(auto_now=True) 

     def __str__(self):
         return self.name