import matplotlib.pyplot as plt
import numpy as np


class Geometric():
    
    
    def __init__(self):
        self.name = 'geo'
        
        
    def graph(self):
        
        x = np.linspace(0, 1, 1000)
        y = x**2
        fig, ax = plt.subplots(figsize=(15, 10))
        ax.plot(x, y)
        fig.savefig('static/images/geometric.png')