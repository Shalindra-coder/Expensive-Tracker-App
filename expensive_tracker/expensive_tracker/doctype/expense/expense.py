# Copyright (c) 2024, shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class Expense(Document):
    def before_save(self):
        # Set default value for Main Select if not selected
        if not self.expense_category:  # Replace 'main_select_field' with your actual field name
            self.expense_category = 'General'
        
        # Generate a Reference Number if not already set
        if not self.refrence_number:  # Replace 'reference_number_field' with your actual field name
            self.refrence_number = self.generate_reference_number()

    def generate_reference_number(self):
        # Example logic to generate a random reference number
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return f"REF-{random_part}"
    
    def validate(self):
        if not self.amount:
            frappe.msgprint('please add positive number in amount ')
