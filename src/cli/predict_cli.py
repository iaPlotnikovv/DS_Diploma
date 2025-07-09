import click 
from src.modeling.regression import regression_pred
from src.modeling.classification import nn_predict

@click.command()
@click.option('-a','--amp', required=True, type=float, help='Амплитуда (Amp)')
@click.option('-f','--freq', required=True, type=float, help='Частота (FreQ)')
def cli(amp,freq):
                
    predict_width = regression_pred(amp, freq)
    
    print (f"\nПредсказанная ширина валика: e = {predict_width[0]:.2f} мм\n")
    
    nn_predict(amp,freq)
    