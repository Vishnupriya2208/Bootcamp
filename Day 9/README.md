

 📊 Task 1: Life Expectancy Chart  

📌 Overview  
This task involves **analyzing the trends in life expectancy over time** and visualizing it using **Power BI**.  

 **Key Steps:**  
1. **Load dataset** containing life expectancy and year-wise records.  
2. **Calculate the average life expectancy per year**.  
3. **Create a Line Chart** 📈 in Power BI:  
   - **X-axis**: Year  
   - **Y-axis**: Average Life Expectancy  

---

 📁 Files in this Folder  

| **File Name**           | **Description**  |  
|-------------------------|----------------|  
| `life_expectancy.xlsx`  | Excel file containing life expectancy data from Gapminder. |  
| `life_expectancy.pbix`  | Power BI file with data visualization. |  
| `README.md`            | Task description and setup details. |  
| `life_expectancy_chart.png` | Screenshot of the generated **Life Expectancy Chart**. |  

---

📌 Data Processing Steps  

**1️⃣ Load Data into Power BI**  
- Import **life_expectancy.xlsx** into Power BI  
- Load it into the **Data Model**  

---
 **2️⃣ Data Preparation & Calculation**  

- Open **Power BI Desktop**  
- Select **Transform Data**  
- Ensure the dataset contains **Year** and **Life Expectancy**  
- Create a **Measure** for **Average Life Expectancy**  
  
---

**3️⃣ Create Line Chart in Power BI**  

#### **Steps to Create the Chart:**  
1. **Go to the "Report" View**  
2. Click on **Line Chart** visualization  
3. Set **X-axis** → `Year`  
4. Set **Y-axis** → `AvgLifeExpectancy` (Measure created)  
5. Format the chart (Title, Colors, Labels, Gridlines)  

📸 **Save the chart as** `life_expectancy_chart.png`

---
 📌 Next Steps  
✔ **Compare life expectancy trends by country**  
✔ **Analyze correlation with GDP and healthcare factors**  
✔ **Enhance visualization with additional filters and drill-downs**  

---
Here is the **README.md** file formatted similarly to your reference, covering the **Income Chart** analysis and visualization in Power BI.  

---

 📊 Task 2: Income Chart  

📌 Overview  
This task involves **analyzing the trends in income over time** and visualizing it using **Power BI**.  

**Key Steps:**  
1. **Load dataset** containing income and year-wise records.  
2. **Calculate the Average, Minimum, and Maximum Income per year**.  
3. **Create a Line Chart** 📈 in Power BI:  
   - **X-axis**: Year  
   - **Y-axis**: Average, Min, and Max Income  

---

 📁 Files in this Folder  

| **File Name**           | **Description**  |  
|-------------------------|----------------|  
| `income_data.xlsx`  | Excel file containing income data from Gapminder. |  
| `income_chart.pbix`  | Power BI file with data visualization. |  
| `README.md`            | Task description and setup details. |  
| `income_chart.png` | Screenshot of the generated **Income Chart**. |  

---

 📌 Data Processing Steps  

 **1️⃣ Load Data into Power BI**  
- Import **income_data.xlsx** into Power BI  
- Load it into the **Data Model**  

---

**2️⃣ Data Preparation & Calculation**  

- Open **Power BI Desktop**  
- Select **Transform Data**  
- Ensure the dataset contains **Year** and **Income**  
- Create **Measures** for **Average, Min, and Max Income**  
---

 **3️⃣ Create Line Chart in Power BI**  

 **Steps to Create the Chart:**  
1. **Go to the "Report" View**  
2. Click on **Line Chart** visualization  
3. Set **X-axis** → `Year`  
4. Set **Y-axis** → Add `AvgIncome`, `MinIncome`, and `MaxIncome` (Measures created)  
5. Format the chart (Title, Colors, Labels, Gridlines)  

📸 **Save the chart as** `income_chart.png`

---
 📌 Next Steps  
✔ **Compare income trends by country or region**  
✔ **Analyze correlation with life expectancy and economic growth**  
✔ **Enhance visualization with tooltips, filters, and drill-downs**  

---

Here is the **README.md** file formatted for the **Rise of Cell Phones** analysis and visualization in Power BI.  

---

 📱 Task 3: Rise of Cell Phones  

## 📌 Overview  
This task involves **analyzing the rise of cell phone usage per person over time** and visualizing it using **Power BI**.  

**Key Steps:**  
1. **Load datasets** containing total cell phones and population data.  
2. **Join the two tables on** `Country` and `Year`.  
3. **Calculate the Number of Cell Phones per Person** (`Total Cell Phones / Population`).  
4. **Create a Line Chart** 📈 in Power BI:  
   - **X-axis**: Year  
   - **Y-axis**: Number of Cell Phones per Person  

---

 📁 Files in this Folder  

| **File Name**           | **Description**  |  
|-------------------------|----------------|  
| `cell_phones.xlsx`  | Excel file containing total cell phone data from Gapminder. |  
| `population.xlsx`  | Excel file containing population data from Gapminder. |  
| `rise_of_cellphones.pbix`  | Power BI file with data visualization. |  
| `README.md`            | Task description and setup details. |  
| `cellphones_chart.png` | Screenshot of the generated **Cell Phones per Person Chart**. |  

---

📌 Data Processing Steps  

 **1️⃣ Load Data into Power BI**  
- Import **cell_phones.xlsx** and **population.xlsx** into Power BI.  
- Load both datasets into the **Data Model**.  

---

**2️⃣ Data Preparation & Transformation**  

- **Join the tables** using the `Merge Queries` option in Power Query:  
  - **Join condition**: `Country` and `Year` (common fields).  
  - Select `Inner Join` to keep matching records.  

- **Create a Calculated Column** for **Number of Cell Phones per Person** using **DAX**:  
---

 **3️⃣ Create Line Chart in Power BI**  

**Steps to Create the Chart:**  
1. **Go to the "Report" View**  
2. Click on **Line Chart** visualization  
3. Set **X-axis** → `Year`  
4. Set **Y-axis** → `PhonesPerPerson` (Calculated Column)  
5. Apply filters (e.g., by country or region) if needed  
6. Format the chart (Title, Colors, Labels, Gridlines)  

📸 **Save the chart as** `cellphones_chart.png`

---
 📌 Next Steps  
✔ **Compare trends by country or region**  
✔ **Analyze correlation with GDP, income, or internet penetration**  
✔ **Enhance visualization with filters and drill-downs**  

---

Here is the **README.md** file formatted for the **World Map Visualization in Power BI**.  

---

 🌍 Task 4: World Map Visualization  

 📌 Overview  
This task involves **creating an interactive world map** 🌍 in Power BI where countries are **colored by their population** with a **slider to select different years**.  

**Key Steps:**  
1. **Load the Population dataset** into Power BI.  
2. **Ensure data contains** `Country`, `Year`, and `Population`.  
3. **Create a Map visualization** where:  
   - Countries are **colored based on their population**.  
   - A **Year slicer (slider)** allows filtering the data dynamically.  

---
 📁 Files in this Folder  

| **File Name**           | **Description**  |  
|-------------------------|----------------|  
| `population.xlsx`  | Excel file containing population data from Gapminder. |  
| `world_map.pbix`  | Power BI file with the world map visualization. |  
| `README.md`            | Task description and setup details. |  
| `world_map_visual.png` | Screenshot of the generated **World Map Chart**. |  

---

 📌 Data Processing Steps  

**1️⃣ Load Data into Power BI**  
- Import **population.xlsx** into Power BI.  
- Ensure the dataset contains `Country`, `Year`, and `Population` columns.  
- Verify that `Country` is correctly recognized as a **Geographical field**.  

---

 **2️⃣ Create Data Model & Transform Data**  

- Check and clean the data in **Power Query Editor**.  
- Format `Year` as **a numeric or date field** for use in the slicer.  
- Ensure `Country` is assigned to **Geographical Data Category** (Data Type: Text → Geographic → Country/Region).  

---

 **3️⃣ Create World Map Visualization in Power BI**  

**Steps to Create the Map:**  
1. **Go to the "Report" View**.  
2. Click on **Map Visualization** 🗺️ or **Filled Map** (Choropleth).  
3. Set **Location** → `Country`.  
4. Set **Color Saturation** → `Population` (Darker colors for higher populations).  
5. Add a **Year Slicer (Slider)**:  
   - Click on the **Slicer** visualization.  
   - Select `Year` as the field.  
   - Change it to a **Slider** format.  
6. **Format the Map**:  
   - Adjust color scale for better visibility.  
   - Enable tooltips to show **Country Name & Population**.  

📸 **Save the visualization as** `world_map_visual.png`  
---
 📌 Next Steps  
✔ **Enhance the map by adding GDP or birth rate** for deeper insights.  
✔ **Drill down into specific continents or regions**.  
✔ **Use animation to show population trends dynamically**.  

---

