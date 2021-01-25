from __future__ import unicode_literals
import frappe
from erpnext.accounts.utils import get_fiscal_year
import datetime
from frappe.utils import cint, getdate

def before_naming(self, method):
	if not self.get('amended_from') and not self.get('name'):
		date = self.get("transaction_date") or self.get("posting_date") or  self.get("manufacturing_date") or  self.get("date") or getdate()

		fiscal = get_fiscal(date)
		self.fiscal = fiscal
		
		month = datetime.datetime.strptime(date,'%Y-%m-%d').date().strftime('%B').upper()
		
		self.month = month

		if not self.get('company_series'):
			self.company_series = None
		if self.get('series_value'):
			if self.series_value > 0:
				name = naming_series_name(self.naming_series, fiscal, self.company_series, self.month)
				check = frappe.db.get_value('Series', name, 'current', order_by="name")
				#frappe.msgprint(str(check))
				if check == 0:
					pass
				elif not check:
					
					frappe.db.sql("insert into tabSeries (name, current) values ('{}', 0)".format(name))

				frappe.db.sql("update `tabSeries` set current = {} where name = '{}'".format(cint(self.series_value) - 1, name))

def naming_series_name(name, fiscal, company_series=None, month=None):
	if company_series:
		name = name.replace('company_series', str(company_series))
	if month:
		name = name.replace('month', str(month))

	name = name.replace('YYYY', str(datetime.date.today().year))
	name = name.replace('YY', str(datetime.date.today().year)[2:])
	name = name.replace('MM', '{0:0=2d}'.format(datetime.date.today().month))
	name = name.replace('DD', '{0:0=2d}'.format(datetime.date.today().day))
	name = name.replace('fiscal', str(fiscal))
	name = name.replace('#', '')
	name = name.replace('.', '')
	return name

@frappe.whitelist()
def check_counter_series(name, company_series = None, date = None, month=None):
	if not date:
		date = datetime.date.today()
	

	month = datetime.datetime.strptime(date,'%Y-%m-%d').date().strftime('%B').upper()

	fiscal = get_fiscal(date)
	
	name = naming_series_name(name, fiscal, company_series, month)
	
	check = frappe.db.get_value('Series', name, 'current', order_by="name")
	
	if check == 0:
		return 1
	elif check == None:
		frappe.db.sql("insert into tabSeries (name, current) values ('{}', 0)".format(name))
		return 1
	else:
		return int(frappe.db.get_value('Series', name, 'current', order_by="name")) + 1

def get_fiscal(date):
	fy = get_fiscal_year(date)[0]
	fiscal = frappe.db.get_value("Fiscal Year", fy, 'fiscal')

	return fiscal if fiscal else fy.split("-")[0][2:] + fy.split("-")[1][2:]