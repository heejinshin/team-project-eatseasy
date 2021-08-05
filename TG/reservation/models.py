from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Post(models.Model):
    userid = models.CharField('USERID', max_length=20)
    restaurant_name = models.CharField('우리 가게 이름', max_length=20)
    restaurant_description = models.CharField('가게 설명', max_length=100)
    restaurant_callnumber = models.CharField('가게 전화번호', max_length=13)
    restaurant_address = models.CharField('가게 주소', max_length=100)
    reservation_possible_date = models.DateField('영업 요일')
    reservation_time_begin = models.TimeField('영업 시작하는 시간')
    reservation_time_end = models.TimeField('영업 끝나는 시간')
    reservation_seat = models.IntegerField('예약 가능 좌석 수') 

    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
                                                            verbose_name='OWNER', blank=True, null=True)

    class Meta:
        db_table = 'restaurant_reservations'

    def __str__(self):
        return self.restaurant_name

    def get_absoulte_url(self): # 현재 데이터의 절대 경로 추출
        return reverse('reservation:detail', args=(self.id,))

    def get_previous(self): # 이전 데이터 추출
        return self.get_previous_by_modify_dt()

    def get_next(self): # 다음 데이터 추출
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        # 필드 조정 필요시 작성
        super().save(*args, **kwargs)

class Customer(models.Model):
    userid = models.CharField('USERID', max_length=20)
    customer_name = models.CharField('고객 이름', max_length=20)
    customer_callnumber = models.CharField('고객 전화번호', max_length=13)
    customer_reservation = models.BooleanField('예약 여부') 
    customer_reservation_restaurant = models.CharField('예약 식당', max_length=20) 
    customer_reservation_date = models.DateField('예약 날짜')
    customer_reservation_time = models.TimeField('예약 시간')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
                                                            verbose_name='OWNER', blank=True, null=True)


    class Meta:
        db_table = 'customer_reservations'

    def __str__(self):
        return self.customer_name

    def get_absoulte_url(self): # 현재 데이터의 절대 경로 추출
        return reverse('#', args=(self.id,))

    def get_previous(self): # 이전 데이터 추출
        return self.get_previous_by_modify_dt()

    def get_next(self): # 다음 데이터 추출
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        # 필드 조정 필요시 작성
        super().save(*args, **kwargs)