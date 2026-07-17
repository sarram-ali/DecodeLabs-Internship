import pandas as pd
import mysql.connector

# Read Excel
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Replace NaN with None
df = df.where(pd.notnull(df), None)

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1s2a3r4r5a6m",
    database="decode_labs_week_3"
)

cursor = conn.cursor()

# Clean column names
df.columns = [col.replace(" ", "_") for col in df.columns]

# Create Table
create_table = """
CREATE TABLE IF NOT EXISTS sales(

OrderID VARCHAR(20),
Date DATE,
CustomerID VARCHAR(20),
Product VARCHAR(50),
Quantity INT,
UnitPrice FLOAT,
ShippingAddress VARCHAR(100),
PaymentMethod VARCHAR(50),
OrderStatus VARCHAR(50),
TrackingNumber VARCHAR(30),
ItemsInCart INT,
CouponCode VARCHAR(30),
ReferralSource VARCHAR(30),
TotalPrice FLOAT

)
"""

cursor.execute(create_table)

# Insert Query
insert_query = """
INSERT INTO sales_data
(OrderID,Date,CustomerID,Product,Quantity,UnitPrice,
ShippingAddress,PaymentMethod,OrderStatus,
TrackingNumber,ItemsInCart,CouponCode,
ReferralSource,TotalPrice)

VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

# Insert Data
for row in df.itertuples(index=False):

    values = tuple(None if pd.isna(x) else x for x in row)

    cursor.execute(insert_query, values)

conn.commit()

print("Data Imported Successfully!")

cursor.close()
conn.close()