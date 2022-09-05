import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class GeometricSeries():
    
    
    def __init__(self):
        pass
        
        
    def graph(self, r, a, epsilon, large_m):
        
        
        # We will plot the powers list as our domain, and we will plot the
        # results list as our range
        results = []
        powers = []
    
    
        # We initiate the power variable at 0
        power = 0
        powers.append(power)
    
    
        # We initiate the result variable at 0, for the purposes of initiating
        # the absolute value of difference of two adjacent result terms, as
        # seen below in the while loop
        prev_result = 0
    
    
        # Since we do not wish to plot a value of 0, we omit this entry from
        # our graph
        results.append(np.nan)
    
    
        # This loop will fill our powers and results lists until the if
        # conditional within evaluates to True.
        # The conditions in the first if statement below are not
        # a set of conditions necessary for the mathematical function,
        # but rather a set of conditions necessary to accomodate the author's
        # inability to produce an alternative for comparing a sum of the
        # function's terms with the chosen epsilon.
        # ----------------------------------------------------------------------
        # Example to motivate the first if statement:
        # if power!=0 and power-large_m!=0 and power%large_m==0
        # Let large_m=10 and power=20.
        # if 20 is not 0 (check)
        # and if 20 minus 10 is not 0 (check)
        # and if 20 in base 10 is 0 (check)
        # ----------------------------------------------------------------------
        flag = True
        while flag:
            curr_result = a*r**(power)
            if power!=0 and power-large_m!=0 and power%large_m==0:
                if abs(sum(results[power-large_m:power-1])) < epsilon:
                    flag = False
                    continue
            results.append(curr_result)
            prev_result = curr_result
            power += 1
            powers.append(power)
        
        
        # The statements below will plot the powers and results list that we
        # have from the above while loop, completing the graph of our function
        fig, ax = plt.subplots(figsize=(15, 10))
        ax.scatter(powers, results, label=r'$af(r)=\sum_{i=0}^{\infty}ar^i$')
        plt.xlabel('Integer Powers', fontsize=20)
        plt.ylabel('Sequence Value', fontsize=20)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        fig.suptitle('Geometric Series', fontsize=20)
        plt.legend(prop={'size': 20})
        fig.savefig('app/static/images/geometric_series.png')

