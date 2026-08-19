# FWI Prediction Web App

This project is a Flask web application that predicts the Fire Weather Index (FWI) using a trained regression model.

## Live App

The app is live here:

https://fwi.pythonanywhere.com/predictdata

## Project Overview

The model takes weather and environmental input values and predicts the FWI value for fire risk assessment. The app uses a saved machine learning model and scaler that were trained during the project workflow.

## Tech Stack

- Python
- Flask
- pandas
- NumPy
- scikit-learn
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
├── requirements.txt
└── .gitignore
```

## Features

- User-friendly web form for fire weather inputs
- Feature scaling using a saved StandardScaler
- Prediction using a saved trained regression model
- Input and output display on the webpage
- Easy testing using sample values from the dataset

## Model Performance

This is a regression problem, so the notebook reports metrics such as MAE, MSE, RMSE and R².

From the notebook experiments, the best-performing models showed strong results:

- Ridge Regression: MAE ≈ 0.5192, R² ≈ 0.9801
- Linear Regression: MSE ≈ 0.5050, R² ≈ 0.9806
- Lasso Regression: MAE ≈ 1.0094, R² ≈ 0.9431

These values indicate the model is performing very well for predicting the FWI value on this dataset.

## Dataset Examples for Testing

Below are representative rows from the cleaned dataset that can be used to test the model in the web app.

| Row | Temperature | RH | Ws | Rain | FFMC | DMC | DC | ISI | BUI | FWI | Classes | Region |
|-----|-------------|----|----|------|------|-----|----|-----|-----|-----|---------|--------|
| 1 | 29 | 57 | 18 | 0.0 | 65.7 | 3.4 | 7.6 | 1.3 | 3.4 | 0.5 | not fire | 0 |
| 2 | 29 | 61 | 13 | 1.3 | 64.4 | 4.1 | 7.6 | 1.0 | 3.9 | 0.4 | not fire | 0 |
| 3 | 26 | 82 | 22 | 13.1 | 47.1 | 2.5 | 7.1 | 0.3 | 2.7 | 0.1 | not fire | 0 |
| 4 | 25 | 89 | 13 | 2.5 | 28.6 | 1.3 | 6.9 | 0.0 | 1.7 | 0.0 | not fire | 0 |
| 5 | 27 | 77 | 16 | 0.0 | 64.8 | 3.0 | 14.2 | 1.2 | 3.9 | 0.5 | not fire | 0 |
| 6 | 31 | 67 | 14 | 0.0 | 82.6 | 5.8 | 22.2 | 3.1 | 7.0 | 2.5 | fire | 0 |
| 7 | 33 | 54 | 13 | 0.0 | 88.2 | 9.9 | 30.5 | 6.4 | 10.9 | 7.2 | fire | 0 |
| 8 | 30 | 73 | 15 | 0.0 | 86.6 | 12.1 | 38.3 | 5.6 | 13.5 | 7.1 | fire | 0 |
| 9 | 25 | 88 | 13 | 0.2 | 52.9 | 7.9 | 38.8 | 0.4 | 10.5 | 0.3 | not fire | 0 |
| 10 | 28 | 79 | 12 | 0.0 | 73.2 | 9.5 | 46.3 | 1.3 | 12.6 | 0.9 | not fire | 0 |
| 11 | 31 | 65 | 14 | 0.0 | 84.5 | 12.5 | 54.3 | 4.0 | 15.8 | 5.6 | fire | 0 |
| 12 | 26 | 81 | 19 | 0.0 | 84.0 | 13.8 | 61.4 | 4.8 | 17.7 | 7.1 | fire | 0 |
| 13 | 27 | 84 | 21 | 1.2 | 50.0 | 6.7 | 17.0 | 0.5 | 6.7 | 0.2 | not fire | 0 |
| 14 | 30 | 78 | 20 | 0.5 | 59.0 | 4.6 | 7.8 | 1.0 | 4.4 | 0.4 | not fire | 0 |
| 15 | 28 | 80 | 17 | 3.1 | 49.4 | 3.0 | 7.4 | 0.4 | 3.0 | 0.1 | not fire | 0 |
| 16 | 29 | 89 | 13 | 0.7 | 36.1 | 1.7 | 7.6 | 0.0 | 2.2 | 0.0 | not fire | 0 |
| 17 | 30 | 89 | 16 | 0.6 | 37.3 | 1.1 | 7.8 | 0.0 | 1.6 | 0.0 | not fire | 0 |
| 18 | 31 | 78 | 14 | 0.3 | 56.9 | 1.9 | 8.0 | 0.7 | 2.4 | 0.2 | not fire | 0 |
| 19 | 31 | 55 | 16 | 0.1 | 79.9 | 4.5 | 16.0 | 2.5 | 5.3 | 1.4 | not fire | 0 |
| 20 | 30 | 80 | 16 | 0.4 | 59.8 | 3.4 | 27.1 | 0.9 | 5.1 | 0.4 | not fire | 0 |

Note: in the trained model, the `Classes` column is encoded as numeric values (`0` for not fire, `1` for fire).

## How to Run Locally

1. Open a terminal inside the `web app` folder.
2. Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
python application.py
```

5. Open in the browser:

```text
http://127.0.0.1:5000/
```

## Important Notes

- The app loads the saved model and scaler from the `models` folder.
- The trained files must be present before running the application.
- The main prediction route is `/predictdata`.
- This project is intended for educational and demonstration purposes.

## Model Files Used

- `models/linreg.pkl` → trained regression model
- `models/scaler.pkl` → saved StandardScaler used for feature scaling

## Future Improvements

- Add stronger input validation
- Improve the user interface
- Add CSV upload support
- Deploy with Docker or cloud hosting
- Add model comparison charts in the UI

## License

This project is for learning and demonstration purposes.
