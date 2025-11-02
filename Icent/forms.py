import datetime
from django import forms
from .models import UserGroup,SysUser

class UserGroupForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = ['usergroup_name','usergroup_desc']


class SysUserForm(forms.ModelForm):
    class Meta:
        model = SysUser
        fields = ['userno', 'username', 'password', 'birthday', 'remark', 'email']
        widgets = {
            'remark': forms.Textarea(attrs={'class': 'textarea', 'rows': '5'}),
            'birthday': forms.DateInput(
                attrs={
                    'type': 'date',  # 触发浏览器原生日期选择器
                    'class': 'date-input',  # 自定义CSS类（方便样式调整）
                    'placeholder': '选择出生日期'  # 占位提示（可选）
                },
                format='%Y-%m-%d'  # 日期格式（YYYY-MM-DD，与数据库兼容）
            )
        }
        labels = {
            'birthday': '出生日期'  # 直接在 Meta 中配置标签，无需重复定义字段
        }

    # 可选：添加日期格式验证（确保输入符合要求）
    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        # 示例：禁止选择未来日期（可根据业务需求调整）
        if birthday and birthday > datetime.date.today():
            raise forms.ValidationError("出生日期不能是未来日期！")
        return birthday