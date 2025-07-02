from src.paths import MODELS
import os
import joblib

def save_model(model, name):
    
    modelpath=os.path.join(MODELS,name)

    joblib.dump(model,modelpath)