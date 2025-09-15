# fetchOut.py

## Overview
`fetchOut.py` is a Python script that connects to a Microsoft SQL Server database, executes the stored procedure `sp_x_out` (with optional `@CardNo` parameter), and exports the results into CSV, Excel (XLSX), or both formats. 

This is **v1.3.0**, the latest release.  

---

## Features
- Connects to SQL Server using pyodbc  
- Executes the stored procedure: `sp_x_out`  
- Supports optional parameter: `@CardNo`  
- Default CardNo to 0 if invalid input is provided
- Optional file_type parameter to export CSV, XLSX, or both
- Fetches all rows and columns returned by the stored procedure  
- Creates a `results/` folder automatically  
- Filenames include timestamp and CardNo (if provided)
- Exports results to:
  - If `@CardNo` provided:  
    - `results/results_<CardNo>_<timestamp>.csv`
    - `results/results_<CardNo>_<timestamp>.xlsx`
  - Otherwise:
    - `results/results_<timestamp>.csv`
    - `results/results_<timestamp>.xlsx`
- Uses .env file to store database credentials securely
- Startup validation for missing .env variables

---

## Requirements
- Python 3.8+  
- Dependencies:
  - pyodbc
  - pandas
  - openpyxl (for Excel export)
  - python-dotenv (for environment variables)

Install dependencies with:

```bash
pip install pyodbc pandas openpyxl python-dotenv
```

---

## Setup
1. Create a `.env` file in the same folder as `fetchOut.py`:
```
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=244.178.44.111
DB_DATABASE=Live
DB_UID=sa
DB_PWD=P@ssw0rd
DB_TIMEOUT=600
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
Without parameter (fetch all, both CSV & XLSX):
```
python fetchOut.py
```
With parameter (@CardNo, e.g., 12345) and default export (both):
```
python fetchOut.py 12345
```
Specify file type (c or csv = CSV, x or xlsx = XLSX, b or both = both):
```
python fetchOut.py 12345 c
python fetchOut.py 12345 x
python fetchOut.py 12345 b
```
4. Results will be saved in the `results/` folder with timestamped filenames.

---

## Versioning

### v1.3.0 (2025-09-15)
- Moved database credentials to .env file
- Added .gitignore to exclude .env from version control
- Added support for python-dotenv to load environment variables
- Added startup validation for missing .env variables
- Removed hardcoded credentials from code

### v1.2.0 (2025-09-02)
- Optional @CardNo parameter
- Optional file_type parameter for CSV/XLSX/both
- Default invalid CardNo to 0
- Results saved in results/ folder
- Timestamped filenames

### v1.1.0 (2025-09-02)
- Added support for optional `@CardNo` parameter
- Results saved in a dedicated `results/` folder
- Filenames now include `timestamps` and `CardNo` (if provided)

### v1.0.0 (2025-09-02)
- Initial version
- Executes `sp_x_out` without parameters
- Exports data to CSV and Excel

---

## Author
**Hamza**