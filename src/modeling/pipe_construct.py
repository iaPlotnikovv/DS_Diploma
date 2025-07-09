from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score 
from sklearn.metrics import root_mean_squared_error



class PipeConstruct(Pipeline):
   
    def __init__(self, set_scaler, set_model, *, memory = None, verbose = False):
        self.set_scaler = set_scaler
        self.set_model = set_model
        steps = [
            ("scaler", set_scaler),
            ("model", set_model)
        ]
        super().__init__(steps=steps, memory=memory, verbose=verbose)

    def cross_validation(self, X_train, y_train, cv):
        scores = -1*cross_val_score(self,
                         X_train,
                         y_train,
                         scoring="neg_mean_absolute_error", 
                         cv=cv,
                         n_jobs=-1)
        print(f"Cross-validation Average MAE: {scores.mean():.2f}\n")

    
    def error_score(self, X_test, y_test):
        predicts = super().predict(X_test)
        r2=r2_score(y_test,predicts)
        rmse = root_mean_squared_error(y_test,predicts)
        
        print(f"MAE: {mean_absolute_error(y_test,predicts):.2f}")
        print(f"RMSE: {rmse:.2f}")
        print(f"Коэффициент детерминации: {r2:.2f}\n")
        
        
        
        