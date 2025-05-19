import frappe
import requests

SOURCE_URL = "https://abna-alarabiya.com/api/resource/Customer"
SOURCE_HEADERS = {
    "Authorization": "token 1e2a66c44fc1b2f:3f2c048956dcdf3",
    "Content-Type": "application/json"
}

TARGET_API_KEY = "1d5f31413daeba8"
TARGET_API_SECRET = "b69aeef7a100353"

@frappe.whitelist()
def sync_customers():
    try:
        response = requests.get(SOURCE_URL, headers=SOURCE_HEADERS)
        customers = response.json().get("data", [])

        for customer in customers:
            create_or_update_customer(customer)
    
        return {"status": "Success", "message": f"{len(customers)} customers synced"}
    
    except Exception as e:
        frappe.log_error(f"Customer Sync Error: {str(e)}")
        return {"status": "Failed", "message": str(e)}

def create_or_update_customer(customer_data):
    existing_customer = frappe.get_all("Customer", filters={"name": customer_data["name"]})

    if existing_customer:
        frappe.db.set_value("Customer", customer_data["name"], customer_data)
    else:
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": customer_data["customer_name"],
            "customer_type": customer_data["customer_type"],
            "customer_group": customer_data["customer_group"],
            "territory": customer_data["territory"]
        })
        customer.insert(ignore_permissions=True)
