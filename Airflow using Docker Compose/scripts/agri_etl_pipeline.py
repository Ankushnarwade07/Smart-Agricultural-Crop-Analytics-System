import pandas as pd
import pickle

print("🚀 Starting ETL...")

data = pd.read_csv("/opt/airflow/data/Crop_recommendation.csv")
data = data.dropna()

with open("/opt/airflow/models/crop_recommendation_pipeline_colab.pkl", "rb") as f:
    model = pickle.load(f)

pred = model.predict(data.drop(columns=["label"]))
pd.DataFrame({"Predicted_Label": pred}).to_csv("/opt/airflow/data/agri_predictions_airflow.csv", index=False)

print("✅ ETL completed successfully!")