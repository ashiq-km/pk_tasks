# Setup Instructions

This document explains how to set up and run the project locally, with a focus on **Task 4: Model Deployment using FastAPI**.

The repository contains multiple tasks. Only **Task_2** and **Task_4** are required for deployment.

---

## Repository Structure (Relevant Parts)

```
.
├── Task_1/
│   └── requirements.txt        # Not required for deployment
│
├── Task_2/
│   ├── notebooks/
│   │   └── cnn_cifar10.ipynb
│   ├── models/
│   │   └── best_model.keras    # Trained CNN model
│   └── requirements.txt        # Dependencies for training & inference
│
├── Task_4/
│   └── main.py                 # FastAPI application
│
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 1. Clone the Repository

```bash
git clone https://github.com/ashiq-km/pk_tasks.git
cd pk_tasks
```

---

## 2. Create and Activate Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate the environment

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\\Scripts\\activate
```

---

## 3. Install Dependencies

The deployment uses the same dependencies as Task 2 (model training and inference).

Install requirements from **Task_2**:

```bash
pip install -r Task_2/requirements.txt
```

> Note: `Task_1/requirements.txt` is not required for deployment.

---

## 4. Verify Model Availability

Ensure the trained model exists at the following path:

```
Task_2/models/best_model.keras
```

This model is loaded automatically when the FastAPI application starts.

---

## 5. Run the FastAPI Application

From the **project root directory**, run:

```bash
uvicorn Task_4.app.main:app --reload
```

If successful, you should see output similar to:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 6. Access API Documentation (Swagger UI)

Open your browser and navigate to:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows interactive testing of all available endpoints.

---

## 7. Available API Endpoints

| Endpoint   | Method | Description                            |
| ---------- | ------ | -------------------------------------- |
| `/`        | GET    | Home endpoint to verify API is running |
| `/health`  | GET    | Health check endpoint                  |
| `/predict` | POST   | Upload an image and receive prediction |

---

## 8. Using the `/predict` Endpoint

* Upload an image file (JPG or PNG)
* The image is resized internally to **32 × 32**
* The API returns:

  * Predicted class label
  * Confidence score

Example response:

```json
{
  "predicted_class": "Frog",
  "confidence": 0.82
}
```

---

## Notes

* The model is trained on the **CIFAR-10** dataset.
* Predictions on images outside the CIFAR-10 distribution may result in lower confidence.
* Confidence values can be used as a heuristic to identify uncertain or potentially incorrect predictions.

---

End of setup instructions.
