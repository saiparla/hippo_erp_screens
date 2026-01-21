
import frappe
import json

@frappe.whitelist(allow_guest=True)
def create_student_registration():
    # Parse the JSON payload
    data = frappe.local.request.get_data(as_text=True)
    data = json.loads(data)

    # Create the document for registration
    doc = frappe.get_doc({
        "doctype": "Hippo Student Registration",
        "full_name": data.get("fullName"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "gender": data.get("gender"),
        "course": data.get("course"),
        "sub_course": data.get("subCourse"),
        "qualification": data.get("qualification"),
        "college": data.get("college"),
        "batch": data.get("batch"),
        "source": data.get("source"),
        "mode": data.get("mode"),
        "comments": data.get("comments")
    })

    # Insert while ignoring uniqueness checks and permissions
    # This will prevent 409 CONFLICT for duplicates
    doc.insert(ignore_permissions=True, ignore_mandatory=True, ignore_if_duplicate=True)

    frappe.db.commit()

    return {"message": "Registration Successful 🎉"}


@frappe.whitelist(allow_guest=True)
def get_all_sub_courses():
    """
    Returns all sub-courses, duplicates included
    """
    return frappe.get_all(
        "Sub Course",
        fields=["course", "sub_course"],
        order_by="sub_course"
    )

@frappe.whitelist(allow_guest=True)
def get_all_courses():
    """
    Returns all courses, duplicates included
    """
    return frappe.get_all(
        "Course",
        fields=["course"],
        order_by="course"
    )
