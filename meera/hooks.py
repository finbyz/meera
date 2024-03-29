# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "meera"
app_title = "Meera"
app_publisher = "FinByz"
app_description = "Meera"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@finbyz.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meera/css/meera.css"
# app_include_js = "/assets/meera/js/meera.js"

# include js, css files in header of web template
# web_include_css = "/assets/meera/css/meera.css"
# web_include_js = "/assets/meera/js/meera.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "meera.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "meera.install.before_install"
# after_install = "meera.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meera.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doctype_js = {
	"Sales Order": "public/js/doctype_js/sales_order.js"
}

doc_events = {
	"Sales Invoice": {
		"before_naming": "meera.meera.doc_events.sales_invoice.before_naming"
	},
	"Sales Order": {
		"before_naming": "meera.api.before_naming"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"meera.tasks.all"
# 	],
# 	"daily": [
# 		"meera.tasks.daily"
# 	],
# 	"hourly": [
# 		"meera.tasks.hourly"
# 	],
# 	"weekly": [
# 		"meera.tasks.weekly"
# 	]
# 	"monthly": [
# 		"meera.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "meera.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "meera.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "meera.task.get_dashboard_data"
# }

# e invoice override
import erpnext

from meera.e_invoice_override import update_invoice_taxes, get_invoice_value_details, make_einvoice
erpnext.regional.india.e_invoice.utils.update_invoice_taxes = update_invoice_taxes
erpnext.regional.india.e_invoice.utils.get_invoice_value_details = get_invoice_value_details
erpnext.regional.india.e_invoice.utils.make_einvoice = make_einvoice
