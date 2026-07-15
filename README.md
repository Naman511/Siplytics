# Siplytics

**Project Objective:**
This project provides a comprehensive data pipeline and analytical dashboard designed to evaluate vendor performance. By integrating sales, purchase, and freight data, Siplytics offers data-driven insights into vendor efficiency, profitability, and their contribution to overall business growth.

---

## PowerBI Dashboard
<img width="1223" height="748" alt="Screenshot 2026-07-15 063012" src="https://github.com/user-attachments/assets/29f2eb2b-20a4-4429-9497-def4edf90529" />


---

## Project Overview
The project architecture involves:
*   **Data Ingestion:** A robust Python pipeline utilizes `pandas` and `SQLAlchemy` to ingest CSV data into an `inventory.db` SQLite database[cite: 2].
*   **Data Processing:** Python scripts clean and transform the data, calculating metrics such as **Gross Profit**, **Profit Margin**, **Stock Turnover**, and **Sales-to-Purchase Ratios**[cite: 2].
*   **Exploratory Data Analysis (EDA):** Statistical analysis was performed to identify inventory inefficiencies, such as products purchased but never sold, and to validate the profitability models of different vendor groups[cite: 2, 3].

## Key Insights
*   **Vendor Reliance:** The top 10 vendors account for 65.69% of total purchases, highlighting a potential supply chain risk[cite: 3].
*   **Bulk Purchasing:** Large-scale orders resulted in a 72% lower unit cost compared to smaller order sizes, validating the strategy of bulk procurement[cite: 3].
*   **Inventory Efficiency:** High-margin brands with low sales volume were identified as prime candidates for targeted marketing and pricing optimization[cite: 3].
*   **Logistics:** High variations in freight costs across vendors suggest a need for further optimization of logistics and shipping agreements[cite: 3].

## Technical Stack
*   **Language:** Python 3.13[cite: 2]
*   **Database:** SQLite[cite: 2]
*   **Libraries:** `pandas`, `SQLAlchemy`, `seaborn`, `matplotlib`, `scipy`[cite: 2, 4]
*   **Environment:** Jupyter Notebooks for analysis and ETL logic[cite: 2]

## Project Structure
```text
├── data/                               # Raw CSV data files
├── logs/                               # Ingestion and processing logs
│   └── ingestion_db.log
├── Ingestion and EDA.ipynb             # Notebook for data ingestion and exploratory analysis
├── ingestion_db.py                     # Python script to load CSVs into the SQLite database
├── inventory.db                        # SQLite database
├── Siplytics_project_report.pdf        # Comprehensive project report
├── Vendor Performance Analysis.ipynb   # Main notebook for vendor performance and statistical analysis
└── README.md                           # This file
