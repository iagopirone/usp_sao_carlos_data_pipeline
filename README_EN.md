# USP São Carlos – Automated Institutional Data Pipeline
[Português](README.md) | English

![USP São Carlos](https://img.shields.io/badge/USP-São%20Carlos-0050A0)
![Institutional Project](https://img.shields.io/badge/Project-Institutional-blue)
![PUB-USP](https://img.shields.io/badge/PUB-USP%202024/2025-lightgrey)
![ETL](https://img.shields.io/badge/ETL-Production%20Ready-success)
![Validation](https://img.shields.io/badge/Validation-2019--2024-green)
![Reusable](https://img.shields.io/badge/Reusable-Yearly-important)
![License](https://img.shields.io/badge/License-MIT-black)

This repository contains a complete ETL pipeline designed to automate the extraction, filtering and standardization of institutional indicators for the São Carlos campus of the University of São Paulo (USP).  
The data is collected directly from the official USP Statistical Yearbook (USP Digital).

The project was developed under the **USP Unified Scholarship Program (PUB-USP)** with the goal of replacing manual, repetitive indicator collection with a reproducible, structured and long-term reusable system.

---

## Problem addressed

The Statistical Yearbook consolidates data for the entire university.  
Because of this, each campus traditionally needs to manually extract, filter and reorganize information to obtain its own indicators — a process that is slow, error-prone and repeated every year.

This pipeline addresses this problem by:

- downloading official tables directly from the USP Digital website,  
- standardizing column formats across different Yearbook editions,  
- isolating rows corresponding specifically to the São Carlos campus,  
- exporting clean, analysis-ready CSV files,  
- and enabling full yearly reuse with minimal effort.

---

## Progress relative to the official schedule

According to the PUB-USP project plan, the full development cycle spans 12 months, including exploratory analysis, progressive module implementation, testing, documentation and training.

The actual development began on **September 4th**.  
Within the first weeks, the following components were completed:

- the full extraction module;  
- the full transformation module;  
- the load module;  
- an integrated and validated pipeline using multiple Yearbook editions (2019–2024);  
- standardized filtering for São Carlos;  
- the final ETL architecture, modular and reusable.

Based on the official schedule, these results correspond to approximately **months 6–7** of the project.  
In practice, development is **three to four months ahead of plan**, demonstrating fast execution, autonomy and technical maturity.

---

## Processed indicators

The pipeline automatically processes the following datasets:

- Territorial area  
- Infrastructure  
- Administrative staff  
- Faculty  
- Undergraduate snapshot  
- Graduate programs (CAPES snapshot)  
- Graduate historical evolution  
- Distance extension courses  

Note: The pipeline is generic and independent of the year.  
The 2019–2024 editions were used solely for validation. The system is ready to process any future Yearbook edition as soon as it is released.

---

## Project structure

