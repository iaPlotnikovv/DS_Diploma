from src.paths import MODELS
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import os
import joblib

def nn_predict(amp,freq):
    preprocessor_path = os.path.join(MODELS, "nn_preprocessor.pkl") 
    model_path = os.path.join(MODELS, "nn_clf.keras") 
    
    preprocessor= joblib.load(preprocessor_path)
    nn_clf= load_model(model_path)
    
    layers=np.arange(4,13)
    
    X_raw= pd.DataFrame({
        "Layer":layers,
        "Amp":[amp]*len(layers),
        "FreQ":[freq]*len(layers),
         }
    )
    X_transformed = preprocessor.transform(X_raw)
    

    probas = nn_clf.predict(X_transformed)
    #print(probas)
    for i, prob in enumerate(probas):
       label = int(prob>0.5)
       result = {1:"годно",0:"негодно"}
    
       
       print(f"Слой {layers[i]}: вероятность успеха {100*prob[0]:.2f} % ({result[label]})")

    
    
        