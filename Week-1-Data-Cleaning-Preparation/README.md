<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0B3D91&height=220&section=header&text=Week%201%20-%20Data%20Cleaning&fontSize=42&fontColor=ffffff&animation=fadeIn"/>
</p>

<h2 align="center">🧹 Cleaning Raw Data for Reliable Analysis</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Week-1-0A66C2?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Internship-Decode%20Labs-1E88E5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-Pandas-3776AB?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>
</p>

---

# 📌 Overview

This project was completed as **Week 1** of my **Data Analytics Internship at Decode Labs**.

The objective was to clean a raw e-commerce dataset and prepare it for future analysis by improving data quality and ensuring consistency across all records.

---

# 🎯 Internship Task

### Goal

Clean a raw dataset by:

- Handling missing values
- Identifying duplicate records
- Correcting incorrect data formats

---

# 📂 Dataset Information

| Attribute | Value |
|-----------|------:|
| Dataset Type | E-Commerce Sales |
| Total Rows | 1,200 |
| Total Columns | 14 |

---

# 🔍 Data Quality Assessment

Before cleaning, the dataset was inspected for:

- Missing values
- Duplicate records
- Incorrect data types
- Data consistency
- Dataset structure

### Initial Findings

| Issue | Result |
|--------|--------|
| Missing Values | CouponCode column |
| Duplicate Rows | None |
| Incorrect Date Format | Date stored as text |

---

# 🛠 Cleaning Process

### ✔ Missing Values

- Identified missing values using Pandas
- Missing values were found only in the **CouponCode** column
- Replaced missing coupon values with **"No Coupon"**

---

### ✔ Duplicate Records

- Checked the entire dataset for duplicate rows
- Verified that no duplicate records existed

---

### ✔ Data Type Correction

Converted:

- Date → DateTime format

Verified:

- Numeric columns
- Text columns

---

### ✔ Data Validation

Validated:

- Unique Order IDs
- Numeric values
- Data consistency
- Dataset integrity

---

# 📊 Final Result

After cleaning, the dataset became suitable for future analysis.

| Validation | Status |
|-----------|:------:|
| Missing Values Removed | ✅ |
| Duplicate Records | ✅ |
| Correct Data Types | ✅ |
| Clean Dataset | ✅ |

---

# 🛠 Technologies Used

- Python
- Pandas
- Jupyter Notebook

---

# 📁 Project Structure

```text
Week-1-Data-Cleaning/
│
├── Data/
│   ├── cleaned_dataset.csv
│   └── Dataset for Data Analytics - Sheet1.csv
│
├── notebook/
│   └── analysis.ipynb
│
├── Project_Instructions.pdf
│
└── README.md
```

---

# 💡 Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Missing Value Handling
- Duplicate Detection
- Data Validation
- Data Type Conversion
- Pandas
- Python

---

# 🎓 Learning Outcomes

Through this task, I strengthened my understanding of:

- Real-world data cleaning workflows
- Data quality assessment
- Preparing datasets for analysis
- Writing clean and organized Python code

---

<p align="center">
Completed as part of the <strong>Decode Labs Data Analytics Internship</strong>.
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0B3D91&height=120&section=footer"/>
</p>