"""
============================================================
 Script Name : fetchOut.py
 Version     : v1.0.0
 Last Update : 2025-09-02
 Author      : Hamza

 Change Log:
 - v1.0.0 (2025-09-02):
   • Initial version: run sp_x_out without any parameter.
   • Basic CSV/XLSX export without parameter handling.
============================================================
"""
import pyodbc
import pandas as pd

def run_stored_proc():
    # Connection string for your Live DB
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=244.178.44.111;"
        "Database=Live;"
        "UID=sa;"
        "PWD=P@ssw0rd;"
        "Connect Timeout=600;"
    )

    try:
        # Connect to SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Execute your stored procedure
        cursor.execute("EXEC sp_x_out")

        # Fetch all rows and column names
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        # Convert to pandas DataFrame
        df = pd.DataFrame.from_records(rows, columns=columns)

        # Save to CSV
        df.to_csv("sp_x_out_results.csv", index=False)

        # Save to Excel
        df.to_excel("sp_x_out_results.xlsx", index=False)

        print("✅ Data exported to:")
        print("   - sp_x_out_results.csv")
        print("   - sp_x_out_results.xlsx")

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    run_stored_proc()
