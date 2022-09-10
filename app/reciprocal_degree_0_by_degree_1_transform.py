import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


class ReciprocalDegree0ByDegree1Transform():
    
    
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
                domain = np.arange(-10, 10.01, 0.01)
                            
                y_parent = 1/domain
                y_parent[y_parent>1000] = np.inf
                y_parent[y_parent<-1000] = np.inf
                            
                y_parent = np.array(y_parent)
                ax.plot(domain, y_parent, label=f'$f(x)=1/x$')
                flag = False
                break
            
            elif x_scalar == 0:
                domain = np.arange(-10, 10.01, 0.01)
                            
                y_parent = 1/domain
                y_parent[y_parent>1000] = np.inf
                y_parent[y_parent<-1000] = np.inf
                    
                y_parent = np.array(y_parent)
                ax.plot(domain, y_parent, label=f'$f(x)=1/x$')
                flag = False
                break
            
            else:
                if x_scalar != 1:
                
                    if h != 0:
                
                        if h/x_scalar < 0:
                            
                            domain = np.arange((h/x_scalar)-10, 10.01, 0.01)
                            
                            y_parent = 1/domain
                            y_parent[y_parent>1000] = np.inf
                            y_parent[y_parent<-1000] = np.inf
                            
                            y_transform = y_scalar*\
                            (1/(x_scalar*domain-(h/x_scalar))) + k
                            y_transform[y_transform>1000] = np.inf
                            y_transform[y_transform<-1000] = np.inf                            
                            
                            ax.plot(domain, y_parent, label=f'$f(x)=1/x$')
                            ax.plot(domain, y_transform,\
                            label=f'$g(x)={y_scalar}$'\
                            f'$(1/({x_scalar}x-({h}/{x_scalar}))) + {k}$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h/x_scalar-1
                            b_1 = y_scalar*\
                            (1/(x_scalar*a_1-(h/x_scalar))) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = (h/x_scalar)-0.5
                            b_2 = y_scalar*\
                            (1/(x_scalar*a_2-(h/x_scalar))) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = (h/x_scalar)+0.5
                            b_3 = y_scalar*\
                            (1/(x_scalar*a_3-(h/x_scalar))) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                            
                            flag = False
                            break
                            
                        elif h/x_scalar > 0:
                            domain = np.arange(-10, (h/x_scalar)+10.01, 0.01)
                            
                            y_parent = 1/domain
                            y_parent[y_parent>1000] = np.inf
                            y_parent[y_parent<-1000] = np.inf
                            
                            y_transform = y_scalar*\
                            (1/(x_scalar*domain-(h/x_scalar))) + k
                            y_transform[y_transform>1000] = np.inf
                            y_transform[y_transform<-1000] = np.inf
                            
                            ax.plot(domain, y_parent, label=f'$f(x)=1/x$')
                            ax.plot(domain, y_transform,\
                            label=f'$g(x)={y_scalar}$'\
                            f'$(1/({x_scalar}x-({h}/{x_scalar}))) + {k}$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h/x_scalar-1
                            b_1 = y_scalar*\
                            (1/(x_scalar*a_1-(h/x_scalar))) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = (h/x_scalar)-0.5
                            b_2 = y_scalar*\
                            (1/(x_scalar*a_2-(h/x_scalar))) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = (h/x_scalar)+0.5
                            b_3 = y_scalar*\
                            (1/(x_scalar*a_3-(h/x_scalar))) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                            
                            flag = False
                            break
                
                    else:
                        domain = np.arange(-10, 10.01, 0.01)
                            
                        y_parent = 1/domain
                        y_parent[y_parent>1000] = np.inf
                        y_parent[y_parent<-1000] = np.inf
                        
                        y_transform = y_scalar*(1/(x_scalar*(domain))) + k
                        y_transform[y_transform>1000] = np.inf
                        y_transform[y_transform<-1000] = np.inf
                        
                        ax.plot(domain, y_parent, label=f'$f(x)=1/x$')
                        ax.plot(domain, y_transform,\
                        label=f'$g(x)={y_scalar}$'\
                        f'$(1/({x_scalar}x)) + {k}$')
                        
                        # Plotting labeled ordered pairs
                        a_1 = h/x_scalar-1
                        b_1 = y_scalar*(1/(x_scalar*(a_1))) + k
                        ax.scatter(\
                        a_1, b_1,\
                        label='({:f}, {:f})'.format(a_1, b_1),\
                        c='orange',\
                        s=100, marker='s')
        
                        a_2 = (h/x_scalar)-0.5
                        b_2 = y_scalar*(1/(x_scalar*(a_2))) + k
                        ax.scatter(\
                        a_2, b_2,\
                        label='({:f}, {:f})'.format(a_2, b_2),\
                        c='cyan',\
                        s=100, marker='s')
                
                        a_3 = (h/x_scalar)+0.5
                        b_3 = y_scalar*(1/(x_scalar*(a_3))) + k
                        ax.scatter(\
                        a_3, b_3,\
                        label='({:f}, {:f})'.format(a_3, b_3),\
                        c='purple',\
                        s=100, marker='s')
                        
                        flag = False
                        break
                
                else:
                    domain = np.arange(-10, 10.01, 0.01)
                            
                    y_parent = 1/domain
                    y_parent[y_parent>1000] = np.inf
                    y_parent[y_parent<-1000] = np.inf
                    
                    y_transform = y_scalar*(1/(domain-h)) + k
                    y_transform[y_transform>1000] = np.inf
                    y_transform[y_transform<-1000] = np.inf
                    
                    ax.plot(domain, y_parent, label=f'$f(x)=1/x$')
                    ax.plot(domain, y_transform,\
                    label=f'$g(x)={y_scalar}$'\
                    f'$(1/(x-{h})) + {k}$')
                    
                    # Plotting labeled ordered pairs
                    a_1 = h/x_scalar-1
                    b_1 = y_scalar*(1/(a_1-h)) + k
                    ax.scatter(\
                    a_1, b_1,\
                    label='({:f}, {:f})'.format(a_1, b_1),\
                    c='orange',\
                    s=100, marker='s')
        
                    a_2 = (h/x_scalar)-0.5
                    b_2 = y_scalar*(1/(a_2-h)) + k
                    ax.scatter(\
                    a_2, b_2,\
                    label='({:f}, {:f})'.format(a_2, b_2),\
                    c='cyan',\
                    s=100, marker='s')
                
                    a_3 = (h/x_scalar)+0.5
                    b_3 = y_scalar*(1/(a_3-h)) + k
                    ax.scatter(\
                    a_3, b_3,\
                    label='({:f}, {:f})'.format(a_3, b_3),\
                    c='purple',\
                    s=100, marker='s')
                    
                    flag = False
                    break
        
        # Plotting labeled ordered pairs for the parent
        a_1 = 1
        b_1 = 1/a_1
        ax.scatter(a_1, b_1, label='({:f}, {:f})'.format(a_1, b_1),\
        c='red',\
        s=100, marker='>')
        
        a_2 = -1
        b_2 = 1/a_2
        ax.scatter(a_2, b_2, label='({:f}, {:f})'.format(a_2, b_2),\
        c='blue',\
        s=100, marker='>')
        
        # Putting some restrictions and information on the graphing window
        plt.ylim(-10, 10)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=20)
        fig.suptitle('Reciprocal Degree 0 by Degree 1 Transform', fontsize=20)
        plt.legend(prop={'size': 20})
            
        # Saving the figure to the static folder
        fig.savefig(\
        'app/static/images/reciprocal_degree_0_by_degree_1_transform.png')