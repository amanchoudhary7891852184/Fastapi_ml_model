# Kidney Stone Prediction API 🔬🩺

**A small FastAPI service that predicts the presence of kidney stones from urine measurements using a pre-trained ML model.**

---

## 🚀 Features
- **REST API** built with **FastAPI**
- Predicts kidney stone presence from urine features
- Includes input validation with Pydantic schemas
- Model/scaler loading from pickled files

---

## 📁 Project structure (key files)
- `app.py` — FastAPI app (routes: `GET /`, `POST /predict`)
- `model_loader.py` — Loads `kidney_stone_best_model.pkl` and `scaler.pkl`, runs prediction
- `schemas.py` — Pydantic models: `UrineInput`, `PredictionOutput`
- `model.ipynb` — Notebook for training / exploration
- `kindey stone urine analysis.csv` — dataset (note: filename in repo)
- `requriments.txt` — project dependencies (note the filename typo in the repo)

---

## 💻 Requirements
- Python 3.8+
- Install dependencies:
```bash
python -m venv myenv
# Windows (PowerShell)
myenv\Scripts\Activate.ps1
pip install -r requriments.txt
```
> ⚠️ Note: The requirements file in the repository is named `requriments.txt` (misspelled). Use that name or rename it if you prefer.

---

## ▶️ Running the app (development)
Ensure the model artifacts `kidney_stone_best_model.pkl` and `scaler.pkl` are in the project root.

- Activate your venv (Windows examples):
  - PowerShell:
    ```powershell
    myenv\Scripts\Activate.ps1
    ```
  - CMD:
    ```cmd
    myenv\Scripts\activate.bat
    ```

- Start the server (development with auto-reload):
```bash
# cross-platform
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000

# or
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

- After starting:
  - Interactive docs: http://127.0.0.1:8000/docs
  - Health: `GET /` → `{ "message": "Kidney Stone Prediction API is running" }`

---

## 🔁 API: Predict
- Endpoint: `POST /predict`
- Request body (JSON) — fields are required:
```json
{
  "gravity": 1.01,
  "ph": 6.5,
  "osmo": 300,
  "cond": 0.5,
  "urea": 30,
  "calc": 8
}
```
- Response example:
```json
{
  "prediction": 1,
  "result": "Kidney Stone Detected"
}
```

---

## 🧾 Notes & Tips
- The service expects the pickled model and scaler named exactly `kidney_stone_best_model.pkl` and `scaler.pkl`.
- You can test the API quickly using curl or the Swagger UI at `/docs`.
- The Pydantic schema enforces types and basic documentation for each field.

---

## ✍️ Contributing
- Feel free to open issues or submit PRs to improve model accuracy, add tests, or fix typos (e.g., `requriments.txt`).

---

## 📄 License
- Add your preferred license here (e.g., MIT). If you want, I can add a license file as well.
