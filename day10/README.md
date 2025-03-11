**Project: Cricket Data Analysis Capstone Project**

 Overview
This capstone project focuses on cricket data extraction, transformation, and analysis to build interactive dashboards for player and team performance insights. The project utilizes data from **ESPN Cricinfo (via web scraping)** or **Kaggle datasets** to generate meaningful insights, including **player statistics, auction prices, chemistry scores, and historical trends.** The final output includes **visual dashboards in Tableau or Power BI** for interactive exploration.

 Files in This Repository

| **File Name**       | **Description** |
|----------------------|----------------|
| `data_extraction.ipynb`  | Jupyter Notebook for scraping cricket data from ESPN Cricinfo or loading Kaggle datasets |
| `data_cleaning.ipynb`    | Jupyter Notebook for transforming and cleaning the data |
| `player_auction_data.csv`| Dataset containing IPL auction prices for players |
| `match_data.csv`         | Cleaned dataset containing ball-by-ball match data |
| `player_performance.csv` | Aggregate player performance statistics |
| `team_performance.csv`   | Aggregate team-level performance statistics |
| `dashboard.pbix`         | Power BI dashboard for visualization |
| `dashboard.twbx`         | Tableau workbook for visualization |
| `README.md`              | This document |

---

 Data Extraction

   1: Scraping from ESPN Cricinfo
- Extract ball-by-ball commentary and match data.
- Collect **player names, match details, runs, wickets, and events**.
- Ensure data coverage of **at least 5 years** for reliable insights.

  2: Using Kaggle Datasets
- Load pre-existing cricket datasets from Kaggle.
- Perform necessary **data transformations** to ensure consistency.

---

Data Transformation
The extracted data is **cleaned and processed** to extract the following key features:

 **Match Details**
- **Match Name**
- **Match Date**
- **Series Name & Year**
- **Match Venue**
- **Winning Team**
- **Team 1 Score & Team 2 Score**

 **Ball-Level Details**
- **Ball No, Over No**
- **Bowler Name, Batter Name**
- **Ball Type (Dot, Wide, No Ball, etc.)**
- **Shot Type (Boundary, Single, etc.)**
- **Runs Scored**
- **Speed of the Ball (if available)**

 **Additional Data**
- Player auction price (matched from **Kaggle datasets**).
- Mapping player **nationality, age, and team changes**.
- Calculating **player chemistry scores** (striker and non-striker performance together).

---

 Data Loading
The cleaned and transformed data is stored in **CSV format** and loaded into visualization tools.

- **Aggregate Player Performance**: Grouped stats like batting average, wickets, strike rate.
- **Match-Wise Data**: Summarized performances across multiple matches.
- **Team-Level Data**: Auction trends, win/loss ratios, and team strength analysis.

---

 Reporting & Dashboarding
Dashboards are created using **Tableau** (preferred for web publishing) and **Power BI**.

**Dashboard Features**
1. **Player Profile Dashboard**
   - Dropdown to select a player and view:
     - **Average Run Rate**
     - **Batting/Bowling Style**
     - **Team History Timeline**
     - **Auction Price Trends**
     - **Player Chemistry Score**

2. **Statistical Dashboard**
   - Graphs for **player performance across matches, series, and teams**.
   - Heatmaps for **bowler effectiveness and batting consistency**.

3. **Team Insights**
   - **Ranking trends over years**
   - **Auction expenditures per season**
   - **Competitor analysis (most losses against a particular team)**

4. **Venue & Series Analytics**
   - **Best players per stadium**
   - **Performance in different playing conditions (home vs. away)**

---
 Tools & Technologies
- **Python (Pandas, BeautifulSoup, Selenium, NumPy)**
- **Jupyter Notebooks for data processing**
- **SQL for structured data management**
- **Power BI / Tableau for dashboards**
- **Kaggle for additional datasets**

---

Conclusion
This project provides a **comprehensive cricket analytics framework**, allowing users to explore **player statistics, team trends, and auction insights** through **interactive dashboards**. The use of **advanced analytics** like **player chemistry and AI-based scores** makes it a **unique and insightful project** for cricket enthusiasts and data analysts.
