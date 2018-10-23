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
from django.contrib import messages
import tweepy
from email.mime.text import MIMEText




now = datetime.datetime.now()
cur_date = now.strftime("%Y-%m-%d")
#datesplitlist=[]
curdatelist=[]
class index(View):
    """
    def get(self,request):
        words = []
        context={}
        flag=0
        l=wordinfo.objects.filter(date=cur_date).first()
        words.append(l)
        count=datepicker.objects.all().count()
        if(count>=1):
            date= datepicker.objects.order_by('date')[0]
            li = wordinfo.objects.filter(date=date).first()
            if(li is None):
                print("words",type(words))
                messages.warning(request,"no words on this day")

            words.append(li)
            flag=1
        context['words']=words
        self.datedel()
        if flag==1:
            del words[0]
            return render(request, 'word/index.html', context)
        elif flag==0:
            return render(request, 'word/index.html', context)
    """

    def get(self, request):
        words = []
        context = {}
        flag = 0
        l = wordinfo.objects.filter(date=cur_date).first()
        words.append(l)
        count = datepicker.objects.all().count()
        if (count >= 1):
            date = str(datepicker.objects.order_by('date')[0])
            li = wordinfo.objects.filter(date=date).first()
            if (li is None):
                print("words", type(words))
                messages.warning(request, "no words on this day")

            words.append(li)
            flag = 1
        context['words'] = words
        self.datedel()
        if flag == 1:
            del words[0]
            return render(request, 'word/index.html', context)
        elif flag == 0:
            return render(request, 'word/index.html', context)
    def datedel(self):
        datepicker.objects.all().delete()
    def post(self,request):
        date = request.POST.get('date')
        print("date",date)
        self.datedel()
        obj=datepicker.objects.create(date=date)
        obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





def subscribe(request):
    try:
        flag=0
        name = request.POST.get('name')
        email = request.POST.get('email')
        nation = request.POST.get('nation')
        """
        data_object = mail.objects.create(name=name,email=email, nation=nation)
        data_object.save()
        print(data_object)
        return JsonResponse({'success': True, 'message': "**Subscribed Successfully....!!!!**"})
        """
        mailslist=[]
        emails = mail.objects.values('email')
        for i in emails:
            eachmail = i['email']
            mailslist.append(eachmail)
        print(mailslist)
        global  tag
        tag=0
        for i in mailslist:
            #print("email",email)
            #print("i",i)
            if email == i:
                flag=1
                tag=1
        if(flag==0):
            data_object = mail.objects.create(name=name, email=email, nation=nation)
            data_object.save()
            print(data_object)

            return JsonResponse({'success': False, 'message': "**Subscribed successfully...!!!**"})
        else:

            return JsonResponse({'success': True, 'message': "you subscribed earlier "})

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
        global split_columns_list
        split_columns_list=[]
        get_currentdate_list = str(wordinfo.objects.filter(date=cur_date).first())
        split_columns_list=re.split("-",get_currentdate_list)
        split_columns_list = "WORD OF THE DAY "+"\n"+"\n" + "WORD: "+split_columns_list[3]+ "\n" +   "Transliteration: "+split_columns_list[4]+ "\n" +   "MEANING: "+split_columns_list[5]+ "\n" + "SYNONYMS: "+split_columns_list[6]+ "\n"+ "INENGLISH: "+split_columns_list[7]+ "\n"+  "USAGE: "+split_columns_list[8] +"\n"+  "QUOTE: "+split_columns_list[9] +"\n"
        #split_columns_list = "WORD OF THE DAY " + "\n" + "\n" + "WORD: " + split_columns_list[3]


        l=[]

        try:
            s= "ఉప్పుగప్పురంబు న్రొక్కపోలికనుండుచూడచూడ రుచుల జాడవేరుపురుషులందు పుణ్య పురుషులువేరయవిశ్వదాభిరామ వినుర వేమ"
            html_content=split_columns_list
            s=html_content
           # msg = MIMEText(s, _charset="UTF-8")

            # print(html_content)
            notification="check the email"
            emails= mail.objects.values('email')
            for i in emails:
                eachmail = i['email']
                l.append(eachmail)
            send_mail('send mail',s,settings.EMAIL_HOST_USER,l,fail_silently=False)
            return HttpResponse('check mail')
        except Exception as e:
            print(e)
            return HttpResponse('cannot Send email')


class ONsubscribemail(View):

    def get(self, request):
        sub=[]
        email = request.POST.get('email')

        subscriber_id=[]
        try:
            html_content = "Thanks for subscribtion"
            print(html_content)
            notification="check the email"
            emails = mail.objects.values('email')
            for i in emails:
                eachmail = i['email']
                sub.append(eachmail)
            subscriber_id.append(sub[len(sub)-1])
            print("sub",sub[len(sub)-1])
            print(sub)
            print("tag",tag)
            if(tag==0):
                send_mail('send mail',html_content,settings.EMAIL_HOST_USER,subscriber_id,fail_silently=False)
                return HttpResponse('check mail')
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


        except Exception as e:
            print(e)
            return HttpResponse('cannot Send email')

class Twitter(View):
    def get(self, request):
        l = []
        get_currentdate_list = []
        global split_columns_list
        split_columns_list = []
        get_currentdate_list = str(wordinfo.objects.filter(date=cur_date).first())
        split_columns_list = re.split("-", get_currentdate_list)
        split_columns_list = "WORD OF THE DAY "+"\n"+"\n" + "WORD: "+split_columns_list[3]+ "\n" +   "Transliteration: "+split_columns_list[4]+ "\n" +   "MEANING: "+split_columns_list[5]+ "\n" + "SYNONYMS: "+split_columns_list[6]+ "\n"+ "INENGLISH: "+split_columns_list[7]+ "\n"+  "USAGE: "+split_columns_list[8] +"\n"+  "QUOTE: "+split_columns_list[9] +"\n"+  "POEM: "+split_columns_list[10]

        try:
                cfg = {
                    "consumer_key": "MvwyNlszfB3IOJS795LJoCZ5C",
                    "consumer_secret": "oDcUzL06pPFtuqR6hVxQMCWdagnJLJ02ywCH5rO9K5E6cYbMDY",
                    "access_token": "1049262181961875457-lmOqlcwLDyGoeeBOPR5QlhxYhWoUl9",
                    "access_token_secret": "0zvLzy6lb7PCJSqNBUrFaBILaKtTrsoFQ5xIl62F7U8RW"
                }

                auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
                auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])


                api = tweepy.API(auth)
                tweet = split_columns_list

                status = api.update_status(status=tweet)
                #print("status", status)
                return HttpResponse("check tweet")
                # return JsonResponse({'success': True, 'message': "tweet done..!!!**"})
        except Exception as e:
            print(e)
                # return JsonResponse({'success': False, 'message': "tweet not done...!!!**"})
            return HttpResponse("tweet not done")

