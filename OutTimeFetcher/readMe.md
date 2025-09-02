# fetchOut.py

## Overview
`fetchOut.py` is a Python script that connects to a Microsoft SQL Server database, executes the stored procedure `sp_x_out`, and exports the results into both CSV and Excel (XLSX) formats.

This is **v1.0.0**, the initial release.

---

## Features
- Connects to SQL Server using pyodbc
- Executes the stored procedure: `sp_x_out`
- Fetches all rows and columns returned by the stored procedure
- Exports results to:
  - `sp_x_out_results.csv`
  - `sp_x_out_results.xlsx`

---

## Requirements
- Python 3.8+  
- Dependencies:
  - pyodbc
  - pandas
  - openpyxl (for Excel export)

Install dependencies with:
```
pip install pyodbc pandas openpyxl
```

---

## Usage
1. Clone or copy the script to your local machine.  
2. Update the connection string inside the script if needed:
```
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=244.178.44.111;"
    "Database=Live;"
    "UID=sa;"
    "PWD=P@ssw0rd;"
    "Connect Timeout=600;"
)
```
3. Run the script:
```
python fetchOut.py
```
4. Results will be saved in the same folder as:
   - `sp_x_out_results.csv`
   - `sp_x_out_results.xlsx`

---

## Versioning

### v1.0.0 (2025-09-02)
- Initial version
- Executes `sp_x_out` without parameters
- Exports data to CSV and Excel

---

## Author
**Hamza**