from django.shortcuts import render
from django.views.generic import ListView, DetailView
from reservation.models import Post, Customer

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.views import OwnerOnlyMixin

###############################################################
# 가게 목록, 가게 상세 정보
###############################################################
class PostListView(ListView):
    model = Post
    template_name = 'reservation/post_all.html'   # 템플릿 파일명 변경
    context_object_name = 'posts'                 # 컨텍스트 객체 이름 변경(object_list)
    paginate_by = 3                               # 페이지네이션, 페이지당 문서 건 수


class PostDetailView(DetailView):
    model = Post

###########################################################################################
# 가게 등록, 수정, 삭제
#########################################################
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'restaurant_name', 
        'restaurant_description', 
        'restaurant_callnumber',
        'restaurant_address',
        'reservation_possible_date',
        'reservation_time_begin',
        'reservation_time_end',
        'reservation_seat'      
                       
        ]
    success_url = reverse_lazy('reservation:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = [
        'restaurant_name', 
        'restaurant_description', 
        'restaurant_callnumber',
        'restaurant_address',
        'reservation_possible_date',
        'reservation_time_begin',
        'reservation_time_end',
        'reservation_seat'      
                       
        ]
    success_url = reverse_lazy('reservation:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('reservation:index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)



##################################################
#예약 확인, 상세 정보
##################################################

class CustomerListView(ListView):
    model = Customer                 
    template_name = 'reservation/customer_reservation.html'                         

class CustomerDetailView(DetailView):
    model = Customer


##################################################
#예약 하기, 수정하기, 삭제하기
##################################################
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = [

        'customer_name',
        'customer_callnumber',
        'customer_reservation',
        'customer_reservation_restaurant',
        'customer_reservation_date',
        'customer_reservation_time'      
                       
        ]
    success_url = reverse_lazy('reservation:customerindex')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CustomerUpdateView(OwnerOnlyMixin, UpdateView):
    model = Customer
    fields = [

        'customer_name',
        'customer_callnumber',
        'customer_reservation',
        'customer_reservation_restaurant',
        'customer_reservation_date',
        'customer_reservation_time'      
                       
        ]
    success_url = reverse_lazy('reservation:customerindex')

class CustomerDeleteView(OwnerOnlyMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('reservation:customerindex')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)