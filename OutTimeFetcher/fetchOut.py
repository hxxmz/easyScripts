"""
============================================================
 Script Name : fetchOut.py
 Version     : v1.1.0
 Last Update : 2025-09-02
 Author      : Hamza

 Change Log:
 - v1.2.0 (2025-09-02):
   • Added optional @CardNo parameter.
   • Added file_type option to export CSV, XLSX, or both.
   • Default CardNo to 0 if invalid input.
   • Results stored in 'results/' folder.
   • Filenames include timestamp and CardNo (if provided).

 - v1.1.0 (2025-09-02):
   • Added optional @CardNo parameter support.
   • Auto-creates a 'results' folder for exports.
   • Output files now include timestamp and card number (if provided).
   • Improved export filenames for uniqueness.

 - v1.0.0 (2025-09-02):
   • Initial version: run sp_x_out without any parameter.
   • Basic CSV/XLSX export without parameter handling.
============================================================
"""
import sys
import os
import pyodbc
import pandas as pd
from datetime import datetime

def run_stored_proc(card_no=None, file_type="both"):
    # Connection string
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=244.178.44.111;"
        "Database=Live;"
        "UID=sa;"
        "PWD=P@ssw0rd;"
        "Connect Timeout=600;"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        if card_no:
            if not str(card_no).isdigit():
                print(f"⚠ Invalid CardNo '{card_no}', defaulting to 0")
                card_no = 0

            print(f"▶ Running: EXEC sp_x_out @CardNo = {card_no}")
            cursor.execute("EXEC sp_x_out @CardNo = ?", (card_no,))
        else:
            print("▶ Running: EXEC sp_x_out")
            cursor.execute("EXEC sp_x_out")

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame.from_records(rows, columns=columns)

        # Ensure results folder exists
        results_dir = "results"
        os.makedirs(results_dir, exist_ok=True)

        # Build filename with datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if card_no:
            base_name = f"results_{card_no}_{timestamp}"
        else:
            base_name = f"results_{timestamp}"

        # Export according to file_type
        if file_type.lower() in ("c", "csv", "both", "b"):
            csv_file = os.path.join(results_dir, base_name + ".csv")
            df.to_csv(csv_file, index=False)
            print(f"✅ CSV exported: {csv_file}")

        if file_type.lower() in ("x", "xlsx", "both", "b"):
            xlsx_file = os.path.join(results_dir, base_name + ".xlsx")
            df.to_excel(xlsx_file, index=False)
            print(f"✅ Excel exported: {xlsx_file}")

        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    card_no = None
    file_type = "both"

    if len(sys.argv) > 1:
        if sys.argv[1].strip() != "":
            card_no = sys.argv[1]
    if len(sys.argv) > 2:
        file_type = sys.argv[2]

    run_stored_proc(card_no, file_type)
