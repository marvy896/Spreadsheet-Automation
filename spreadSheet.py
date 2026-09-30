import pandas as pd
from datetime import datetime

# ==========================================
# 1. OPEN THE SPREADSHEET
# ==========================================

input_file = "sales_data.xlsx"

df = pd.read_excel(input_file)

print("Original Data:")
print(df)


# ==========================================
# 2. SORT THE DATA
# ==========================================

df = df.sort_values(by="Amount", ascending=False)


# ==========================================
# 3. REMOVE DUPLICATES
# ==========================================

df = df.drop_duplicates()


# ==========================================
# 4. CALCULATE TOTALS
# ==========================================

total_sales = df["Amount"].sum()
number_of_transactions = len(df)

average_sale = df["Amount"].mean()


# ==========================================
# 5. PREPARE THE REPORT
# ==========================================

report = f"""
WEEKLY SALES REPORT
===================

Report Date: {datetime.now().strftime("%Y-%m-%d")}

Number of Transactions: {number_of_transactions}

Total Sales: ₦{total_sales:,.2f}

Average Sale: ₦{average_sale:,.2f}

===================
"""

print(report)


# ==========================================
# 6. SAVE CLEANED DATA + REPORT
# ==========================================

output_file = "weekly_sales_report.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # Cleaned and sorted data
    df.to_excel(
        writer,
        sheet_name="Cleaned Data",
        index=False
    )

    # Summary report
    summary = pd.DataFrame({
        "Metric": [
            "Number of Transactions",
            "Total Sales",
            "Average Sale"
        ],

        "Value": [
            number_of_transactions,
            total_sales,
            average_sale
        ]
    })

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )


print(f"Report saved as: {output_file}")