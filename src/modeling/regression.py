from src.paths import MODELS
import os
import joblib

def regression_pred(amp, freq):
    path = os.path.join(MODELS, "regression.pkl") 
    
    model = joblib.load(path)
    
    return model.predict([[amp,freq]])