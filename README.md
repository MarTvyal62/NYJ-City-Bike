# 🚲 Jersey City Citi Bike Operational Analytics Pipeline

[![Live Presentation](https://shields.io)](https://github.io)
[![Interactive Dashboard](https://shields.io)](https://tableau.com)
[![Python Pipeline](https://shields.io)](https://github.com)

## 📌 Executive Summary
An end-to-end data science and business intelligence pipeline that automates data ingestion, cleaning, cross-domain API enrichment, and geospatial density mapping for over multi-period transit transaction logs. This project explicitly demonstrates how raw, unstructured commuter logs can be programmatically engineered to uncover critical operational bottlenecks and weather-driven user behavioral shifts.

---

## 🚀 Interactive Deliverables
*   **📊 Web Data Story (Reveal.js):** [Launch the Live Presentation](https://github.io)  
    *An interactive, slide-based strategic business proposal detailing transaction speeds, system volume anomalies, and user trend diagnostics.*
*   **📈 BI Dashboard (Tableau):** [View Production Visualization Track](https://tableau.com)  
    *Executive management tracking views leveraging advanced LOD expressions, analytical parameters, and transactional filter toggles.*

---

## 🛠️ Technical Architecture & Pipeline Stages

### 1. Data Ingestion & Storage Automation
*   Engineered a modular Python retrieval pipeline utilizing programmatic URL builders to systematically extract, isolate, and structure compressed `.csv` zip files into distinct directory trees.

### 2. Analytical Data Cleansing & Optimization (Pandas & NumPy)
*   Profiled multi-million row matrices to strip text-schema anomalies, handle corrupt coordinate inputs, and re-index messy timestamp properties.
*   Generated structural feature flags isolating weekend vs. weekday temporal customer profiles to measure commuter retention thresholds.

### 3. Cross-Domain REST API Enrichment
*   Written request workflows querying external meteorological databases to extract real-time regional weather variables (precipitation indices, wind speeds, temperatures), joining matrices against hourly ride density.

### 4. Advanced Geospatial Aggregation (GeoPandas & PostGIS logic)
*   Mapped spatial distributions and density networks across localized urban polygon boundaries utilizing `GeoPandas`, `Shapely` geometric shapes, and interactive `Folium` mapping engines.

---

## 📊 Core Stack
*   **Languages & Scripting:** Python 3.10, Markdown
*   **Data Science Suite:** Pandas, NumPy, Jupyter Notebooks, Anaconda
*   **Visualization & BI Engines:** Tableau Desktop, Reveal.js Engine, Plotly, Folium, Seaborn, Matplotlib
*   **Geospatial Processing:** GeoPandas, Shapely

---
💡 *Developed with a strict application-engineering focus on optimized execution runtime and clean data separation protocols.*
