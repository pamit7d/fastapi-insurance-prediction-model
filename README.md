# Insurance Premium Prediction App

A full-stack machine learning application that predicts insurance premium categories based on user details. The project consists of a **FastAPI** backend for serving predictions and a **Streamlit** frontend for the user interface.

## 🚀 Features

- **Machine Learning Model**: Random Forest Classifier trained on insurance data.
- **REST API**: FastAPI backend aimed at high performance.
- **Interactive UI**: Streamlit-based web interface for easy predictions.
- **Smart Logic**: Calculates BMI, Age Groups, and Lifestyle Risk automatically.
- **Deployment Ready**: Configured for Vercel (Backend) and Streamlit Cloud (Frontend).

## 🛠️ Tech Stack

- **Python 3.x**
- **FastAPI** (Backend Framework)
- **Streamlit** (Frontend Framework)
- **Scikit-learn** (Machine Learning)
- **Pandas** (Data Processing)

## 📂 Project Structure

```bash
├── app.py              # FastAPI Backend Application
├── frontend.py         # Streamlit Frontend Application
├── train_model.py      # Script to train and save the model
├── model.pkl           # Trained Random Forest Model
├── insurance.csv       # Dataset used for training
├── vercel.json         # Vercel deployment configuration
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## ⚙️ Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd insurance
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Backend (FastAPI)**
   ```bash
   uvicorn app:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

5. **Run the Frontend (Streamlit)**
   open a new terminal and run:
   ```bash
   streamlit run frontend.py
   ```
   The app will open in your browser at `http://localhost:8501`.

## 🌐 Deployment

### Backend (Render)
1. Push code to GitHub.
2. Sign up on [Render](https://render.com/).
3. Create a **New Web Service**.
4. Connect your GitHub repository.
5. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Deploy.
7. Copy the deployed URL (e.g., `https://your-app.onrender.com`).

### Frontend (Streamlit Cloud)
The frontend is optimized for Streamlit Cloud.
1. Sign up on [Streamlit Cloud](https://share.streamlit.io/).
2. Create **New App** and select your repository.
3. **Advanced Settings**:
   - Add a secret/environment variable:
     - `API_URL` = `https://your-app.onrender.com/predict` (Replace with your Render URL).
4. Deploy.

## 📡 API Reference

### POST `/predict`

Predicts the insurance premium category.

**Request Body:**
```json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "response": "Low"
}
```
