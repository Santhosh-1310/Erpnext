import frappe

@frappe.whitelist(allow_guest=True)
def create_lead(lead_name, lead_email, company_name, lead_mobile, lead_gender):
    try:
        # Validate inputs
        if not lead_name or not lead_email or not company_name:
            return {'status': 'error', 'message': 'All fields are required.'}

        # Create Lead document
        lead = frappe.get_doc({
            'doctype': 'Lead',
            'first_name': lead_name,        # Mapping to 'first_name' field
            'email_id': lead_email,         # Mapping to 'email_id' field (from 'status' input)
            'company_name': company_name,
            'mobile_no': lead_mobile,
            'gender': lead_gender
        })

        lead.insert(ignore_permissions=True)
        frappe.db.commit()

        return {'status': 'success', 'message': 'Lead created successfully'}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Create Lead Error")
        return {'status': 'error', 'message': f'Error occurred: {str(e)}'}

@frappe.whitelist(allow_guest=True)
def create_lead_api():
    # Extract data from the form submission
    lead_name = frappe.form_dict.get("first_name")  # Corresponds to the 'first_name' input in the form
    lead_email = frappe.form_dict.get("lead_email")     # Corresponds to the 'status' input in the form (mapped to email)
    company_name = frappe.form_dict.get("company_name")  # Corresponds to 'company_name' input

    # Call the create_lead function to create the lead in ERPNext
    return create_lead(lead_name, lead_email, company_name)

@frappe.whitelist(allow_guest=True)
def create_lead_notification(doc, method):
    """This function will be triggered after a Lead document is inserted."""
    frappe.msgprint(f"New Lead created: {doc.first_name} ({doc.email_id})")
