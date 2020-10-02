from django.db import models
import datetime

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# https://docs.djangoproject.com/en/2.2/topics/db/sql/

STATUS_BOOK_TICKET = [
    (0, 'Vé Mới Đặt'),
    (1, 'Vé Đã Nhận'),
    (2, 'Vé Đã Đi'),
    (3, 'Vé Không Đi')
]


class Customer(models.Model):
    id = models.AutoField
    cmnd = models.IntegerField('CMND', default=0)
    username = models.CharField('Tên Khách Hàng', max_length=50)
    phone = models.CharField('Số Điện Thoại', max_length=30)
    number_ticket = models.IntegerField('Số Vé Mua', default=0)
    number_ticket_go = models.IntegerField('Số Vé Đi', default=0)
    number_ticket_return = models.IntegerField('Số Vé Về', default=0)
    deposit = models.CharField('Tiền Đặt Cọc', max_length=50)
    money = models.CharField('Tiền Còn Thiếu', max_length=50)
    create_date = models.DateField('Ngày Nhập', default=datetime.date.today)
    start_date = models.DateField('Ngày Tàu Đi', blank=True, null=True)
    start_time_train = models.TimeField(
        'Giờ Đi', max_length=50, blank=True, null=True)
    end_date = models.DateField('Ngày Tàu Về', blank=True, null=True)
    end_time_train = models.TimeField(
        'Giờ Về', max_length=50, blank=True, null=True)
    note = models.TextField('Ghi Chú', max_length=2000)
    status = models.IntegerField(
        'Trạng Thái', default=0, choices=STATUS_BOOK_TICKET)
