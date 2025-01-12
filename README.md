# AI Symptom Checker

This project is an AI-powered tool for analyzing symptoms and predicting potential medical conditions with probabilities.

## Project Directory Structure
```plaintext
AI SYMPTOM CHECKER/
├── cloud/
│   └── README.md
├── data/
│   ├── processed/
│   │   └── (empty or processed files go here)
│   ├── raw/
│   │   ├── Diseases_Symptoms.csv
│   │   └── medlineplus_diseases.csv
├── notebooks/
│   └── (Jupyter notebooks go here)
├── scripts/
│   ├── Data collection.py
│   └── upload_to_s3.py
├── symptom-checker/
│   └── README.md
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
├── requirements.txt
└── README.md



## Data Collection Overview
The data collection step is divided into five chapters:

1. **Understanding Requirements**:
   - **Goal**: Collect data on symptoms, conditions, and probabilities.
   - **Sources**: Web scraping, public APIs, open datasets.

2. **Web Scraping**:
   - **Tools**: BeautifulSoup, Scrapy.
   - **Example**: Scraped **MedlinePlus Encyclopedia** for disease data.

3. **Public APIs**:
   - **Tools**: `requests`, authentication for APIs like Symptoma.

4. **Open Datasets**:
   - **Sources**: Kaggle, MIMIC-III.
   - **Example**: Processed `medlineplus_diseases.csv` and merged datasets.

5. **Cloud Storage**:
   - **AWS S3 Bucket**: `symptom-checker-raw-data`.
   - **Script**: Automated uploads using `boto3`.

## Next Steps
- Data Warehousing and ETL pipeline development.

## How to Run
1. **Set Up Environment**:
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate it:
     ```bash
     source venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run Scripts**:
   - Scrape data:
     ```bash
     python scripts/Data\ collection.py
     ```
   - Upload to S3:
     ```bash
     python scripts/upload_to_s3.py
     ```

## Contact
For any questions or collaboration opportunities, please reach out via GitHub or LinkedIn!
