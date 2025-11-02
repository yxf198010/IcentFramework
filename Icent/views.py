from django.shortcuts import render, redirect
from .models import UserGroup,SysUser
from .forms import UserGroupForm,SysUserForm
# Create your views here.

def index(request):
	"""埃讯特的主页"""
	return render(request,'Icent/index.html')

def usergroups(request):
    """显示所有的用户组"""
    usergroups = UserGroup.objects.order_by('createdate')
    context= {'usergroups': usergroups}
    return render(request,'Icent/usergroups.html', context)
    
def usergroup(request,id):
    """显示特定用户组及其所有用户"""
    usergroup = UserGroup.objects.get(id=id)
    sysusers = usergroup.sysuser_set.order_by('-createdate')
    context= {'usergroup': usergroup,'sysusers':sysusers}
    return render(request,'Icent/usergroup.html', context)

def usergroup_add(request):
    """添加新用户组"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = UserGroupForm()
    else:
        # POST提交的数据：对数据进行处理
        form = UserGroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Icent:usergroups')
    # 显示空表单或指出表单数据无效
    context = {'form': form}
    return render(request,'Icent/usergroup_add.html', context)

def sysuser_add(request, usergroup_id):
    usergroup = UserGroup.objects.get(id=usergroup_id)

    """添加新用户"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = SysUserForm()
    else:
        # POST提交的数据：对数据进行处理
        form = SysUserForm(data=request.POST)
        if form.is_valid():
            sysuser_add = form.save(commit=False)
            sysuser_add.usergroup = usergroup
            sysuser_add.save()
            return redirect('Icent:usergroup', id=usergroup_id)
    # 显示空表单或指出表单数据无效
    context = {'usergroup': usergroup,'form': form}
    return render(request,'Icent/sysuser_add.html', context)

def sysuser_edit(request, sysuser_id):
    """编辑用户"""
    sysuser = SysUser.objects.get(id=sysuser_id)
    usergroup = sysuser.usergroup

    """编辑用户"""
    if request.method != 'POST':
        # 初次请求：当前用户填充表单
        form = SysUserForm(instance=sysuser)
    else:
        # POST提交的数据：对数据进行处理
        form = SysUserForm(instance=sysuser, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Icent:usergroup', usergroup.id)
    # 显示表单或指出表单数据无效
    context = {'sysuser': sysuser,'usergroup': usergroup,'form': form}
    return render(request,'Icent/sysuser_edit.html', context)

