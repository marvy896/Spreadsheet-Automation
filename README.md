📊 Spreadsheet Automation with Python

A simple Python automation project that demonstrates how repetitive data-processing tasks can be automated without performing them manually every week.

## 🤖 Automation vs AI

**Automation** follows predefined instructions to perform repetitive tasks.

For example:

> Open a spreadsheet → Sort the data → Remove duplicates → Calculate totals → Generate a report.

Python can automate all of these steps.

**AI is different.**

AI becomes particularly useful when information is unstructured or requires interpretation — such as emails, PDFs, handwritten information, or natural-language requests.

### Simple way to remember:

**Automation follows instructions.**
**AI helps interpret information.**

This project focuses on the **automation** side of that workflow.

---

## 🚀 What This Project Does

The script automatically:

* 📂 Opens an Excel spreadsheet
* 🔃 Sorts the data
* 🧹 Removes duplicate records
* 🧮 Calculates totals
* 📊 Generates a summary report
* 💾 Saves the processed data into a new Excel workbook

Instead of manually performing these tasks every Monday, Python can handle them automatically.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **OpenPyXL**
* **Microsoft Excel**

---

## 📁 Project Structure

```text
spreadsheet-automation/
│
├── sales_data.xlsx
├── automation.py
├── weekly_sales_report.xlsx
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/spreadsheet-automation.git
```

Move into the project directory:

```bash
cd spreadsheet-automation
```

Install the required libraries:

```bash
pip install pandas openpyxl
```

---

## ▶️ How to Run

Place your Excel file in the project folder and name it:

```text
sales_data.xlsx
```

Then run:

```bash
python automation.py
```

The script will process the spreadsheet and create:

```text
weekly_sales_report.xlsx
```

---

## 📋 Example Input

The input spreadsheet can contain data such as:

| Date       | Customer | Product | Amount |
| ---------- | -------- | ------- | -----: |
| 2026-09-01 | John     | Laptop  | 500000 |
| 2026-09-02 | Mary     | Phone   | 250000 |
| 2026-09-03 | John     | Laptop  | 500000 |
| 2026-09-04 | Peter    | Monitor | 150000 |

The duplicate record can automatically be removed, and the remaining data can be sorted and summarized.

---

## 📊 Output

The generated workbook contains:

### Cleaned Data

The processed and sorted spreadsheet with duplicate records removed.

### Summary

A simple report containing:

* Number of transactions
* Total sales
* Average sale

---

## 🔄 The Automation Workflow

```text
Excel Spreadsheet
       ↓
   Read Data
       ↓
   Sort Data
       ↓
Remove Duplicates
       ↓
 Calculate Totals
       ↓
 Generate Report
       ↓
 Save Excel File
```

---

## 💡 Why Automation Matters

Imagine performing the same six steps every Monday.

Doing it manually might take several minutes or even hours.

With automation, you can turn the process into:

```text
Run Script
    ↓
Get Results
```

The goal isn't simply to write Python code.

The goal is to **eliminate repetitive work and improve productivity.**

---

## 🤖 Future AI Integration

This project can be extended into an **AI-powered automation workflow**.

Instead of only processing structured Excel data, AI could help interpret:

* 📧 Emails
* 📄 PDF documents
* 📝 Natural-language requests
* ✍️ Poorly formatted information
* 🖼️ Scanned documents

The workflow could become:

```text
Email / PDF / Document
          ↓
       AI
          ↓
Interpret Information
          ↓
Structured Data
          ↓
      Python
          ↓
Automation
          ↓
Report
          ↓
Email
```

This demonstrates an important distinction:

> **Automation performs predefined tasks. AI helps interpret information and handle less-structured inputs.**

---

## 🎯 Project Goal

The purpose of this project is to demonstrate how Python can be used for **practical workplace automation**, especially for repetitive administrative and data-processing tasks.

---

## 👨‍💻 Author

**Marvel Kene**

AI & Practical Tech Productivity
Python | AI Automation | Technology

---

## 📌 Future Improvements

* [ ] Automatically read emails
* [ ] Extract data from PDFs
* [ ] Add AI-powered document interpretation
* [ ] Generate PDF reports
* [ ] Send reports automatically by email
* [ ] Schedule the script to run every Monday
* [ ] Build a simple dashboard
* [ ] Add error logging and notifications

---

⭐ If you find this project useful, consider starring the repository.
