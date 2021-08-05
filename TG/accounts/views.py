from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied

class UserCreateView(generic.CreateView): 
 template_name = 'registration/register.html' 
 form_class = UserCreationForm
 success_url = reverse_lazy('accounts:register_done') 
 
class UserCreateDoneView(generic.TemplateView): 
 template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):

        self.object = self.get_object() # 모델 인스턴스 얻기

        if self.request.user != self.object.owner:

            self.handle_no_permission()
            
        return super().get(request, *args, **kwargs)