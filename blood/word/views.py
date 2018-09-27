from django.http import HttpResponse,HttpResponseRedirect
import sqlite3
from django.views import View
from django.shortcuts import render
from .models import wordinfo,mail,datepicker
import random
import re
import json
from django.http import JsonResponse
import datetime
from django.conf import settings
from django.core.mail import send_mail


now = datetime.datetime.now()
cur_date = now.strftime("%Y-%m-%d")

class index(View):
    def get(self,request):
        words = []
        context={}
        flag=0
        l=wordinfo.objects.filter(date=cur_date).first()
        words.append(l)

        count=datepicker.objects.all().count()
        if(count>=1):
            date=datepicker.objects.order_by('date')[0]
            print("date",date)
            li = wordinfo.objects.filter(date=date).first()
            words.append(li)
            flag=1

        context['words']=words
        print(type(words))
        print("c",context)
        self.datedel()
        if flag==1:
            del words[0]
            return render(request, 'word/index.html', context)
        else:
            return JsonResponse({ 'message': "**No words on this day....!!!!**"})

    def datedel(self):
        datepicker.objects.all().delete()
    def post(self,request):
        date = request.POST.get('date')
        self.datedel()
        obj=datepicker.objects.create(date=date)
        obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





def subscribe(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        nation = request.POST.get('nation')

        data_object = mail.objects.create(name=name,email=email, nation=nation)
        data_object.save()
        print(data_object)
        return JsonResponse({'success': True, 'message': "**Subscribed Successfully....!!!!**"})

    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'message': "**Subscribed Unsuccessfully...!!!**"})


#class Datastore(View):
global date
def datastore(request):
    pass



class Sendmail(View):
    def get(self, request):
        l=[]
        get_currentdate_list =[]
        split_columns_list=[]
        get_currentdate_list = str(wordinfo.objects.filter(date=cur_date).first())
        split_columns_list=re.split("-",get_currentdate_list)
        split_columns_list = "WORD OF THE DAY "+"\n"+"\n" + "WORD: "+split_columns_list[3]+ "\n" + "MEANING: "+split_columns_list[4]+ "\n" + "ANTONYM: "+split_columns_list[5]+ "\n"+ "SYNONYM: "+split_columns_list[6]+ "\n"+  "USAGE: "+split_columns_list[7]

        try:
            html_content = split_columns_list
            print(html_content)
            notification="check the email"
            emails= mail.objects.values('email')
            for i in emails:
                eachmail = i['email']
                l.append(eachmail)
            send_mail('send mail',html_content,settings.EMAIL_HOST_USER,l,fail_silently=False)
            return HttpResponse('check mail')
        except Exception as e:
            print(e)
            return HttpResponse('cannot Send email')
