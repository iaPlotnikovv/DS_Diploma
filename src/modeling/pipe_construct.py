from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error



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
                         cv=cv)
        print(f"Cross-validation Average MAE: {scores.mean()}")

    
    def mae(self, X_test, y_test):
        predicts = super().predict(X_test)
        print(f"MAE: {mean_absolute_error(y_test,predicts)}")
        