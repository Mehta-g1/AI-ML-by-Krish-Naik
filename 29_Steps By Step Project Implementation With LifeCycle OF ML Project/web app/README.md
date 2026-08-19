# FWI Prediction Web App

This project is a Flask web application for predicting the Fire Weather Index (FWI) using a trained machine learning model.

## Project Overview

The app accepts weather and fire-related inputs from the user, passes them to a saved trained model, and displays the predicted FWI value on the webpage.

## Tech Stack

- Python
- Flask
- scikit-learn
- pandas
- NumPy
- Pickle
- HTML / Jinja Templates

## Project Structure

```text
web app/
├── application.py
├── models/
│   ├── linreg.pkl
│   └── scaler.pkl
├── notebooks/
├── templates/
│   ├── home.html
│   └── index.html
├── README.md
└── requirements.txt   (if present in parent project)
```

## Features

- User input form for fire risk parameters
- Data preprocessing using saved StandardScaler
- Prediction using saved trained model
- Display of input values and predicted result

## How to Run

1. Open terminal in the `web app` folder.
2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r ..\requirements.txt
```

4. Run the app:

```bash
python application.py
```

5. Open the browser and visit:

```text
http://127.0.0.1:5000/
```

## Important Notes

- The app loads the trained model and scaler from the `models` folder.
- Ensure the model files exist before running the application.
- The route `/predictdata` handles the prediction form submission.

## Model Files

The application uses:

- `models/linreg.pkl` → trained regression model
- `models/scaler.pkl` → saved StandardScaler for feature scaling

## Future Improvements

- Add validation for numeric input
- Improve UI design
- Add error handling for invalid values
- Deploy to Render / Heroku / Railway / Azure

## License

This project is for learning and demonstration purposes.
