# hr_eos_saudi

## End of Service – Odoo 17

### Overview
Module **hr_eos_saudi** is developed on **Odoo 17** to calculate **End of Service** according to **Saudi Labor Law (Article 84)**.

---

### Calculation Logic
- End of Service is calculated **once only** when employee End of Service is approved.
- Calculation is based on **Last Contract Wage**.
- Service period is calculated from:
  - **First Contract Date**
  - **End of Work Permit Date**

#### Rule:
- **First 5 years** → Half salary for each year  
- **After 5 years** → Full salary for each year  
- Partial years are calculated proportionally.

---

### Payroll Integration
- Adds **Salary Rule** for End of Service.
- Adds **Payroll Statement** view showing:
  - Employee
  - Joining Date
  - End of Work Permit Date
  - Service Days
  - End of Service Amount
- Fully linked with **Payslip**.

---

### Reports
- **Pivot Report** for End of Service per employee and total amount.
- Export available to **Excel**.

---

### Compatibility
- Odoo 17
- Saudi Labor Law compliant
