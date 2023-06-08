from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


# Create your views here.
# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html')

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


# class LoginView(TemplateView):
#     template_name = 'login.html'

# class LoginView(TemplateView):
#     template_name = 'login.html'
#
#     def post(self, request):
#         data = request.POST
#         if data.get('username') == 'admin' and data.get('password') == '123456':
#             res = {'status': 0, 'msg': '登录成功'}
#         else:
#             res = {'status': 1, 'msg': '用户名或密码错误'}
#         return JsonResponse(res)


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        data = request.POST
        # django自动连接数据库校验
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user:
            res = {'status': 0, 'msg': '登录成功'}
            login(request, user)
        else:
            res = {'status': 1, 'msg': '用户名或密码错误'}
        return JsonResponse(res)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
