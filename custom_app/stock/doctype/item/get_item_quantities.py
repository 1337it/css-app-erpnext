import frappe
from frappe import _

@frappe.whitelist()
def get_item_quantities_for_companies():
    # Initialize a dictionary to hold company-wise item quantities
    company_item_quantities = {}

    # Fetch all the companies
    companies = frappe.get_all("Company", fields=["name"])

    # Loop through each company and fetch item quantities
    for company in companies:
        company_name = company.name
        
        # Get all items and their quantities in the company's warehouses
        items = frappe.get_all("Bin", filters={"company": company_name}, fields=["item_code", "actual_qty"])

        # Add items and their quantities to the company dictionary
        company_item_quantities[company_name] = []

        for item in items:
            company_item_quantities[company_name].append({
                "item_code": item.item_code,
                "actual_qty": item.actual_qty
            })

    return company_item_quantities
