"""
============================================================
 Script Name : fetchOut.py
 Version     : v1.3.0
 Last Update : 2025-09-15
 Author      : Hamza

 Change Log:
 - v1.3.0 (2025-09-15):
   • Moved database credentials to a .env file.
   • Added .gitignore to exclude .env from version control.
   • Added support for loading environment variables using python-dotenv.
   • Added startup check for missing .env variables.
   • Removed hardcoded credentials from code for security.

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
from dotenv import load_dotenv

def init_env():
    # Load environment variables from .env file
    print("🔧 Loading environment variables from .env...") # cmtspm
    load_dotenv()

    # ✅ Validate required variables exist
    print("🔍 Validating environment variables...") # cmtspm
    if not all([os.getenv("DB_SERVER"), os.getenv("DB_DATABASE"),
                os.getenv("DB_UID"), os.getenv("DB_PWD")]):
        print("❌ Missing one or more DB environment variables in .env file.")
        print("🚪 Exiting...")
        sys.exit(1)
    
    print("✅ Environment variables loaded successfully.") # cmtspm

def run_stored_proc(card_no=None, file_type="both"):

    # Connection string
    conn_str = (
        f"Driver={{{os.getenv('DB_DRIVER')}}};"
        f"Server={os.getenv('DB_SERVER')};"
        f"Database={os.getenv('DB_DATABASE')};"
        f"UID={os.getenv('DB_UID')};"
        f"PWD={os.getenv('DB_PWD')};"
        f"Connect Timeout={os.getenv('DB_TIMEOUT', '600')};"
    )

    try:
        print("🔗 Connecting to database...") # cmtspm
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

        print("📥 Fetching results...") # cmtspm
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame.from_records(rows, columns=columns)

        # Ensure results folder exists
        print("📁 Ensuring results folder exists...") # cmtspm
        results_dir = "results"
        os.makedirs(results_dir, exist_ok=True)

        # Build filename with datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print("💾 Exporting results...") # cmtspm
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

        print("🔒 Closing connection...") # cmtspm
        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    init_env()

    card_no = None
    file_type = "x"

    if len(sys.argv) > 1:
        if sys.argv[1].strip() != "":
            card_no = sys.argv[1]
    if len(sys.argv) > 2:
        file_type = sys.argv[2]

    run_stored_proc(card_no, file_type)

    # ✅ Pause to keep console open until user presses Enter
    input("\nPress Enter to exit...")
