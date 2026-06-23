# Financial Market Data Warehouse Pipeline

An enterprise-grade, object-oriented ETL (Extract, Transform, Load) data pipeline that programmatically extracts live financial market metrics, applies analytical data cleaning, and streams deduplicated datasets into a containerized Microsoft SQL Server Data Warehouse.

This system is built using defensive validation principles, automated logging patterns, and professional environment decoupling to ensure robust, production-ready execution.

## 🏗️ System Architecture

The pipeline is engineered using clean Object-Oriented Programming (OOP) paradigms, strictly isolating system responsibilities into dedicated operational modules:

1. **`APIClient` (Extraction):** Manages secure HTTP networking routines, utilizing browser spoofing headers to pull raw JSON time-series market payloads from financial endpoints.
2. **`DataTransformer` (Transformation):** Leverages `pandas` to parse deep nested JSON structures, enforce high-precision mathematical data scales, clean date fields, and handle intraday data-grain deduplication.
3. **`DatabaseManager` (Loading & Auditing):** Coordinates system infrastructure handshakes via `SQLAlchemy` ORM and native `unixODBC` drivers to manage data streams and record transactional runtime metadata.

---

## ⚙️ Core Technical Features

* **Intraday Grain Resolution:** Automatically drop-duplicates dense time-series payloads to conform cleanly to daily snapshot data warehouse constraints without database primary key conflicts.
* **Defensive Pipeline Validation:** Employs early input testing; validating API data payloads before initiating any long-term database transactions to prevent stale, corrupted, or lingering `RUNNING` status blocks in audit logs.
* **Transactional Auditing:** Writes infrastructure-level logs (`PipelineLog`) capturing precise execution tracking states (`RUNNING`, `SUCCESS`, `FAILED`), ingestion volumes, and Python error tracebacks.

---

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.12+
* **Data Manipulation:** `pandas`
* **Database Engine & ORM:** Microsoft SQL Server 2022 (Dockerized), `SQLAlchemy`, `pyodbc`
* **Host Operating System Environment:** Linux (Ubuntu/Pop!_OS)
* **Native OS Dependencies:** `unixodbc`, `unixodbc-dev`, `msodbcsql18` (Microsoft ODBC Driver 18 for SQL Server)

---

## 🚀 Local Installation & Execution Guide

### 1. Initialize the Container Database
Ensure your local Docker container hosting Microsoft SQL Server is spun up and running smoothly:
```bash
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=YourStrongPassword" \
   -p 1433:1433 --name market-sql-server \
   -d [mcr.microsoft.com/mssql/server:2022-latest](https://mcr.microsoft.com/mssql/server:2022-latest)