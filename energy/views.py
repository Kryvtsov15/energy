from django.shortcuts import render
from  django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.http import  HttpResponseRedirect
from django.views.generic import TemplateView
import requests

# Create your views here.


def base(request):
    return render(request, "base.html")

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = "/"
    template_name = "login.html"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class List(TemplateView):
    template_name = "info_base.html"
    def get(self, request):
        if request.user.is_authenticated:
            response = requests.get('https://68d2c478.ngrok.io/bases/')
            import_data = response.json()
            print(import_data)
            ctx = {
                "all_data": list(import_data)
            }

            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})

def page_controller(request):
    return render(request, 'pavilion.html', locals())

class Pavilion(TemplateView):
    template_name = "pavilion.html"
    def get(self, request):
        if request.user.is_authenticated:
            response = requests.get('https://82250cea.ngrok.io/getzone/73/5/')
            data_pavilion = response.json()
            print(data_pavilion)
            ctx = {
                "inf_pavilion": list(data_pavilion)
            }

            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class Zone(TemplateView):
    template_name = "zone.html"
    def get(self, request):
        if request.user.is_authenticated:
            response = requests.get('https://ea93a823.ngrok.io/getzone/73/1/')
            data_zone = response.json()
            # print(data_zone)
            ctx = data_zone[0]
            # ctx = {
            #     "inf_zone": list(data_zone)
            # }
            # print(ctx.get('controllers'))
            # print(ctx)
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})