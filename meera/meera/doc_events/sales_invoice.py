import frappe
from frappe import _

def before_naming(self, method):
	if not self.name and not self.amended_from:
		if self.naming_series.find('#') and self.naming_series[-1] != '#':
			from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
			SalesInvoice.autoname = autoname


def autoname(self):
	if not self.name:
		if self.invoice_no:
			self.name = self.invoice_no
		elif self.naming_series.find('#') and self.naming_series[-1] != '#':
			from erpnext.accounts.utils import get_fiscal_year

			date = self.get("transaction_date") or self.get("posting_date") or getdate()

			fy = get_fiscal_year(date)[0]
			fiscal = frappe.db.get_value("Fiscal Year", fy, 'fiscal')

			if fiscal:
				self.fiscal = fiscal
			else:
				fy_years = fy.split("-")
				fiscal = fy_years[0][2:] + fy_years[1][2:]
				self.fiscal = fiscal

			naming_series = self.naming_series.replace('#', '').replace('.', '').replace('company_series', (self.company_series or '')).replace('fiscal', self.fiscal)

			check = frappe.db.get_value('Series', naming_series, 'current', order_by="name")
			if check == 0 or check:
				value = check + 1
				frappe.db.sql(f"update `tabSeries` set current = {check + 1} where name = '{naming_series}'")
			elif not check:
				value = 1
				frappe.db.sql(f"insert into tabSeries (name, current) values ('{naming_series}', 1)")
			
			naming_series = self.naming_series.replace('.', '').replace('company_series', (self.company_series or '')).replace('fiscal', self.fiscal)

			cnt = 0
			for i in self.naming_series:
				if cnt == 0:
					if i == '#':
						cnt += 1
				else:
					if i == '#':
						cnt += 1
					else:
						break
			
			hashed = '#' * cnt

			self.name = self.naming_series.replace('.', '').replace(hashed, f'{str(value).zfill(cnt)}').replace('company_series', (self.company_series or '')).replace('fiscal', self.fiscal)