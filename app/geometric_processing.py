import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class Geometric():
    
    
    def __init__(self):
        pass
        
        
    def graph(self, lower, upper):
        
        x = np.linspace(lower, upper, 1000)
        y = x**2
        fig, ax = plt.subplots(figsize=(15, 10))
        ax.plot(x, y)
        fig.savefig('app/static/images/geometric.png')