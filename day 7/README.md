 📊 Task 1: Load Data into MySQL from Python  

 🔍 Overview  
This task involves **downloading data from Gapminder** for:  
1. **Communication > Cell phones (total)**  
2. **Population**  

Then, we will **load these datasets into MySQL** as **two separate tables** using Python and Pandas.  

 📂 Files in this Folder  

| File Name                  | Description |
|---------------------------|-------------|
| `load_gapminder_data.ipynb` | Jupyter Notebook with the Python script to load data into MySQL |
| `cell_phones.xlsx`         | Excel file containing cell phone usage data from Gapminder |
| `population.xlsx`          | Excel file containing population data from Gapminder |
| `README.md`                | Task description and details |

 📊 Data Description  

The **Gapminder dataset** consists of:  

 **1. Cell Phones Data (cell_phones.xlsx)**  
- **Country**: Name of the country.  
- **Year**: The year of recorded data.  
- **Cell Phones (Total)**: Total number of cell phones in use for that country and year.  

**2. Population Data (population.xlsx)**  
- **Country**: Name of the country.  
- **Year**: The year of recorded data.  
- **Population**: The total population for that country and year.  

 🛠️ Steps to Perform  

1️⃣ **Download the Excel Files from Gapminder**  
   - Download **"Cell Phones (Total)"** and **"Population"** datasets.  

2️⃣ **Read Data into Pandas DataFrames**  
   - Use **pandas.read_excel()** to load both datasets.  
   - Perform basic **data cleaning** (remove NaN values, standardize country names if needed).  

3️⃣ **Connect to MySQL Database**  
   - Use **MySQL Connector** or **SQLAlchemy** to establish a connection.  

4️⃣ **Create MySQL Tables**  
   - Table 1: `cell_phones_data`  
   - Table 2: `population_data`  
   - Ensure **primary keys and foreign keys** are structured correctly.  

5️⃣ **Load Data into MySQL**  
   - Insert **cell phones data** into `cell_phones_data` table.  
   - Insert **population data** into `population_data` table.  

6️⃣ **Verify Data in MySQL**  
   - Run **SELECT queries** to confirm successful insertion.  

---

 📊 Task 2: Aggregations on Cell Phone Data  

 🔍 Overview  
This task involves performing **aggregations** on the dataset containing **the number of cell phones** for each year. We will compute the following:  
- **MAX** (Maximum number of cell phones per year)  
- **AVG** (Average number of cell phones per year)  
- **SUM** (Total number of cell phones per year)  

 📂 Files in this Folder  

| File Name                  | Description |
|---------------------------|-------------|
| `aggregation_analysis.ipynb` | Jupyter Notebook with the Python script for aggregation |
| `cell_phones_data.csv`     | Dataset containing cell phone usage per year |
| `README.md`                | Task description and details |

 📊 Data Description  

The dataset consists of:  

- **Country**: Name of the country  
- **Year**: The year of recorded data  
- **Cell Phones (Total)**: Total number of cell phones used in that country and year  

 🛠️ Steps to Perform  

1️⃣ **Load the Dataset**  
   - Use **pandas.read_csv()** to read the dataset.  

2️⃣ **Perform Aggregations**  
   - Compute **MAX** (Maximum cell phones per year).  
   - Compute **AVG** (Average number of cell phones per year).  
   - Compute **SUM** (Total number of cell phones per year).  

3️⃣ **Visualize the Results**  
   - Use **Matplotlib/Seaborn** to create bar charts or line plots.  

4️⃣ **Save Aggregated Results**  
   - Store results in a **new CSV file** or **display in a table**.    
---

 📊 Task 3: Joining Tables to Calculate Cell Phones per Person  

 🔍 Overview  
This task involves **joining two tables** in **SQL Workbench** to calculate the **number of cell phones per person** for each country and year. We will:  
- **Join the `cell_phones_data` table with the `population_data` table** using `Country` and `Year` as keys.  
- **Calculate the number of cell phones per person** using the formula:  

  \[
  \text{Cell Phones per Person} = \frac{\text{Total Cell Phones}}{\text{Population}}
  \]

📂 Files in this Folder  

| File Name                  | Description |
|---------------------------|-------------|
| `join_query.sql`           | SQL script for joining tables and calculating cell phones per person |
| `cell_phones_data.csv`     | Dataset containing total cell phones per country and year |
| `population_data.csv`      | Dataset containing population per country and year |
| `README.md`                | Task description and details |

📊 Data Description  

The database contains **two tables**:  

 **1. Cell Phones Data (`cell_phones_data`)**  
- **Country**: Name of the country  
- **Year**: The year of recorded data  
- **Cell Phones (Total)**: Total number of cell phones in that country and year  

**2. Population Data (`population_data`)**  
- **Country**: Name of the country  
- **Year**: The year of recorded data  
- **Population**: The total population of that country in that year  

🛠️ Steps to Perform  

1️⃣ **Load Data into SQL Workbench**  
   - Import `cell_phones_data.csv` and `population_data.csv` into **MySQL Workbench**.  

2️⃣ **Join the Tables**  
   - Use an **INNER JOIN** on `Country` and `Year`.  

3️⃣ **Calculate Cell Phones per Person**  
   - Use SQL to compute:  
     ```sql
     SELECT 
         cp.Country, 
         cp.Year, 
         cp.`Cell Phones (Total)`, 
         p.Population, 
         (cp.`Cell Phones (Total)` / p.Population) AS `Cell Phones per Person`
     FROM cell_phones_data cp
     INNER JOIN population_data p
     ON cp.Country = p.Country AND cp.Year = p.Year;
     ```
  
4️⃣ **Save and Export Results**  
   - Store the **joined table and results** in a new table.  

---

 📊 Task 4: Aggregations with Retrieval / Window Functions  

🔍 Overview  
This task involves performing **aggregations and retrieval using SQL window functions** to determine:  
- The **country with the MAX number of cell phones** for each year.  
- How to use **window functions** for ranking data efficiently.  

 📂 Files in this Folder  

| File Name                | Description |
|-------------------------|-------------|
| `aggregation_query.sql`  | SQL script to retrieve country with max cell phones per year |
| `cell_phones_data.csv`   | Dataset containing total cell phones per country and year |
| `README.md`              | Task description and details |

 📊 Data Description  

The **`cell_phones_data`** table contains:  
- **Country**: Name of the country  
- **Year**: The year of recorded data  
- **Cell Phones (Total)**: Total number of cell phones in that country and year  

 🛠️ Steps to Perform  

1️⃣ **Load Data into SQL Workbench**  
   - Import `cell_phones_data.csv` into **MySQL Workbench**.  

2️⃣ **Use Window Functions to Find MAX per Year**  
   - Use the **RANK()** function to rank countries by cell phones within each year.  

   ```sql
   SELECT Country, Year, `Cell Phones (Total)`
   FROM (
       SELECT 
           Country, 
           Year, 
           `Cell Phones (Total)`, 
           RANK() OVER (PARTITION BY Year ORDER BY `Cell Phones (Total)` DESC) AS rank
       FROM cell_phones_data
   ) ranked_data
   WHERE rank = 1;
   ```
  
3️⃣ **Alternative Using GROUP BY and MAX()**  
   - Another approach using **GROUP BY** and **JOIN**:  
   
   ```sql
   SELECT c1.Country, c1.Year, c1.`Cell Phones (Total)`
   FROM cell_phones_data c1
   WHERE c1.`Cell Phones (Total)` = (
       SELECT MAX(c2.`Cell Phones (Total)`) 
       FROM cell_phones_data c2
       WHERE c1.Year = c2.Year
   );
   ```

4️⃣ **Save and Export Results**  
   - Store the **results in a new table** or export as CSV.  
---

