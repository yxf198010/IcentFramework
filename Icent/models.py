from django.db import models

# Create your models here.
class SysUser(models.Model):
    userno = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    isactive = models.BooleanField(default=True)
    Created = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()
    remark = models.TextField(max_length=200)
    createdate = models.DateTimeField(auto_now_add=True)
    createuser = models.CharField(max_length=50)
    updatedate = models.DateTimeField(auto_now=True)
    updateuser = models.CharField(max_length=50)

    def __str__(self):
        return self.username
