import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


class SquareFunction():
    
    
    def __init__(self):
        pass
    
    
    def graph(self, scalar):
        
        
        fig, ax = plt.subplots(figsize=(15, 10))
        x = np.linspace(-10, 10, 1000)
        y = scalar*x
        ax.plot(x, y)
        
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')

        # remove the ticks from the top and right edges
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        fig.savefig('app/static/images/square_function_transform.png')






