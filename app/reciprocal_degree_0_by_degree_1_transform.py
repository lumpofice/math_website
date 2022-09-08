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
                domain = np.arange(-10, 10.01, 0.1)
                            
                y_parent = 1/domain
                y_parent[y_parent>1000] = np.inf
                y_parent[y_parent<-1000] = np.inf
                            
                y_parent = np.array(y_parent)
                ax.plot(domain, y_parent, label='Parent')
                flag = False
                break
            
            elif x_scalar == 0:
                domain = np.arange(-10, 10.01, 0.1)
                            
                y_parent = 1/domain
                y_parent[y_parent>1000] = np.inf
                y_parent[y_parent<-1000] = np.inf
                    
                y_parent = np.array(y_parent)
                ax.plot(domain, y_parent, label='Parent')
                flag = False
                break
            
            else:
                if x_scalar != 1:
                
                    if h != 0:
                
                        if h/x_scalar < 0:
                            
                            domain = np.arange((h/x_scalar)-10, 10.01, 0.1)
                            
                            y_parent = 1/domain
                            y_parent[y_parent>1000] = np.inf
                            y_parent[y_parent<-1000] = np.inf
                            
                            y_transform = y_scalar*(\
                            1/(x_scalar*(domain-(h/x_scalar)))) + k
                            y_transform[y_transform>1000] = np.inf
                            y_transform[y_transform<-1000] = np.inf                            
                            
                            ax.plot(domain, y_parent, label='Parent')
                            ax.plot(domain, y_transform, label='Transform')
                            flag = False
                            break
                            
                        elif h/x_scalar > 0:
                            domain = np.arange(-10, (h/x_scalar)+10.01, 0.1)
                            
                            y_parent = 1/domain
                            y_parent[y_parent>1000] = np.inf
                            y_parent[y_parent<-1000] = np.inf
                            
                            y_transform = y_scalar*(\
                            1/(x_scalar*(domain-(h/x_scalar)))) + k
                            y_transform[y_transform>1000] = np.inf
                            y_transform[y_transform<-1000] = np.inf
                            
                            ax.plot(domain, y_parent, label='Parent')
                            ax.plot(domain, y_transform, label='Transform')
                            flag = False
                            break
                
                    else:
                        domain = np.arange(-10, 10.01, 0.1)
                            
                        y_parent = 1/domain
                        y_parent[y_parent>1000] = np.inf
                        y_parent[y_parent<-1000] = np.inf
                        
                        y_transform = y_scalar*(1/(x_scalar*(domain))) + k
                        y_transform[y_transform>1000] = np.inf
                        y_transform[y_transform<-1000] = np.inf
                        
                        ax.plot(domain, y_parent, label='Parent')
                        ax.plot(domain, y_transform, label='Transform')
                        flag = False
                        break
                
                else:
                    domain = np.arange(-10, 10.01, 0.1)
                            
                    y_parent = 1/domain
                    y_parent[y_parent>1000] = np.inf
                    y_parent[y_parent<-1000] = np.inf
                    
                    y_transform = y_scalar*(1/(domain-h)) + k
                    y_transform[y_transform>1000] = np.inf
                    y_transform[y_transform<-1000] = np.inf
                    
                    ax.plot(domain, y_parent, label='Parent')
                    ax.plot(domain, y_transform, label='Transform')
                    flag = False
                    break
        
        # Putting some restrictions and information on the graphing window
        plt.ylim(-10, 10)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=20)
        fig.suptitle('Reciprocal Degree 0 by Degree 1 Transform', fontsize=20)
        plt.legend(prop={'size': 20})
            
        # Saving the figure to the static folder
        fig.savefig(\
        'app/static/images/reciprocal_degree_0_by_degree_1_transform.png')