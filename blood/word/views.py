from django.http import HttpResponse,HttpResponseRedirect
import sqlite3
from django.views import View
from django.shortcuts import render
from .models import wordinfo,mail
import random
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
        l=wordinfo.objects.filter(date=cur_date).first()
        words.append(l)
        print(words)
        context ={'words': words }
        return render(request, 'word/index.html', context)

#getinfo()
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
def datastore(request):
    words=[]

    date = request.POST.get('date')
    date = "2018-09-19"
    """
        
        if date:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            date = cur_date
    """
    word_info = wordinfo.objects.filter(date=date).first()
    words.append(word_info)
    print(words)
    context={'words':words}
    return render(request, 'word/index.html', context)



class Sendmail(View):
    def get(self, request):
        l=[]
        L =[]
        L = str(wordinfo.objects.filter(date=cur_date).first())

        print("L",L)
        try:
            html_content = L
            print(html_content)
            notification="check the email"
            emails= mail.objects.values('email')
            for i in emails:
                eachmail = i['email']
                l.append(eachmail)
            send_mail('send mail',html_content,settings.EMAIL_HOST_USER,l,fail_silently=False)
            # send_mail('subject',html_content,'shannoburugupally14@gmail.com' ,'shubhamt547@gmail.com'] , fail_silently=False)
            return HttpResponse('check mail')
        except Exception as e:
            print(e)
            return HttpResponse('cannot Send email')
