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
		item = tracker.get_slot('item')
		item = item.lower()
		
		
		#dispatcher.utter_message(loc)
		if item =="debt":
			dispatcher.utter_message("**Tax Debt - Things You Should Know When You Owe the IRS Money** \n For those of you who happen not to be seasoned tax professionals, dealing with the **IRS** can be fairly intimidating.\n Even if you know what you're doing and have done nothing wrong, it can still be an intimidating experience.The less you understand about the workings of the IRS, the more intimidated you may feel. \n If you find yourself owing tax debt to the IRS, whether intentional or not, it's important to resolve things as quickly as possible. \n When you owe the IRS,, no amount of burying your head in the sand will help because the problem will not go away by itself.")
		elif item =="unfiled":
			dispatcher.utter_message("Although the IRS has received a record number of returns this year, there are still millions of people and business owners who did not file tax returns by April 15th. The reasons for this are numerous, but the IRS research shows that often people do not file in years that their status changes, for instance the death of a spouse or a divorce. \n Emotional or financial hardship reasons may also cause a person not to file. And then there are some folks who have simply procrastinated. Whatever your reason is, if you did not file your taxes by April 15th, you should stop putting it off and file your tax returns as soon as possible - even if you are late.")
		elif item =="audit":
			dispatcher.utter_message("**Tax Representative** or **Defender** are the people whose job it is to keep up on all of the changes in order to be able to help the taxpayer to get the best representation possible. \n For that reason alone, it is very good that the IRS only allows a select group of qualified individuals to be able to represent a taxpayer during an IRS or state audit.")
		elif item=="employment":
			dispatcher.utter_message("When a 941 tax problem crisis falls on a business in the form of heavy back taxes, every other normal situation also seems to fall apart. \n Hard time is just seconds away from our lives. Among all the tax problems, 941 tax problems is a major hurdle in ones life. \n How To Deal With 941 Payroll Tax Problems. Visit Help here.")
		elif item=="lien":
			dispatcher.utter_message("Today's economy is quite jerky. One of the hottest issues all around somehow or the other concerns the current economic crises which is making people still suffer. Because of these hardships numerous people as well as companies have fallen prey to the tax payment delays causing the IRS to file tax liens. Since they lacked the finances to pay for the taxes the need for tax representation became greater. \n To know more visit here.")
		elif item=="fees":
			dispatcher.utter_message("Our fees for an Offer in Compromise are reasonably based on a flat rate and the terms of our engagement will be presented to you during your **FREE** consultation.")
		elif item=="433":
			dispatcher.utter_message("IRS 433 form - Why Should You Consider Professional Help  The IRS is one of the most powerful of all of the government agencies and they wield considerable power when it comes interacting with them. When it comes tax debt and working with the IRS there are established rules and forms that are in place to help you resolve your back tax problem.  So it is imperative that you figure out how to complete the IRS Form 433 and each of the associated forms.  Each of the following forms was established to be filled out by the taxpayer and submitted for review by the IRS; 433-A, 433-B, 433-D, and 433-F. Each of the forms has a designed purpose and each one has to be filled out in a certain way in order for the IRS to even consider accepting them and acting on them.  To know in details visit https://www.myirstaxrelief.com/irs-433-form-help.html")
		elif item=="433-a":
			dispatcher.utter_message("IRS form 433-a is known as __the Collection Information Statement for Wage Earners and Self-Employed Individuals__, this is where the IRS gathers all of your income and living expenses information when you are looking settle with the IRS. To know more visit https://www.myirstaxrelief.com/irs-433-form-help.html")
		elif item=="433-b":
			dispatcher.utter_message("IRS form 433-b is known as __the Collection Information Statement for Business__,this is designed specifically for the IRS to gather business income and business expenses information from a business that is seeking a tax debt settlement. To know more visit https://www.myirstaxrelief.com/irs-433-form-help.html")
		elif item=="433-d":
			dispatcher.utter_message("IRS form 433-d is known as __the Direct Debit Installment Agreement for Individuals and Businesses__ it is in this form that all the details are finalized when the IRS has come to a settlement with an individual or business and the terms are spelled out. To know more visit https://www.myirstaxrelief.com/irs-433-form-help.html")
		elif item=="433-f":
			dispatcher.utter_message("IRS form 433-f is known as __the Collection Information Form__ and is a much more streamlined form than the 433-A. It is essentially used for the same purpose; resolving back tax problems, however, it is used primarily for those using the IRS automated collection service, ACS. To know more visit https://www.myirstaxrelief.com/irs-433-form-help.html")
		elif item=="941":
			dispatcher.utter_message("Under federal and state tax laws, a portion of employees' wages must be withheld and remitted to pay taxes. The federal tax withheld from employees' paychecks are known as the 941 payroll tax. As an employer, it's your responsibility to calculate the amount that each employee owes based on their withholding status, deduct the right amount with each paycheck and then remit the money to the federal government and state agencies. To know more visit https://www.myirstaxrelief.com/understanding-941-payroll-taxes-problems.html")
		elif item=="504":
			dispatcher.utter_message("The IRS or Internal Revenue Service has a singular purpose as part of the Federal Government, it is designed to collect and account for all of the tax dollars owed to the government. The IRS derives all of its power from the United States Tax Code and all actions that they take are done so using many different notices and forms. One of those forms is the CP 504 notice and it has to do with IRS Tax Levy. To know more visit https://blog.myirstaxrelief.com/cp-504-what-you-need-to-know-if-you-receive-one-in-the-mail/")
		elif item=="1040":
			dispatcher.utter_message("Form 1040 is used by U.S. taxpayers to file an annual income tax return. It should be filed by the deadline every year. Penalties and fees can be avoided by simply filling your tax returns, 1040, 1120, 1065, 941 by the deadline every year and pay as much as possible To know more visit https://www.myirstaxrelief.com/filing-back-taxes.html")
		elif item=="1120":
			dispatcher.utter_message("Form 1120 is used for U.S. Corporation Income Tax Return, to report the income, gains, losses, deductions, credits, and to figure the income tax liability of a corporation. To know more visit https://www.myirstaxrelief.com/filing-back-taxes.html")	
		else:
			dispatcher.utter_message("Hmm..I did not get that. Can you please try again? or it will be better if you visit our FAQs [here](https://www.myirstaxrelief.com/faqs.html) or you can reach us by visiting [here](https://www.myirstaxrelief.com/contact-us.html) ")
			


class ActionCheckItem(Action):
	def name(self):
		return "action_check_item"
		
	def run(self, dispatcher, tracker, domain):
		list_item = ["debt", "unfiled","audit", "employment","commission", "lien","fees","433","433-a","433-b","433-d","433-f","941","504","1040","1120"]
		
		
		item = tracker.get_slot('item')
		#dispatcher.utter_message(loc)
		if item is not None:
			if ((item.lower() in list_item)):
				return[SlotSet('item',item)]
			else:
				
				return[SlotSet('item',None)]
		else:
			
			return[SlotSet('item', None)]