from django.db import models

# Create your models here.

class UserGroup(models.Model):
    usergroup_name = models.CharField(max_length=50,unique=True,verbose_name="用户组名称")
    usergroup_desc = models.TextField(verbose_name="用户组描述")
    isactive = models.BooleanField(default=True, verbose_name="已激活？")
    createdate = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    createuser = models.CharField(max_length=50, verbose_name="创建人")
    updatedate = models.DateTimeField(blank=True,null=True,verbose_name="修改日期")
    updateuser = models.CharField(max_length=50,null=True,blank=True,verbose_name="修改人")

    class Meta:
        verbose_name = "用户组"
        verbose_name_plural = "用户组列表"

    def __str__(self):
        return self.usergroup_name


class SysUser(models.Model):
    userno = models.CharField(max_length=50, unique=True,verbose_name="用户工号")
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    isactive = models.BooleanField(default=True, verbose_name="已激活？")
    usergroup = models.ForeignKey('UserGroup', on_delete=models.CASCADE,default=1,verbose_name="用户组")
    email = models.EmailField(verbose_name="电子邮箱")
    birthday = models.DateField(verbose_name="生日")
    remark = models.TextField(verbose_name="备注")
    createdate = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    createuser = models.CharField(max_length=50, verbose_name="创建人")
    updatedate = models.DateTimeField(blank=True,null=True,verbose_name="修改日期")
    updateuser = models.CharField(max_length=50,blank=True,null=True,verbose_name="修改人")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户列表"

    def __str__(self):
        return self.username



