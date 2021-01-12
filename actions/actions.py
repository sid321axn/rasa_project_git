from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import json

class ActionSearchResult(Action):
	def name(self):
		return "action_result"
		
	def run(self, dispatcher, tracker, domain):
		
		intent= tracker.latest_message['intent'].get('name')
		message = {}
		message["data"]={"intent":intent}
		dispatcher.utter_custom_json(message)
