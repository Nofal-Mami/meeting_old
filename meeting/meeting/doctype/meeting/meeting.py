# -*- coding: utf-8 -*-
# Copyright (c) 2019, Mada and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		"""Set missing names and warn if duplicate"""
		found = []
		for v_attendee in self.attendees:
			if not v_attendee.full_name: #check if  full_name field is null proceed to fetch a value from user's doctype
				v_attendee.full_name = get_full_name(v_attendee.attendee)

			if v_attendee.attendee in found:
				frappe.throw(_("Attendee {0} entered twice").format(v_attendee.attendee))

			found.append(v_attendee.attendee)#remote wsl fixed

def get_full_name(attendee):
	user = frappe.get_doc("User",attendee)#user  is an object of type record

	#concatenate by space if it has a value
	user_f = [user.first_name, user.middle_name, user.last_name] #list definition
	return " ".join(user_f) #assign value to field full_name, join is a function to concatenate values from a list