from django.shortcuts import render, redirect
from .models import UserGroup
from .forms import UserGroupForm
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
