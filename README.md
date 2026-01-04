# 🌍 Air Quality Index (AQI) Dashboard

An interactive **Air Quality Index (AQI) Dashboard** built using **Streamlit** and **Pandas** to visualize air pollution data across different countries with geographical mapping and filters.

---

## 🚀 Features

- 📄 Dataset preview
- 📊 Descriptive statistics
- 🔎 AQI range filter (interactive sidebar)
- 🗺️ Geographical AQI visualization using latitude & longitude
- 📈 AQI distribution chart (Streamlit native charts)
- ⚡ Fast loading with caching
- ☁️ Cloud-safe (no matplotlib / seaborn dependency issues)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**

---

## 📂 Project Structure

aqi/
├── app.py
├── requirements.txt
├── AQI-and-Lat-Long-of-Countries (1).csv
└── README.md

yaml
Copy code

---

## 📦 Installation (Local Setup)

1. Clone the repository:
```bash
git clone https://github.com/your-username/aqi-dashboard.git
cd aqi-dashboard
Install dependencies:

bash
Copy code
python -m pip install -r requirements.txt
Run the app:

bash
Copy code
python -m streamlit run app.py
