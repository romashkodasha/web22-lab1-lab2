from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
def GetData():
   return [{'title': 'HIP-HOP', 'id': 1, 'sch': 'вторник, четверг', 'time':'19:00-20:00', 'img':'https://sun1-23.userapi.com/impf/c848524/v848524677/f8fe6/0-_aTBRsj64.jpg?size=1440x2160&quality=96&sign=59f7b845672798de987c7f1916d1d6c1&type=album'},
        {'title': 'BREAK DANCE', 'id': 2, 'sch': 'вторник, четверг', 'time':'15:00-16:00', 'img':'https://sun1-19.userapi.com/impf/c636724/v636724920/1c844/nRoLcFVTNGw.jpg?size=810x1080&quality=96&sign=d7fc2510811deb2bd0f0c71d05357c6c&type=album'},
          {'title': 'JAZZ FUNK', 'id': 3, 'sch': 'понедельник, среда', 'time':'19:00-20:00', 'img':'https://sun1-13.userapi.com/impf/c845021/v845021378/100a9d/wN7xVbcR2zs.jpg?size=1365x2048&quality=96&sign=1228a543e5d9a70fa4dd649adbc3d169&type=album'},
          {'title': 'AFRO', 'id': 4, 'sch': 'понедельник, среда', 'time':'15:00-16:00', 'img':'https://sun1-15.userapi.com/impg/ZsZXpmcUHXEkkqiB-LSgYLkFa-T0BWD84kmJuQ/7I6gUlwQJcs.jpg?size=1440x1800&quality=95&sign=ae7876acb684d69758e9c730819e8076&type=album'},
          {'title': 'DANCEHALL', 'id': 5, 'sch': 'понедельник, среда', 'time':'17:00-18:00', 'img':'https://sun9-63.userapi.com/impg/4fiXNUznFmjpaB8-NzwFH8mihMPr_GHp9-y9oQ/rZdEjBw5u8k.jpg?size=1440x2160&quality=95&sign=1bcb32538aeae903aa720a88f988247a&type=album'}]
sch=['вторник, четверг','вторник, четверг','понедельник, среда','понедельник, среда','понедельник, среда']
def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': GetData()
    }})
def GetOrder(request, id):
    return render(request, 'order.html', {'data' : GetData()[id-1]})
# Create your views here.
