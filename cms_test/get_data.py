from django.utils import simplejson
from model import get_data
from django.http import HttpResponse
import json

def response_mimetype(request):
	if "application/json" in request.META['HTTP_ACCEPT']:
		return "application/json"
	else:
		return "text/plain"

def page_info(request):
	data = []
	res = []
	page = get_data(request.GET['page'])
	if(page == None):
		return HttpResponse(json.dumps(''), mimetype="application/json")
	print page
	if(page['product'].count > 0):
		for obj in page['product']:
			if(obj != ''):
				res += [{
					'image': obj[0],
					'url': obj[1],
					'float': obj[2]
				}]
	desc = []
	for obj in page['desc']:
		if(obj != ''):
			desc += [{
				'desc': obj[0]
			}]
	data = {"product": res, 'desc': desc}

	return HttpResponse(json.dumps(data), mimetype="application/json")
