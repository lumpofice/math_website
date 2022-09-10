import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


class PolynomialDegree2Transform():
    
    
    def __init__(self):
        pass
    
    
    def graph(self, h, x_scalar, y_scalar, k):
        
        # h: Horizontal shift on the argument
        # x_scalar: Reflective/Non-reflective scalar on the argument
        # and the horizontal shift
        # y_scalar: Reflective/Non-reflective scalar on the function value
        # before the vertical shift
        # k: Vertical Shift the function value
        
        # Setting up the graph before plotting
        fig, ax = plt.subplots(figsize=(15, 10))
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
            
        # Plotting the functions
        flag = True
        while flag:
            
            if y_scalar == 0:
                x = np.linspace(-10, 10, 1000)
                y_parent = x**2
                ax.plot(x, y_parent, label='Parent')
                flag = False
                break
        
            elif x_scalar == 0:
                x = np.linspace(-10, 10, 1000)
                y_parent = x**2
                ax.plot(x, y_parent, label='Parent')
                flag = False
                break
            
            else:
                if x_scalar != 1:
                
                    if h != 0:
                
                        if h/x_scalar < 0:
                            x = np.linspace((h/x_scalar)-10, 10, 1000)
                            y_parent = x**2
                            y_transform = y_scalar*(\
                            x_scalar*(x-(h/x_scalar)))**2 + k
                            ax.plot(x, y_parent, label='Parent')
                            ax.plot(x, y_transform, label='Transform')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h/x_scalar
                            b_1 = y_scalar*(\
                            x_scalar*(a_1-(h/x_scalar)))**2 + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({0:.2g}, {0:.2g})'.format(a_1, b_1))
        
                            a_2 = (h/x_scalar)-0.5
                            b_2 = y_scalar*(\
                            x_scalar*(a_2-(h/x_scalar)))**2 + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({0:.2g}, {0:.2g})'.format(a_2, b_2))
                
                            a_3 = (h/x_scalar)+0.5
                            b_3 = y_scalar*(\
                            x_scalar*(a_3-(h/x_scalar)))**2 + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({0:.2g}, {0:.2g})'.format(a_3, b_3))
                            
                            flag = False
                            break
            
                        elif h/x_scalar > 0:
                            x = np.linspace(-10, (h/x_scalar)+10, 1000)
                            y_parent = x**2
                            y_transform = y_scalar*(x_scalar*(\
                            x-(h/x_scalar)))**2 + k
                            ax.plot(x, y_parent, label='Parent')
                            ax.plot(x, y_transform, label='Transform')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h/x_scalar
                            b_1 = y_scalar*(\
                            x_scalar*(a_1-(h/x_scalar)))**2 + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({0:.2g}, {0:.2g})'.format(a_1, b_1))
        
                            a_2 = (h/x_scalar)-0.5
                            b_2 = y_scalar*(\
                            x_scalar*(a_2-(h/x_scalar)))**2 + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({0:.2g}, {0:.2g})'.format(a_2, b_2))
                
                            a_3 = (h/x_scalar)+0.5
                            b_3 = y_scalar*(\
                            x_scalar*(a_3-(h/x_scalar)))**2 + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({0:.2g}, {0:.2g})'.format(a_3, b_3))
                            
                            flag = False
                            break
                
                    else:
                        x = np.linspace(-10, 10, 1000)
                        y_parent = x**2
                        y_transform = y_scalar*(x_scalar*(x))**2 + k
                        ax.plot(x, y_parent, label='Parent')
                        ax.plot(x, y_transform, label='Transform')
                        
                        # Plotting labeled ordered pairs
                        a_1 = h/x_scalar
                        b_1 = y_scalar*(\
                        x_scalar*(a_1-(h/x_scalar)))**2 + k
                        ax.scatter(\
                        a_1, b_1,\
                        label='({0:.2g}, {0:.2g})'.format(a_1, b_1))
        
                        a_2 = (h/x_scalar)-0.5
                        b_2 = y_scalar*(\
                        x_scalar*(a_2-(h/x_scalar)))**2 + k
                        ax.scatter(\
                        a_2, b_2,\
                        label='({0:.2g}, {0:.2g})'.format(a_2, b_2))
                
                        a_3 = (h/x_scalar)+0.5
                        b_3 = y_scalar*(\
                        x_scalar*(a_3-(h/x_scalar)))**2 + k
                        ax.scatter(\
                        a_3, b_3,\
                        label='({0:.2g}, {0:.2g})'.format(a_3, b_3))
                        
                        flag = False
                        break
                
                else:
                    x = np.linspace(-10, 10, 1000)
                    y_parent = x**2
                    y_transform = y_scalar*(x-h)**2 + k
                    ax.plot(x, y_parent, label='Parent')
                    ax.plot(x, y_transform, label='Transform')
                    
                    # Plotting labeled ordered pairs
                    a_1 = h/x_scalar
                    b_1 = y_scalar*(\
                    x_scalar*(a_1-(h/x_scalar)))**2 + k
                    ax.scatter(\
                    a_1, b_1,\
                    label='({0:.2g}, {0:.2g})'.format(a_1, b_1))
        
                    a_2 = (h/x_scalar)-0.5
                    b_2 = y_scalar*(\
                    x_scalar*(a_2-(h/x_scalar)))**2 + k
                    ax.scatter(\
                    a_2, b_2,\
                    label='({0:.2g}, {0:.2g})'.format(a_2, b_2))
                
                    a_3 = (h/x_scalar)+0.5
                    b_3 = y_scalar*(\
                    x_scalar*(a_3-(h/x_scalar)))**2 + k
                    ax.scatter(\
                    a_3, b_3,\
                    label='({0:.2g}, {0:.2g})'.format(a_3, b_3))
                    
                    flag = False
                    break
        
        # Plotting labeled ordered pairs for the parent
        a_1 = 1
        b_1 = a_1**2
        ax.scatter(a_1, b_1, label='({0:.2g}, {0:.2g})'.format(a_1, b_1))
        
        a_2 = -1
        b_2 = a_2**2
        ax.scatter(a_2, b_2, label='({0:.2g}, {0:.2g})'.format(a_2, b_2))
        
        # Putting some restrictions and information on the graphing window
        plt.ylim(-10, 10)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=20)
        fig.suptitle('Polynomial Degree 2 Transform', fontsize=20)
        plt.legend(prop={'size': 20})
            
        # Saving the figure to the static folder
        fig.savefig(\
        'app/static/images/polynomial_degree_2_transform.png')






