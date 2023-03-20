from django.http import FileResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.encoding import smart_str
from django.core import serializers
import json
from datetime import datetime, timedelta
import os
import glob
import random,string
from faces.models import Survey

#from faces.fetch_s3 import fetchCSV_S3, fetchImages_S3
from faces.readcsv import createFacesRelease1, createFacesReleaseevaluation1

# relative_images_path = ''
# images_path = 'images/'    

# @api_view(["GET"])
# def getUserPatternRelease1(request):
#     pattern = createFacesRelease1()
#     return JsonResponse({'pattern':pattern},safe=False)

# @api_view(["GET"])
# def getImage(request, image_name):
#     image_data = open(relative_images_path+images_path+str(image_name)+'.jpg', "rb").read()
#     return HttpResponse(image_data, content_type="image/jpeg")


# @api_view(["POST"])
# def postResults(data):
#     try:
#         data=str(data.body.decode("utf-8"))
#         survey_instance = Survey.objects.create(data=data)
#         return JsonResponse('Data posted!',safe=False)
#     except ValueError as e:
#         print("----Error----")
#         return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

relative_images_path = ''
images_path = 'images/'    
release2_images_path = 'well_groomed_images/'
release3a_images_path = 'well_groomed_images/'
release3b_images_path = 'wg_skin_tone_images/'
release3c_images_path = 'age_images/'
release3d_images_path = 'gender_images/'
release7_images_path = ''
release8_images_path = 'election_morph_win_images/'

@api_view(["GET"])
def index(request):
    return HttpResponse('img.jpg', content_type="image/jpeg")

@api_view(["GET"])
def getUserPattern(request):
    pattern = createFacesPatternActual()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternSurvey2(request):
    pattern = createFacesPatternGAN()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease1(request):
    pattern = createFacesRelease1()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternReleaseevaluation1(request):
    pattern = createFacesReleaseevaluation1()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease2(request):
    pattern = createFacesRelease2()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease3a(request):
    pattern = createFacesRelease3a()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease3b(request):
    pattern = createFacesRelease3b()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease3c(request):
    pattern = createFacesRelease3c()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease3d(request):
    pattern = createFacesRelease3d()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease5(request):
    pattern = createFacesRelease5()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease6a(request):
    pattern = createFacesRelease6a()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease6b(request):
    pattern = createFacesRelease6b()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease7(request):
    pattern = createFacesRelease7()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getUserPatternRelease8(request):
    pattern = createFacesRelease8()
    return JsonResponse({'pattern':pattern},safe=False)

@api_view(["GET"])
def getImageRelease2(request, image_name):
    image_data = open(relative_images_path+release2_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def getImageRelease3a(request, image_name):
    image_data = open(relative_images_path+release3a_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def getImageRelease3b(request, image_name):
    image_data = open(relative_images_path+release3b_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def getImageRelease3c(request, image_name):
    image_data = open(relative_images_path+release3c_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def getImageRelease3d(request, image_name):
    image_data = open(relative_images_path+release3d_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def getImageRelease5(request, image_name):
    image_data = open(relative_images_path+release3a_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def getImageRelease7(request, image_name):
    image_data = open(relative_images_path+release7_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def getImageRelease8(request, image_name):
    image_data = open(relative_images_path+release8_images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["GET"])
def fetchCSV(request):
    if fetchCSV_S3():
        print("Fetched CSV successfully")
        return JsonResponse({'status':'success','text':'Updated the CSV successfully!!'})
    else:
        print("Error in fetching CSV")
        return JsonResponse({'status':'success','text':'Error in updating the CSV!'})

@api_view(["GET"])
def fetchImages(request):
    # Need to delete existing images
    # files = glob.glob(images_path+'*')
    # for f in files:
    #     os.remove(f)
    if fetchImages_S3():
        return JsonResponse({'status':'success','text':'Updated images successfully!!'})
    else:
        return JsonResponse({'status':'success','text':'Error in updating the images!'})

@api_view(["GET"])
def getImage(request, image_name):
    print('hiiiiiiiiiiii')
    print(image_name+'in hi')
    image_data = open(relative_images_path+images_path+str(image_name)+'.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")

@api_view(["POST"])
def getTenImgNames(data):
    ind = (data.body.decode("utf-8"))
    names = getTenSets(ind)
    return JsonResponse(names,safe=False)

@api_view(["POST"])
def postResults(data):
    try:
        print(type(data.body.decode("utf-8")))
        # data=str(data.body.decode("utf-8"))
        data=data.body.decode("utf-8")

        print('type is')
        print(type(json.dumps(data)))
        with open('results.txt','a') as f:
            f.write(str(json.loads(data)))
            f.write(',')
        survey_instance = Survey.objects.create(data=data)
        return JsonResponse('Data posted!',safe=False)
    except ValueError as e:
        print("----Error----")
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def getSurveyCount(request):
    count = Survey.objects.count()
    start_date = datetime.now() - timedelta(days=1)
    count24 = Survey.objects.filter(pub_date__gt=start_date).count()
    latest_date = Survey.objects.all().latest('pub_date').pub_date
    survey_json = Survey.objects.all()
    total = 0
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        total += obj2['score']
    return JsonResponse({'count':count,'count24':count24,'hits':total,'latest_date':str(latest_date)[:10]},safe=False)

@api_view(["GET"])
def getSurveyCount6a(request):
    count = 0
    total_score = 0
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 6 and obj2['version'] == 'a':
                count += 1
                total_score += obj2['score']
        except Exception as e:
            continue
    return JsonResponse({'count':count,'hits':total_score},safe=False)

@api_view(["GET"])
def getSurveyCount6b(request):
    count = 0
    total_score = 0
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 6 and obj2['version'] == 'b':
                count += 1
                total_score += obj2['score']
        except Exception as e:
            continue
    return JsonResponse({'count':count,'hits':total_score},safe=False)


@api_view(["GET"])
def getSurveyJson(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        res.append(obj2)
    return JsonResponse(res,safe=False)

@api_view(["GET"])
def getSurveyResults(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        res.append(obj2)
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response

@api_view(["GET"])
def getSurveyResultsRelease1(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 1:
                res.append(obj2)
        except Exception as e:
            continue
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response

@api_view(["GET"])
def getSurveyResultsRelease6a(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 6 and obj2['version'] == 'a':
                res.append(obj2)
        except Exception as e:
            continue
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response

@api_view(["GET"])
def getSurveyResultsRelease6b(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 6 and obj2['version'] == 'b':
                res.append(obj2)
        except Exception as e:
            continue
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response

@api_view(["GET"])
def getSurveyResultsRelease3b(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 3 and obj2['version'] == 'b':
                res.append(obj2)
        except Exception as e:
            continue
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response

@api_view(["GET"])
def getSurveyResultsRelease7(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 7:
                res.append(obj2)
        except Exception as e:
            continue
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response

@api_view(["GET"])
def getSurveyResultsRelease8(request):
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == 8:
                res.append(obj2)
        except Exception as e:
            continue
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response

@api_view(["GET"])
def getSurveyResultsRelease(request,id):
    print("I am called")
    print(int(id))
    survey_json = Survey.objects.all()
    res = []
    for obj in survey_json:
        obj2 = json.loads(str(obj))
        try:
            if obj2['release'] == int(id):
                res.append(obj2)
        except Exception as e:
            continue
    response = HttpResponse(str(res))
    response['Content-Type'] = 'application/force-download'
    response['Content-Disposition'] = 'attachment; filename=survey_results.txt'
    response['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response
