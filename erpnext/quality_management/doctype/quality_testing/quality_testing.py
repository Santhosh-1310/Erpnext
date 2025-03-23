# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class QualityTesting(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		approved_by: DF.Data | None
		date: DF.Date | None
		drawing_number: DF.Data | None
		image: DF.AttachImage | None
		inspected_by: DF.Data | None
		item_description: DF.Data | None
		lf_view: DF.AttachImage | None
		product_code: DF.Data | None
		rh_view: DF.AttachImage | None
		top_view: DF.AttachImage | None
	# end: auto-generated types
	pass
