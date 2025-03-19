**Task 1: Commentary Word Cloud**  

 **Overview**  
This task generates a **Word Cloud** from cricket commentary data, visually representing the most frequently used words. Larger words indicate higher frequency. **Stop words** (e.g., "the," "is," "a") are removed to highlight meaningful words like player names, actions, and game events.  

---

 📂 **Files in this Folder**  

| File Name        | Description                                        |
|-----------------|----------------------------------------------------|
| **solution.ipynb**  | Jupyter Notebook with the code for word cloud generation |
| **commentary.txt**  | Sample cricket commentary dataset |
| **output.png**      | Image of the generated word cloud |
| **README.md**       | Task description and details                  |

---

 📊 **Data Description**  
The dataset consists of **cricket commentary** text extracted from match broadcasts. The data includes:  

✔ **Player Names** – Mentions of batters, bowlers, and fielders.  
✔ **Match Events** – Sixes, fours, wickets, runs scored.  
✔ **Game Actions** – "Bowls," "hits," "drives," "edges," etc.  
✔ **Match Context** – Over numbers, run rates, partnerships.  

**Example Commentary Data:**  

```
"Sharma bowls a full-length delivery, Smith drives it through covers for four!"  
"Rabada to Kohli, short ball, pulled away for six over square leg!"  
"Ashwin flights it, Warner steps out and lofts it over long-on!"  
"Bumrah bowls a yorker, clean bowled! What a delivery!"  
```

---

**How to Use**  
1️⃣ **Download the files** or clone the repository.  
2️⃣ Open **solution.ipynb** in Jupyter Notebook.  
3️⃣ Run the code to:  
   - **Clean** the commentary by removing stop words.  
   - **Generate** a word frequency distribution.  
   - **Create** a **word cloud visualization**.  
4️⃣ View the **output.png** for insights into frequent words in the commentary.  

---
 **Key Learnings**  
✔ **Text Preprocessing** – Removing stop words and cleaning commentary text.  
✔ **Word Frequency Analysis** – Identifying the most mentioned words.  
✔ **Data Visualization** – Using **WordCloud & Matplotlib** to create a word cloud.  
✔ **Cricket Insights** – Understanding match trends through commentary analysis.  

---

  **Task 2: Commentary to Table**  

 📌 **Overview**  
This task extracts structured data from **cricket commentary** using **Regular Expressions (RegEx)**. The goal is to convert unstructured text into a **tabular format** with key match details such as **bowler name, batter name, ball type, shot type, ball speed, and runs scored**.  

---

📂 **Files in this Folder**  

| File Name        | Description                                        |
|-----------------|----------------------------------------------------|
| **solution.ipynb**  | Jupyter Notebook with the code for commentary extraction |
| **commentary.txt**  | Sample cricket commentary dataset |
| **output.csv**      | Extracted structured data in CSV format |
| **README.md**       | Task description and details                  |

---

📊 **Data Description**  
The dataset consists of **cricket match commentary**, which is processed to extract key information:  

✔ **Bowler Name** – The player who bowled the delivery.  
✔ **Batter Name** – The player facing the ball.  
✔ **Ball Type** – Yorker, bouncer, full toss, length ball, etc.  
✔ **Shot Type** – Boundary (six/four), single, defensive stroke.  
✔ **Ball Speed** – The speed of the delivery (in km/h).  
✔ **Runs Scored** – Number of runs from the ball.  

**Example Commentary Data:**  

```
"Sharma bowls a full-length delivery, Smith drives it through covers for four!"  
"Rabada to Kohli, short ball, pulled away for six over square leg!"  
"Ashwin flights it, Warner steps out and lofts it over long-on!"  
"Bumrah bowls a yorker at 145 km/h, clean bowled! What a delivery!"  
```

**Extracted Table Output:**  

| Bowler  | Batter | Ball Type | Shot Type | Speed (km/h) | Runs |
|---------|--------|-----------|-----------|--------------|------|
| Sharma  | Smith  | Full-length | Cover drive (4) | N/A  | 4  |
| Rabada  | Kohli  | Short ball  | Pull shot (6)  | N/A  | 6  |
| Ashwin  | Warner | Flighted    | Lofted shot (6) | N/A  | 6  |
| Bumrah  | N/A    | Yorker      | Bowled         | 145  | 0  |

---

**How to Use**  
1️⃣ **Download the files** or clone the repository.  
2️⃣ Open **solution.ipynb** in Jupyter Notebook.  
3️⃣ Run the code to:  
   - **Read** the commentary text file.  
   - **Use Regular Expressions (RegEx)** to extract key details.  
   - **Convert** extracted data into a structured table.  
4️⃣ Export the **output.csv** file for further analysis.  

---

 **Key Learnings**  
✔ **Natural Language Processing (NLP)** – Extracting structured data from cricket commentary.  
✔ **Regular Expressions (RegEx)** – Identifying patterns in text to extract key details.  
✔ **Data Structuring** – Converting unstructured commentary into a tabular format.  
✔ **Cricket Insights** – Understanding match events through extracted data.  

---

  **Task 3: Text Pre-processing & Feature Extraction using scikit-learn**  

📌 **Overview**  
This task demonstrates **text pre-processing methods** using **scikit-learn**, focusing on two feature extraction techniques:  
1️⃣ **CountVectorizer()** – Converts text into a matrix of token counts.  
2️⃣ **TfidfVectorizer()** – Converts text into a matrix of TF-IDF (Term Frequency-Inverse Document Frequency) scores.  

These methods help in transforming raw text into numerical vectors, enabling machine learning models to process and analyze textual data.  

---

📂 **Files in this Folder**  

| File Name        | Description                                        |
|-----------------|----------------------------------------------------|
| **solution.ipynb**  | Jupyter Notebook with the code for text vectorization |
| **text_data.txt**   | Sample text dataset for feature extraction |
| **output.csv**      | Extracted text features in a structured format |
| **README.md**       | Task description and details                  |

---

 📊 **Data Description**  
The dataset consists of **text samples** that are processed using **CountVectorizer() and TfidfVectorizer()**.  

**Example Text Data:**  

```
"The quick brown fox jumps over the lazy dog."
"Natural Language Processing is an exciting field in AI."
"Machine Learning models require numerical feature extraction."
"Feature extraction methods convert text into useful representations."
```

**Feature Extraction Methods:**  

✔ **CountVectorizer()** – Converts text into a matrix representing word frequency.  
✔ **TfidfVectorizer()** – Converts text into numerical values based on word importance.  

---

**How to Use**  
1️⃣ **Download the files** or clone the repository.  
2️⃣ Open **solution.ipynb** in Jupyter Notebook.  
3️⃣ Run the code to:  
   - **Load the text dataset.**  
   - **Apply CountVectorizer()** to extract word counts.  
   - **Apply TfidfVectorizer()** to extract TF-IDF features.  
   - **Store the output as a structured dataset (CSV format).**  
4️⃣ Analyze the **output.csv** to observe the extracted features.  

---

 **Key Learnings**  
✔ **Text Pre-processing** – Tokenization, normalization, and feature extraction.  
✔ **Feature Engineering** – Converting text data into structured numerical form.  
✔ **Scikit-learn NLP Tools** – Using **CountVectorizer** and **TfidfVectorizer** effectively.  
✔ **Machine Learning Readiness** – Preparing text data for ML models.  

---

  **Task 4: Implementing TF-IDF from Scratch on Cricket Commentary**  

 📌 **Overview**  
This task implements **TF-IDF (Term Frequency-Inverse Document Frequency) from scratch** using pure Python, **without using scikit-learn**. The goal is to extract important words from a **cricket commentary dataset** and convert them into numerical features for further analysis.  

TF-IDF is a key technique in **Natural Language Processing (NLP)**, used to evaluate how important a word is in a document relative to a collection of documents (corpus).  

---

📂 **Files in this Folder**  

| File Name        | Description                                        |
|-----------------|----------------------------------------------------|
| **solution.ipynb**  | Jupyter Notebook with the code for TF-IDF computation |
| **commentary.txt**  | Sample cricket commentary dataset |
| **output.csv**      | Extracted TF-IDF values for words in the dataset |
| **README.md**       | Task description and details                  |

---
 📊 **Data Description**  
The dataset consists of **cricket match commentary**, which is processed to compute TF-IDF values for each word.  

**Example Commentary Data:**  

```
"Sharma bowls a full-length delivery, Smith drives it through covers for four!"  
"Rabada to Kohli, short ball, pulled away for six over square leg!"  
"Ashwin flights it, Warner steps out and lofts it over long-on!"  
"Bumrah bowls a yorker at 145 km/h, clean bowled! What a delivery!"  
```
---

 **How to Use**  
1️⃣ **Download the files** or clone the repository.  
2️⃣ Open **solution.ipynb** in Jupyter Notebook.  
3️⃣ Run the code to:  
   - **Read the commentary dataset.**  
   - **Preprocess text** (tokenization, stopword removal, stemming).  
   - **Compute TF, IDF, and TF-IDF scores** manually using Python.  
   - **Store the extracted word features** in a structured format (CSV).  
4️⃣ Export **output.csv** for further analysis.  

---

 **Key Learnings**  
✔ **Manual TF-IDF Implementation** – No external libraries like scikit-learn.  
✔ **Text Preprocessing** – Cleaning cricket commentary text for analysis.  
✔ **Mathematical Understanding** – Learning **TF, IDF, and TF-IDF calculations**.  
✔ **Cricket Insights** – Identifying the most important words in match commentary.  

---
