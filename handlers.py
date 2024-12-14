def set_default_category(doc, method):
    # Check if category is not selected
       if not doc.expense_category:
        doc.expense_category = "General"  # Set default category as "General"
