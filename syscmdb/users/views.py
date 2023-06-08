from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from faker import Faker

from users.models import *


# Create your views here.


# class UserListView(View):
#     def get(self, request):
#         data = User.objects.all()
#         return render(request, 'user_list.html', {'data': data})

class UserListView(ListView):
    template_name = 'user_list.html'
    model = User
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['page_range'] = self.page_range(context['page_obj'], context['paginator'])
        return context

    def page_range(self, page_obj, paginator):
        current_page = page_obj.number
        start = current_page - 2
        end = current_page + 3
        if start < 1:
            start = 1
        if end > paginator.num_pages:
            end = paginator.num_pages + 1
        return range(start, end)


class TestDataView(View):
    def get(self, request):
        fk = Faker(locale="zh-CN")
        for i in range(1, 100):
            user = User()
            profile = Profile()
            user.username = fk.user_name()
            user.password = make_password('123456')
            user.email = fk.email()
            user.save()
            profile.profile_id = user.id
            profile.name_cn = fk.name()
            profile.wechat = fk.user_name()
            profile.phone = fk.phone_number()
            profile.info = '测试用户{}'.format(i)
            profile.save()


class UserAddView(TemplateView):
    template_name = 'user_add.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}

        try:
            user = User()
            profile = Profile()
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.save()
            profile.profile_id = user.id
            profile.name_cn = data.get('name_cn')
            profile.wechat = data.get('wechat')
            profile.phone = data.get('phone')
            profile.info = ''
            profile.save()
        except Exception:
            res = {'status': 1, 'msg': '添加失败'}
        return JsonResponse(res)


class UserUpdateView(View):
    def get(self, request):
        return render(request, 'user_update.html', {'user_obj': User.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '修改成功'}

        try:
            user = User.objects.get(id=data.get('uid'))
            profile = Profile.objects.get(profile_id=data.get('uid'))
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.save()
            profile.profile_id = user.id
            profile.name_cn = data.get('name_cn')
            profile.wechat = data.get('wechat')
            profile.phone = data.get('phone')
            profile.info = ''
            profile.save()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '修改失败'}
        return JsonResponse(res)


class UserDeleteView(View):
    def get(self,request):
        data = request.GET
        res = {'status':0,'msg':'删除成功'}
        try:
            User.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status':0,'msg': '删除失败'}
        return JsonResponse(res)


class UserStatusView(View):
    def get(self,request):
        data = request.GET
        res = {'status':0,'msg':'用户状态更新成功'}
        user = User.objects.get(id=data.get('id'))
        status = user.is_active
        if status == 0:
            newstatus = 1
        else:
            newstatus = 0
        try:
            user.is_active = newstatus
            user.save()
        except Exception as e:
            print(e)
            res = {'status':0,'msg': '用户状态更新失败'}
        return JsonResponse(res)
