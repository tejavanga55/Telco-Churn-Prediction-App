# Telco Customer Churn Prediction – Mini ML Project (Student Setup Guide)

## 1. Download the Project ZIP File
1. Download the ZIP file from Teams.
2. Move it to Desktop.
3. Right-click → Extract All.
4. You will see:

```
Churn_Project/
    ├── Telco-Customer-Churn.csv
    ├── train_churn_model.ipynb
    ├── app.py
    ├── streaming_churn_model.pkl
    ├── scaler.pkl
    ├── encoder.pkl
```

---

## 2. Install Python
Run:
```
python --version
```

Install Python 3.10 or 3.11 if missing.

---

## 3. Open the Project in VS Code
1. Open VS Code  
2. File → Open Folder  
3. Select the extracted folder  

---

## 4. Create Virtual Environment
```
python -m venv .venv
```

Activate:

Windows:
```
.venv\Scripts\activate
```

Mac:
```
source .venv/bin/activate
```

---

## 5. Install Required Libraries
```
pip install pandas numpy scikit-learn streamlit matplotlib
```

---

## 6. Run Training Notebook (Optional)
Open `train_churn_model.ipynb` → run cells.

This saves:
```
streaming_churn_model.pkl
scaler.pkl
encoder.pkl
```

---

## 7. Run Streamlit App
```
streamlit run app.py
```

Opens:
```
http://localhost:8501
```

---

## 8. Common Issues

### Missing module
```
pip install <module>
```

### Streamlit not found
```
pip install streamlit
```

### Feature mismatch  
Retrain the model.

---

## 9. Expected Folder Structure
```
Churn_Project/
    ├── Telco-Customer-Churn.csv
    ├── train_churn_model.ipynb
    ├── app.py
    ├── streaming_churn_model.pkl
    ├── scaler.pkl
    ├── encoder.pkl
    ├── README.md
    └── .venv/
```

---

## You are ready to begin the project! 🎉
