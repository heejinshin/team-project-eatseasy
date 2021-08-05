from django.urls import path, re_path
from reservation.views import *

app_name = 'reservation'

urlpatterns = [
# 가게 목록, 상세정보
 path('', PostListView.as_view(), name='index'),
 path('<int:pk>/', PostDetailView.as_view(), name='detail'),

# 가게 등록, 수정, 삭제
 path('add/', PostCreateView.as_view(), name="add"),
 path('<int:pk>/update/', PostUpdateView.as_view(), name="update"),
 path('<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),

# 예약 등록, 확인
 path('customer/', CustomerListView.as_view(), name='customerindex'),
 path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customerdetail'),

# 예약 하기, 수정, 삭제
 path('customer/add/<int:post_id>', CustomerCreateView.as_view(), name="customeradd"),
 path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name="customerupdate"),
 path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name="customerdelete"),

]