
 📌 Task 1: Analyze `robots.txt` for Amazon, ESPNCricInfo, and Instagram  

🔍 Overview  
This task involves analyzing the `robots.txt` files of **Amazon, ESPNcricinfo, and Instagram** to understand the limits set by these websites for web scraping. The `robots.txt` file defines which parts of a website can be accessed by web crawlers and which are restricted.  

📂 Files in this Folder  

| File Name       | Description |
|----------------|-------------|
| `robots_analysis.ipynb` | Jupyter Notebook with the code for fetching and analyzing `robots.txt` files |
| `robots_amazon.txt` | Extracted `robots.txt` file of Amazon |
| `robots_espn.txt` | Extracted `robots.txt` file of ESPNcricinfo |
| `robots_instagram.txt` | Extracted `robots.txt` file of Instagram |
| `README.md` | Task description and details |

 📊 Data Description  

Each `robots.txt` file contains directives that specify:  
- **Allowed paths**: Sections that can be crawled.  
- **Disallowed paths**: Sections that are restricted from web crawlers.  
- **User-agent directives**: Specific instructions for different search engines and bots.  
- **Crawl-delay (if any)**: Specifies how frequently bots should make requests.  

🛠️ Steps to Perform  

1️⃣ **Fetch `robots.txt` files**: Use Python's `requests` module to fetch `robots.txt` from each website.  
2️⃣ **Analyze Directives**:  
   - Identify `User-agent` rules.  
   - List `Disallow` and `Allow` rules.  
   - Check for `Crawl-delay`.  
3️⃣ **Summarize Findings**:  
   - Compare the level of restriction for different websites.  
   - Identify whether scraping is allowed or heavily restricted.  
4️⃣ **Visualize Restrictions** (Optional): Create a table or word cloud to highlight blocked sections.  
----

Here’s a structured README for scraping **ball-by-ball commentary** and extracting structured data for the **GT vs RR Final** match:  

---

 🏏 Task 2: Scrape Ball-by-Ball Commentary - GT vs RR Final  

🔍 Overview  
This task involves scraping **ball-by-ball commentary** from a cricket match between **Gujarat Titans (GT) and Rajasthan Royals (RR) Final**, extracting relevant structured data, and storing it in a tabular format.  

We will **ignore general commentary** and focus **only on the ball-by-ball details** to extract key match insights.  

 📂 Files in this Folder  

| File Name             | Description |
|----------------------|-------------|
| `scraper.ipynb`      | Jupyter Notebook with the web scraping script |
| `gt_rr_commentary.csv` | Extracted ball-by-ball structured data |
| `README.md`         | Task description and details |

📊 Data Description  

The extracted dataset includes the following key columns:  

- **Ball No**: The sequential number of the ball bowled.  
- **Over**: The current over number in the match.  
- **Bowler Name**: Name of the bowler delivering the ball.  
- **Batter Name**: Name of the batter facing the delivery.  
- **Ball Type**: Type of delivery (e.g., wide, no-ball, legal delivery).  
- **Shot Type**: Outcome of the shot (boundary, single, dot ball, etc.).  
- **Speed of Ball**: Speed of the ball (if available in the commentary).  
- **Runs Scored**: Runs scored on that particular ball.  

🛠️ Steps to Perform  

1️⃣ **Scrape Ball-by-Ball Commentary**  
   - Use **BeautifulSoup/Selenium** to extract **only** structured ball-by-ball commentary.  
   - Ignore general match commentary and focus on numerical ball-by-ball updates.  

2️⃣ **Parse and Extract Required Data**  
   - Use **Regular Expressions (Regex)** to extract bowler, batter, ball type, shot type, and runs scored.  
   - Convert the scraped text into a structured DataFrame.  

3️⃣ **Save Data in CSV Format**  
   - Store the structured ball-by-ball data in `gt_rr_commentary.csv`.  
---

🏏 Task 3: Scrape All Matches Commentary for IPL 2022  

 🔍 Overview  
This task involves **automatically scraping ball-by-ball commentary** for all matches of **IPL 2022**, navigating through the series programmatically (without manually copying URLs).  

The scraped data will be structured into a **ball-by-ball dataset**, including additional match-level details.  

 📂 Files in this Folder  

| File Name             | Description |
|----------------------|-------------|
| `ipl_2022_scraper.ipynb`      | Jupyter Notebook with the web scraping script |
| `ipl_2022_commentary.csv` | Extracted structured ball-by-ball data for all matches |
| `README.md`         | Task description and details |

 📊 Data Description  

The extracted dataset includes:  

 **Ball-by-Ball Data**  
- **Ball No**: The sequential number of the ball bowled.  
- **Over**: The current over number in the match.  
- **Bowler Name**: Name of the bowler delivering the ball.  
- **Batter Name**: Name of the batter facing the delivery.  
- **Ball Type**: Type of delivery (e.g., wide, no-ball, legal delivery).  
- **Shot Type**: Outcome of the shot (boundary, single, dot ball, etc.).  
- **Speed of Ball**: Speed of the ball (if available in the commentary).  
- **Runs Scored**: Runs scored on that particular ball.  

 **Match-Level Data**  
- **Match Name**: Team names (e.g., CSK vs MI).  
- **Match Won By**: The team that won the match and margin (e.g., "CSK won by 5 wickets").  
- **Team 1 Score**: Final score of the first team.  
- **Team 2 Score**: Final score of the second team.  
- **Match Venue**: The stadium where the match was played.  
- **Match Date**: The date when the match took place.  

 🛠️ Steps to Perform  

1️⃣ **Automate Navigation Across All IPL 2022 Matches**  
   - Use **Selenium** (or `requests` + `BeautifulSoup` if pagination allows) to **programmatically** navigate all matches.  
   - Extract match URLs dynamically.  

2️⃣ **Scrape Ball-by-Ball Commentary**  
   - Extract **only structured ball-by-ball details** from every match.  
   - Ignore general commentary.  

3️⃣ **Extract Additional Match-Level Data**  
   - Capture **match winner, venue, date, and final scores** from each match page.  

4️⃣ **Store Data in CSV Format**  
   - Save the structured **ball-by-ball dataset** in `ipl_2022_commentary.csv`.  

---

 🏏 Task 4: Scrape Multiple Series and All Matches Commentary (IPL 2021, 2022, 2023)  

 🔍 Overview  
This task involves **automating the scraping process** for **multiple IPL series (2021, 2022, 2023)**, navigating through the dropdown to select different series, and extracting **ball-by-ball commentary for all matches**.  

The script will capture **both ball-by-ball details and match-level information**, storing them in a structured format.  

 📂 Files in this Folder  

| File Name                  | Description |
|---------------------------|-------------|
| `ipl_series_scraper.ipynb` | Jupyter Notebook with the web scraping script |
| `ipl_all_series_commentary.csv` | Extracted structured ball-by-ball data for all matches of IPL 2021, 2022, and 2023 |
| `README.md`                | Task description and details |

 📊 Data Description  

The extracted dataset includes:  

 **Ball-by-Ball Data**  
- **Ball No**: The sequential number of the ball bowled.  
- **Over**: The current over number in the match.  
- **Bowler Name**: Name of the bowler delivering the ball.  
- **Batter Name**: Name of the batter facing the delivery.  
- **Ball Type**: Type of delivery (e.g., wide, no-ball, legal delivery).  
- **Shot Type**: Outcome of the shot (boundary, single, dot ball, etc.).  
- **Speed of Ball**: Speed of the ball (if available in the commentary).  
- **Runs Scored**: Runs scored on that particular ball.  

 **Match-Level Data**  
- **Match Name**: Team names (e.g., CSK vs MI).  
- **Match Won By**: The team that won the match and margin (e.g., "CSK won by 5 wickets").  
- **Team 1 Score**: Final score of the first team.  
- **Team 2 Score**: Final score of the second team.  
- **Match Venue**: The stadium where the match was played.  
- **Match Date**: The date when the match took place.  

 **Series-Level Data**  
- **Series Name**: Name of the IPL series (e.g., "IPL 2021", "IPL 2022", "IPL 2023").  
- **Series Year**: Year of the tournament.  

🛠️ Steps to Perform  

1️⃣ **Automate Dropdown Selection for Multiple IPL Series**  
   - Use **Selenium** to interact with the website’s dropdown and select different IPL series (2021, 2022, 2023).  
   - Extract match URLs dynamically for each selected series.  

2️⃣ **Scrape Ball-by-Ball Commentary for All Matches**  
   - Extract **only structured ball-by-ball details** from every match.  
   - Ignore general commentary.  

3️⃣ **Extract Additional Match & Series-Level Data**  
   - Capture **match winner, venue, date, final scores, and series details** from each match page.  

4️⃣ **Store Data in CSV Format**  
   - Save the structured **ball-by-ball dataset** in `ipl_all_series_commentary.csv`.  

---


