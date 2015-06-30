# coding=UTF-8
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import sys
reload(sys)
sys.setdefaultencoding('utf8')

@csrf_exempt
def index_view(request):
    return render_to_response('dateapp/index.html',locals())
