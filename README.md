# Siplytics

**Vendor Performance Analytics & Invoice Intelligence Platform**

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-003b57.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Library-f7931e.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-ff4b4b.svg)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-f2c811.svg)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen.svg)

---

## Project Objective

Siplytics is an end-to-end vendor intelligence platform. It combines a **data pipeline and Power BI dashboard** for evaluating vendor performance with a **machine learning system** that predicts freight costs and flags risky invoices — giving both a strategic (vendor-level) and an operational (invoice-level) view of the same purchasing data.

The repository has two components:

| Component | What it answers | Folder |
|---|---|---|
| **Vendor Performance Analytics** | "Which vendors and brands are driving (or hurting) the business?" | repo root |
| **Invoice Intelligence System** | "Is this specific invoice priced and paid correctly?" | `Invoice_Intelligence_System/` |

---

## Part 1 — Vendor Performance Analytics

### Power BI Dashboard

<img width="1223" height="748" alt="Siplytics Power BI Dashboard" src="https://github.com/user-attachments/assets/29f2eb2b-20a4-4429-9497-def4edf90529" />

### Overview

- **Data Ingestion** — A Python pipeline built on `pandas` and `SQLAlchemy` ingests raw CSV data into an `inventory.db` SQLite database.
- **Data Processing** — Scripts clean and transform the data, calculating **Gross Profit**, **Profit Margin**, **Stock Turnover**, and **Sales-to-Purchase Ratios**.
- **Exploratory Data Analysis** — Statistical analysis identifies inventory inefficiencies (e.g. products purchased but never sold) and validates profitability models across vendor groups.

### Key Insights

| Insight | Detail |
|---|---|
| **Vendor Reliance** | The top 10 vendors account for **65.69%** of total purchases, highlighting a potential supply chain concentration risk. |
| **Bulk Purchasing** | Large-scale orders resulted in a **72% lower** unit cost compared to smaller order sizes, validating the bulk-procurement strategy. |
| **Inventory Efficiency** | High-margin brands with low sales volume were identified as prime candidates for targeted marketing and pricing optimization. |
| **Logistics** | High variation in freight costs across vendors points to an opportunity to optimize logistics and shipping agreements. |

### Technical Stack

| Component | Technology |
|---|---|
| Language | Python 3.13 |
| Database | SQLite |
| Libraries | `pandas`, `SQLAlchemy`, `seaborn`, `matplotlib`, `scipy` |
| Environment | Jupyter Notebooks |
| Visualization | Power BI |

---

## Part 2 — Invoice Intelligence System

📊 **AI-Driven Freight Cost Prediction & Invoice Risk Flagging**

Where Part 1 looks at vendor performance in aggregate, this module works at the individual invoice level — it's a Streamlit application backed by two supervised ML models trained on the same purchase/vendor-invoice data.

### Module 1 — Freight Cost Prediction

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/3eacbf30-57a7-4e4a-a2a0-e5a0481a1113" />


| | |
|---|---|
| **Inputs** | Invoice Quantity, Invoice Dollars |
| **Output** | Predicted Freight Cost |

### Module 2 — Invoice Risk Flagging

<img width="1918" height="1075" alt="image" src="https://github.com/user-attachments/assets/af8f9ee2-d284-4457-9af2-613e4a804069" />


| | |
|---|---|
| **Inputs** | Quantities, Invoice Dollars, Freight Cost, Delay Features |
| **Outputs** | ✅ Safe Invoice &nbsp;/&nbsp; ⚠️ Manual Review Required |

Invoices are labeled risky if an invoice total mismatch exists **or** the average receiving delay exceeds 10 days — a rule-based label used to train the classifier.

### Modeling Summary

- Logistic Regression and Decision Tree baselines, with a **Random Forest Classifier** as the final model
- Feature significance confirmed via **T-Test** (`p < 0.05`); low-significance features (Days to Pay, Total Brands) dropped
- **StandardScaler / MinMaxScaler** applied before training
- **GridSearchCV** hyperparameter tuning + **5-fold cross-validation**
- **Final accuracy: 89%**
- Trained models and scalers serialized with **Joblib** for inference

### Technical Stack

| Component | Technology |
|---|---|
| Language | Python 3.9+ |
| ML | scikit-learn, SciPy (statistical testing) |
| Data | pandas, NumPy, SQLite |
| App | Streamlit |
| Serialization | Joblib |

---

## Repository Structure

```text
Siplytics/
│
├── data/                                # Raw CSV data files (vendor performance)
├── logs/                                # Ingestion and processing logs
│   └── ingestion_db.log
├── Ingestion and EDA.ipynb              # Data ingestion and exploratory analysis
├── ingestion_db.py                      # Loads CSVs into the SQLite database
├── inventory.db                         # SQLite database (vendor performance)
├── Siplytics_project_report.pdf         # Comprehensive project report
├── Vendor Performance Analysis.ipynb    # Vendor performance & statistical analysis
├── SiplyticsDashboard.pbix              # Power BI dashboard file
├── summary_table.csv                    # Summary output table
│
├── Invoice_Intelligence_System/         # ML-driven invoice intelligence app
│   ├── app.py                           # Streamlit app (freight prediction + risk flagging)
│   ├── requirements.txt
│   ├── data/
│   │   └── yourfile.db                  # SQLite database (purchase + vendor invoice tables)
│   ├── freight_cost_prediction/
│   │   ├── data_preprocessing.py
│   │   ├── modeling_evaluation.py
│   │   ├── train.py
│   │   └── models/                      # Serialized freight-cost model + scaler
│   ├── invoice_flagging/
│   │   ├── data_preprocessing.py
│   │   ├── modeling_evaluation.py
│   │   ├── train.py
│   │   └── models/                      # Serialized risk-classification model + scaler
│   ├── inference/
│   │   ├── predict_freight.py
│   │   └── predict_invoice_flag.py
│   ├── notebooks/                       # Freight cost & invoice flagging notebooks
│   └── screenshots/                     # App UI screenshots
│
└── README.md                            # This file
```

---

## How the Two Parts Fit Together

Both components draw on the same underlying purchase, sales, and freight data, but operate at different altitudes:

1. **Ingest & model vendor-level performance** (root pipeline → Power BI) to understand which vendors, brands, and purchasing patterns drive profitability and risk at a portfolio level.
2. **Score individual invoices** (`Invoice_Intelligence_System/`) against ML models trained on that same data, to catch pricing anomalies and risky invoices before they're paid.

Together they give a business both the strategic view ("where is vendor risk concentrated?") and the operational safeguard ("should this invoice be paid as-is?").

---

## Future Improvements

- Real-time REST API for freight/risk scoring
- Cloud deployment (AWS / Azure / GCP)
- MLflow for experiment tracking, Airflow for pipeline orchestration
- ERP system integration
- Feeding invoice-level risk scores back into the Power BI vendor dashboard for a unified view

---

## Conclusion

Siplytics turns raw purchase, sales, and freight data into a complete vendor intelligence platform — a Power BI dashboard for portfolio-level vendor performance, paired with a Streamlit ML application (89% classification accuracy) that predicts freight costs and flags risky invoices in real time.
