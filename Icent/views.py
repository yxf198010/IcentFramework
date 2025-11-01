from django.shortcuts import render
from .models import UserGroup
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