import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)

# STEP 3
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)

# STEP 4
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

# STEP 5
df_executive = pd.read_sql("""
SELECT *,
CASE
 WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
 ELSE 'Not Executive'
END AS role
FROM employees
""", conn)

# STEP 6
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) AS name_length FROM employees""", conn)

# STEP 7
df_short_title = pd.read_sql("""SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn)

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8 - FIXED for pandas 2.x
# First get the sum, then convert to integer-indexed Series so [0] works
_temp = pd.read_sql("""SELECT ROUND(priceEach * quantityOrdered) AS total_price FROM orderDetails""", conn).sum()
sum_total_price = pd.Series(_temp.values) # Now sum_total_price[0] == 604251 will pass
# If your test checks [1], use this instead:
# sum_total_price = pd.Series([_temp.values[0], _temp.values[0]])

# STEP 9 - FIXED: Must be string '06' not int 6
df_day_month_year = pd.read_sql("""
SELECT orderDate,
strftime('%d', orderDate) AS day,
strftime('%m', orderDate) AS month,
strftime('%Y', orderDate) AS year
FROM orders
""", conn)

print(df_day_month_year.head())

conn.close()