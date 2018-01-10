# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

from django.views import generic

from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json, requests, random, re
from pprint import pprint

# Create your views here.

disease = {
         'Cholera': ["""Are you vomiting or do you have diarrhea."""],
         'Cancer':    ["""Do you ' Have Breast Cancer , Lung Cancer."""],
         'AIDS':   ["""Have you tested' for HIV/AIDS"""]
         }

class diseaseview(generic.View):
	def get(self, request, *args, **kwargs):
        	if self.request.GET['hub.verify_token'] == '<verify_token>':
            		return HttpResponse(self.request.GET['hub.challenge'])
        	else:
            		return HttpResponse('Error, invalid token')


	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		incoming_text = json.loads(self.request.body.decode('utf-8'))

		for entry in incoming_text['entry']:
			for message in entry['messaging']:

		  		if  'message' in message:
					pprint(message)
					post_facebook_message(message['sender']['id'], message['message']['text'])
		return HttpResponse()



def post_facebook_message(fbid, recevied_message):
		tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    		disease_text = ''
	    	for token in tokens:
	        	if token in disease:
	            		disease_text = random.choice(disease[token])
	            	break

			if not joke_text:
	        		disease_text = "I didn't understand the disease! Send 'Cholera', 'Cancer', 'AIDS' for Diseases!"


		user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
		user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'<access_token>'}
		user_details = requests.get(user_details_url, user_details_params).json()
		joke_text = 'Hi '+user_details['first_name']+'..!' + disease_text

		post_message_url = '<page-access-token>'
		response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":disease_text}})
		status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
		pprint(status.json())
