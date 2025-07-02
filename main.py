import click 
from src.modeling.regression import regression_pred

@click.command()
def main():
    print("Hello world!")
    
@click.command()
@click.option('--amp', required=True, type=float, help='Амплитуда (Amp)')
@click.option('--freq', required=True, type=float, help='Частота (FreQ)')
def cli(amp,freq):
    predict = regression_pred(amp, freq)
    print (f"\nПредсказанная ширина валика: e = {predict[0]:.2f} мм\n")
    



if __name__=="__main__":
    cli()
