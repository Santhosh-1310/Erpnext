from frappe.desk.form.assign_to import add as original_add
import frappe

def custom_assign_to_add(args=None):
    # Call the original assign_to.add function
    response = original_add(args)

    # Fetch the document related to the assignment
    doc = frappe.get_doc(args.get("doctype"), args.get("name"))

    # Call your custom server script logic
    assign_user_permission(doc, "assign_to")  # Replace 'assign_to' with the appropriate method

    return response

def assign_user_permission(doc, method):
    # Your server script logic here
    if not doc.assigned_to:
        return

    # Ensure User Permission is created
    existing_permission = frappe.db.exists(
        'User Permission',
        {
            'user': doc.assigned_to,
            'allow': 'Issue',
            'for_value': doc.name
        }
    )
    if not existing_permission:
        user_permission = frappe.get_doc({
            'doctype': 'User Permission',
            'user': doc.assigned_to,
            'allow': 'Issue',
            'for_value': doc.name,
            'apply_for_all_roles': 0
        })
        user_permission.insert(ignore_permissions=True)
        frappe.msgprint(f"User Permission created for {doc.assigned_to} on Issue {doc.name}")
