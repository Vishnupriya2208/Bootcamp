
---
 **📂 Task 1: Load Data into Databricks from Excel**  

### **📌 Overview**  
This task involves **uploading datasets** into Databricks, processing them, and storing them in tables for further analysis. We will be working with **data from Gapminder** for:  
1. 📞 **Communication > Cell phones (total)**  
2. 👥 **Population**  

We will load these datasets into **Databricks tables** and use PySpark for processing.  

---

 **📁 Files in this Folder**  

| **File Name**          | **Description**  |  
|----------------------|----------------|  
| `cell_phones.xlsx`    | Excel file containing cell phone usage data from Gapminder. |  
| `population.xlsx`     | Excel file containing population data from Gapminder. |  
| `load_data_databricks.ipynb` | Databricks Notebook with PySpark script to load data. |  
| `README.md`          | Task description and setup details. |  

---

**📌 Databricks Environment Setup**  

1️⃣ **Create a Cluster:**  
- Go to **Compute** → Click **Create Cluster**  
- Choose **Single Node** or **Standard Mode**  
- Select **Databricks Runtime (DBR) >= 10.x**  
- Click **Create Cluster**  

2️⃣ **Create & Attach a Notebook:**  
- Go to **Workspace** → Click **Create** → Select **Notebook**  
- Name it: `load_data_databricks`  
- Select **Python** as the default language  
- Attach the notebook to the running cluster  

---

 **📌 Steps to Load Data in Databricks**  

 **1️⃣ Upload Excel Files to DBFS (Databricks FileStore)**
- Navigate to **Data** → Click **Add Data**  
- Upload `cell_phones.xlsx` & `population.xlsx`  
- Databricks will store them under `/FileStore/tables/`  

 **2️⃣ Load Data Using PySpark**

 **3️⃣ Verify Table Creation**
Run the SQL command in a new Databricks cell:
---

 **📌 Next Steps**  
✔ **Join both datasets** and calculate **cell phones per capita**  
✔ **Visualize data** using Databricks **display()** function  
✔ **Export cleaned data** for Tableau analysis  

---


 📂 Task 2: Load Data into Databricks from Excel  

 📌 Overview  
This task involves **downloading data from Gapminder** for:  
1. 📞 **Communication > Cell phones (total)**  
2. 👥 **Population**  

We will load these datasets into **Databricks as tables** using **PySpark**.  

---

 📁 Files in this Folder  

| **File Name**          | **Description**  |  
|----------------------|----------------|  
| `cell_phones.xlsx`    | Excel file containing cell phone usage data from Gapminder. |  
| `population.xlsx`     | Excel file containing population data from Gapminder. |  
| `load_data_databricks.ipynb` | Databricks Notebook with PySpark script to load data. |  
| `README.md`          | Task description and setup details. |  

---

📌 Databricks Environment Setup  

**1️⃣ Create a Databricks Cluster**  
- Navigate to **Compute** → Click **Create Cluster**  
- Select **Single Node** or **Standard Mode**  
- Choose **Databricks Runtime (DBR) >= 10.x**  
- Click **Create Cluster**  

**2️⃣ Create & Attach a Notebook**  
- Go to **Workspace** → Click **Create** → Select **Notebook**  
- Name it: `load_data_databricks`  
- Select **Python** as the default language  
- Attach the notebook to the running cluster  

---

 📌 Steps to Load Data in Databricks  

 **1️⃣ Upload Excel Files to DBFS (Databricks FileStore)**
- Navigate to **Data** → Click **Add Data**  
- Upload `cell_phones.xlsx` & `population.xlsx`  
- Databricks will store them under `/FileStore/tables/`  

 **3️⃣ Verify Table Creation**
Run the  SQL command in a new Databricks cell:l
---

 📌 Next Steps  
✔ **Join both datasets** and calculate **cell phones per capita**  
✔ **Visualize data** using Databricks **display()** function  
✔ **Export cleaned data** for Tableau analysis  

---
Here is a **README.md** file formatted similarly to your reference, covering catalog browsing and version history checkpointing.  

---

📂 Task 3: Browse Catalog & Version History in Databricks  

 📌 Overview  
After **loading data into Databricks tables**, the next step is to:  
1. 🔍 **Browse the tables** in the **Catalog**  
2. 📝 **Checkpoint the notebook** in **Version History**  

---

 📁 Files in this Folder  

| **File Name**             | **Description**  |  
|-------------------------|----------------|  
| `cell_phones.xlsx`       | Excel file containing cell phone usage data from Gapminder. |  
| `population.xlsx`        | Excel file containing population data from Gapminder. |  
| `load_data_databricks.ipynb` | Databricks Notebook with PySpark script to load data. |  
| `README.md`             | Task description and setup details. |  
| `catalog_screenshot.png` | Screenshot of tables inside Databricks Catalog. |  
| `version_checkpoint.png` | Screenshot of notebook checkpoint in Version History. |  

---

 📌 Browse Tables in Databricks Catalog  

 **1️⃣ Navigate to Catalog**
- In **Databricks UI**, go to **Data**  
- Click on **Catalog** → Select **default** database  
- You should see the created tables:  
  - 📊 `cell_phones`  
  - 👥 `population`  
---

 📌 Checkpoint Notebook in Version History  

**1️⃣ Save a Notebook Checkpoint**  
- Open the **Databricks Notebook (`load_data_databricks.ipynb`)**  
- Click **Version History** (top-right corner)  
- Click **Save Version**  

---

 📌 Verify Tables with SQL  

Run the  SQL command in a **new Databricks cell** to verify tables:    

---

## 📌 Next Steps  
✔ **Join datasets** to calculate **phones per capita**  
✔ **Create visualizations** for analysis  
✔ **Export processed data** for further use  

---
Here is a **README.md** file formatted similarly to your reference, covering the **Rise of Cell Phones** analysis and visualization in Databricks.  

---

 📊 Task 4: Rise of Cell Phones  

📌 Overview  
This task involves **analyzing the growth of cell phone usage** by computing **cell phones per person** and visualizing the trend over time.  

 **Key Steps:**  
1. **Join datasets**: 📱 `cell_phones` and 👥 `population`  
2. **Calculate cell phones per capita**: `(cell_phones / population)`  
3. **Create a Line Chart** 📈:  
   - **X-axis**: Number of cell phones per person  
   - **Y-axis**: Year  

---

📁 Files in this Folder  

| **File Name**             | **Description**  |  
|-------------------------|----------------|  
| `cell_phones.xlsx`       | Excel file containing cell phone usage data from Gapminder. |  
| `population.xlsx`        | Excel file containing population data from Gapminder. |  
| `rise_of_cell_phones.ipynb` | Databricks Notebook with analysis and visualization. |  
| `README.md`             | Task description and setup details. |  
| `cell_phones_chart.png` | Screenshot of the generated **Line Chart** visualization. |  

---

 📌 Data Processing Steps  

 **1️⃣ Load Data into Databricks**  

---
 **2️⃣ Join Datasets & Calculate Cell Phones Per Person**  
---
**3️⃣ Create Line Chart in Databricks**  

---

 📌 Next Steps  
✔ **Export processed data** for further analysis  
✔ **Compare trends across different countries**  
✔ **Incorporate additional factors (e.g., GDP, internet usage)**  

---
