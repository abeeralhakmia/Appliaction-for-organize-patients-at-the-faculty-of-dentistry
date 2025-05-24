from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
from django.http import HttpResponse,JsonResponse
import json
#انشاء حساب
@csrf_exempt
def register(request):
    try:
        body_unicode = request.body.decode ('utf-8') 
        body = json.loads (body_unicode)
        name=body["name"]
        age=body["age"]
        favouritesports=body["favouritesports"]
        un=body["user_name"]
        pw=body["password"]
        o=User(name=name,age=age,favouritesports=favouritesports,user_name=un,password=pw)
        o.save()
        #return JsonResponse({"result":o.id})
        return JsonResponse({"result":"ok"})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})
        #return JsonResponse({"result":e})
#تسجيل دخول
@csrf_exempt
def login(request):
    try:
        body_unicode = request.body.decode ('utf-8') 
        body = json.loads (body_unicode)
        un=body["user_name"]
        pw=body["password"]
        o=User.objects.get(user_name=un,password=pw)
        d={}
        d["id"]=o.id
        d["name"]=o.name
        d["age"]=o.age
        d["favourite"]=o.favouritesports
        return JsonResponse({"result":"ok","data":d})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})
   #getلاحضار الاقسام الثلاثة بطلب 
@csrf_exempt
def getAllsections(request):
    try:
        data=[]
        obj=section.objects.all()
        for o in obj:
            d={}
            d["id"]=o.id
            d["name"]=o.name
            d["img"]="http://localhost:8000//media//section_img//"+o.img.path.split("\\")[-1]
            data.append(d)
        return JsonResponse({"result":"ok","data":data})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})
    #لاحضار اقسام الرياضات 
@csrf_exempt
def getAllSports(request):
    try:
        data=[]
        obj=sports.objects.all()
        for o in obj:
            d={}
            d["id"]=o.id
            d["name"]=o.name
            d["type"]=o.type
            d["img"]="http://localhost:8000//media//section_img//"+o.img.path.split("\\")[-1]
            data.append(d)
        return JsonResponse({"result":"ok","data":data})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})

@csrf_exempt
def getsportsById(request):
    try:
        body_unicode = request.body.decode ('utf-8') 
        body = json.loads (body_unicode)
        id1=body["id"]
        print(id1)
        data=[]
        o=sports.objects.get(id=id1)
        d={}
        d["name"]=o.name
        l=[]
        for im_obj in sportsImage.objects.filter(sport=o):
            l.append("http://localhost:8000//media//section_img//"+im_obj.img.path.split("\\")[-1])
        d["imgs"]=l
        l2=[]
        for im_obj in sportsvideo.objects.filter(sport=o):
            l2.append("http://localhost:8000//media//section_img//"+im_obj.video.path.split("\\")[-1])
        d["videos"]=l2
        l=[]
        for com_obj in sportadvice.objects.filter(sport=o):
            l.append(com_obj.advice)
        d["advices"]=l
        l=[]
        for com_obj in sportsclub.objects.filter(sport=o):
            c={}
            c["name"]=com_obj.name
            c["location"]=com_obj.location
            l.append(c)
        d["clubs"]=l
        data.append(d)
        return JsonResponse({"result":"ok","data":data})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})
    

#لاحضار اقسام المعالجة الفيزيائية
@csrf_exempt
def getAllPhysicals(request):
  try:
        data=[]
        obj=physicalTherapy.objects.all()
        for o in obj:
            d={}
            d["id"]=o.id
            d["name"]=o.name
            d["type"]=o.type
            d["img"]="http://localhost:8000//media//section_img//"+o.img.path.split("\\")[-1]
            data.append(d)
        return JsonResponse({"result":"ok","data":data})
  except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})

@csrf_exempt
def getphysicalTherapyById(request):
    try:
        body_unicode = request.body.decode ('utf-8') 
        body = json.loads (body_unicode)
        id1=body["id"]
        print(id1)
        data=[]
        o=physicalTherapy.objects.get(id=id1)
        d={}
        d["name"]=o.name
        l=[]
        for im_obj in physicalImage.objects.filter(sport=o):
            l.append("http://localhost:8000//media//section_img//"+im_obj.img.path.split("\\")[-1])
        d["imgs"]=l
        l2=[]
        for im_obj in physicalvideo.objects.filter(sport=o):
            l2.append("http://localhost:8000//media//section_img//"+im_obj.video.path.split("\\")[-1])
        d["videos"]=l2
        l=[]
        for com_obj in physicaladvice.objects.filter(sport=o):
            l.append(com_obj.advice)
        d["advices"]=l
        l=[]
        for com_obj in physicalCenter.objects.filter(sport=o):
            c={}
            c["name"]=com_obj.name
            c["location"]=com_obj.location
            l.append(c)
        d["clubs"]=l
        data.append(d)
        return JsonResponse({"result":"ok","data":data})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})

@csrf_exempt
def getAllFeeds(request):
  try:
        data=[]
        obj=feed.objects.all()
        for o in obj:
            d={}
            d["id"]=o.id
            d["name"]=o.name
            d["type"]=o.type
            d["img"]="http://localhost:8000//media//section_img//"+o.img.path.split("\\")[-1]
            data.append(d)
        return JsonResponse({"result":"ok","data":data})
  except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})    

@csrf_exempt
def getfeedById(request):
    try:
        body_unicode = request.body.decode ('utf-8') 
        body = json.loads (body_unicode)
        id2=body["id"]
        data=[]
        obj=feed.objects.filter(id=id2)
        for o in obj:
            d={}
            d["name"]=o.name
            l=[]
            for im_obj in feedImage.objects.filter(sports=o):
                l.append("http://localhost:8000//media//physicalImage//"+im_obj.img.path.split("\\")[-1])
            d["imgs"]=l
            
            l1=[]
            for com_obj in feedadvice.objects.filter(sports=o):
                dd={}
                dd["advice1"]=com_obj.advice
                l1.append(dd)
            d["advice"]=l1
            data.append(d)
        return JsonResponse({"result":"ok","data":data})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"error"})

