from django.contrib import admin
from reservation.models import Post, Customer

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('restaurant_name','restaurant_description','restaurant_callnumber','restaurant_address','reservation_time_begin','reservation_time_end')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('customer_name','customer_callnumber','customer_reservation','customer_reservation_restaurant','customer_reservation_date','customer_reservation_time')

