# Copyright (c) 2024, shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class Expense(Document):
    def before_insert(self):
        if not self.expense_category:
            self.expense_category = 'General'
        
    
        if not self.refrence_number:  
            self.refrence_number = self.generate_reference_number()

    def generate_reference_number(self):
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return f"REF-{random_part}"
    
    def before_save(self):
        if self.amount<=0:
            frappe.throw("please add positive amount Thank You!")

    

        
