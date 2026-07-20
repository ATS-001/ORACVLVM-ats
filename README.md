# ORACVLVM 
# FIFA World Cup Performance Forecaster

An end-to-end **Machine Learning web application** designed as an interactive decision support tool to simulate and predict the statistical probability of national football squads reaching the tournament Quarter-Finals. By leveraging a trained **Random Forest Classifier Ensemble**, the system evaluates core team dynamics, squad valuations, and historical metrics to generate predictive analytics instantly.

---

## 📋 Features
- **Team Attributes:** Tracks whether a country acts as the tournament host.
- **Historical Performance:** Analyzes goals scored and conceded over the trailing 4-year cycle.
- **Tournament Experience:** Evaluates total historical FIFA World Cup participations.
- **Squad Quality Metrics:** Incorporates current official FIFA Ranks, accumulated FIFA points, squad average age, and aggregate squad market value (€).
- **Interface Buffers:** Built-in systemic "Clear / Reset Inputs" state memory management for continuous simulations.
- **Sleek UX UI:** Terminal-inspired Courier New styling with custom CSS modifications hiding default platform hotbars.

---

## 📊 How It Works
1. **Input:** Users calibrate custom tournament team matrices directly through the workspace sliders and numeric input slots.
2. **Evaluation:** The underlying Random Forest ensemble evaluates the input data mapping array against strict historical feature hierarchies.
3. **Output:** The interface prints the final knockout qualification forecast alongside custom system status configurations.

---

## 🖥️ Website
- **Deployed using:** Streamlit Cloud
- **Link:** *[Click here](https://oracvlvm-ats.streamlit.app/)*

## 🛠 Technology Stack
- **Interface Engine:** Streamlit
- **ML Architecture:** Random Forest Classifier (Ensemble Learning)
- **Model Baseline Accuracy:** 69.23%
- **Metadata Context:** LLM Hub Pipeline mapping reference via local indices

---

## 📅 Workshop Context
**Day 6 of Projectathon conducted by μLearn LBSITW, AI x DS (3rd July 2026)** - **Presented by:** *Aiswarya Jayaprakash, Data Science IG Lead, µLearn LBSITW* 

### Core Concepts Mastered
- **Supervised Classification:** Tuning multi-tree ensembles to output valid probability distributions (`predict_proba`).
- **Feature Engineering Alignment:** Constructing array inputs matching precise pipeline parameters.
- **Session State Control:** Maintaining interface forms clean without disrupting local object variables.

---

## 🛠️ Machine Learning Pipeline Architecture
1. **Feature Hierarchy Extraction**
   - Tracked 8 unique core metrics across historical evaluation groups (2002–2022 dataset arrays).
2. **Probability Scaling**
   - Implemented standard mapping algorithms to parse predictive indices instead of hard single class configurations (`0` or `1`).
3. **Artifact Serialization**
   - Exported the complete trained ensemble pipeline down to a serialized `world_cup_model.pkl` binary matrix using `joblib`.

---

## 📁 Repository Directory Structure
```text
├── app.py                     # Rebranded Streamlit terminal dashboard
├── world_cup_model.pkl        # Serialized Random Forest model binary
├── requirements.txt           # Python ecosystem deployment dependencies
└── README.md                  # Comprehensive repository documentation
```

## 🚀 Local Installation & Deployment

1. **Clone this repository:**
   ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/oracvlvm.git](https://github.com/YOUR_GITHUB_USERNAME/oracvlvm.git)
    cd oracvlvm
   ```

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🔮 Acknowledgments & Data Attributions

- **Data Ownership & Trademarks:** All historical tournament data, rankings, scoring records, and branding attributes associated with the "FIFA World Cup" are the exclusive intellectual property of **FIFA (Fédération Internationale de Football Association)**. 
- **Application Context:** This system is an independent machine learning project built purely for educational analytics and research benchmarking during the μLearn LBSITW Projectathon; it is not officially endorsed by or affiliated with FIFA.

Special thanks to **Aishwarya Jayaprakash** ([Github](https://github.com/Aiswarya-Jayaprakash)) for the baseline pipeline code, structural guidelines, and workshop instruction that enabled this end-to-end model and deployment.

---

### 👨‍💻 Developer Profile
* **Name:** Aaron Thalakkottor Sooraj
* **Degree:** B.Tech in Computer Science Engineering (CSE)
* **Institution:** Vidya Academy of Science and Technology, Thrissur

---

### 📜 License
```text
COPYRIGHT © Since 2023 ATS-PDZ - ALL RIGHTS RESERVED.
```

