import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


class PolynomialDegree2Transform():
    
    
    def __init__(self):
        pass
    
    
    def graph(self, h, x_scalar, x_reflection, y_scalar, k):
        
        # h: Horizontal shift on the argument
        # x_scalar: Scalar on the argument and the horizontal shift
        # x_reflection: -1 or 1 on the x variable (reflection about y-axis)
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
                ax.plot(x, y_parent, label=r'$f(x)=x^{2}$')
                flag = False
                break
        
            elif x_scalar == 0:
                x = np.linspace(-10, 10, 1000)
                y_parent = x**2
                ax.plot(x, y_parent, label=r'$f(x)=x^{2}$')
                flag = False
                break
            
            elif x_reflection == 0:
                x = np.linspace(-10, 10, 1000)
                y_parent = x**2
                ax.plot(x, y_parent, label=r'$f(x)=x^{2}$')
                flag = False
                break
            
            else:
                if x_scalar != 1:
                
                    if h != 0:
                
                        if h < 0:
                            x = np.linspace(h-10, 10, 1000)
                            y_parent = x**2
                            y_transform = y_scalar*\
                            (x_scalar*(x_reflection*x-h))**2 + k
                            ax.plot(x, y_parent, label=r'$f(x)=x^{2}$')
                            ax.plot(x, y_transform, label=r'$g(x)=a$'\
                            r'$(b(cx-h))^{2} + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h
                            b_1 = y_scalar*\
                            (x_scalar*(x_reflection*a_1-h))**2 + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = h-0.5
                            b_2 = y_scalar*\
                            (x_scalar*(x_reflection*a_2-h))**2 + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = (h/x_scalar)+0.5
                            b_3 = y_scalar*\
                            (x_scalar*(x_reflection*a_3-h))**2 + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                            
                            flag = False
                            break
            
                        elif h > 0:
                            x = np.linspace(-10, h+10, 1000)
                            y_parent = x**2
                            y_transform = y_scalar*\
                            (x_scalar*(x_reflection*x-h))**2 + k
                            ax.plot(x, y_parent, label=r'$f(x)=x^{2}$')
                            ax.plot(x, y_transform, label=r'$g(x)=a$'\
                            r'$(b(cx-h))^{2} + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h
                            b_1 = y_scalar*\
                            (x_scalar*(x_reflection*a_1-h))**2 + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = h-0.5
                            b_2 = y_scalar*\
                            (x_scalar*(x_reflection*a_2-h))**2 + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = h+0.5
                            b_3 = y_scalar*\
                            (x_scalar*(x_reflection*a_3-h))**2 + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                            
                            flag = False
                            break
                
                    else:
                        x = np.linspace(-10, 10, 1000)
                        y_parent = x**2
                        y_transform = y_scalar*\
                        (x_scalar*x_reflection*x)**2 + k
                        ax.plot(x, y_parent, label=r'$f(x)=x^{2}$')
                        ax.plot(x, y_transform, label=r'$g(x)=a$'\
                        r'$(bcx)^{2} + k$')
                        
                        # Plotting labeled ordered pairs
                        a_1 = h
                        b_1 = y_scalar*\
                        (x_scalar*x_reflection*a_1)**2 + k
                        ax.scatter(\
                        a_1, b_1,\
                        label='({:f}, {:f})'.format(a_1, b_1),\
                        c='orange',\
                        s=100, marker='s')
        
                        a_2 = h-0.5
                        b_2 = y_scalar*\
                        (x_scalar*x_reflection*a_2)**2 + k
                        ax.scatter(\
                        a_2, b_2,\
                        label='({:f}, {:f})'.format(a_2, b_2),\
                        c='cyan',\
                        s=100, marker='s')
                
                        a_3 = h+0.5
                        b_3 = y_scalar*\
                        (x_scalar*x_reflection*a_3)**2 + k
                        ax.scatter(\
                        a_3, b_3,\
                        label='({:f}, {:f})'.format(a_3, b_3),\
                        c='purple',\
                        s=100, marker='s')
                        
                        flag = False
                        break
                
                else:
                    x = np.linspace(-10, 10, 1000)
                    y_parent = x**2
                    y_transform = y_scalar*(x_reflection*x-h)**2 + k
                    ax.plot(x, y_parent, label=r'$f(x)=x^{2}$')
                    ax.plot(x, y_transform, label=r'$g(x)=a$'\
                    r'$(cx-h)^{2} + k$')
                    
                    # Plotting labeled ordered pairs
                    a_1 = h
                    b_1 = y_scalar*\
                    (x_reflection*a_1-h)**2 + k
                    ax.scatter(\
                    a_1, b_1,\
                    label='({:f}, {:f})'.format(a_1, b_1),\
                    c='orange',\
                    s=100, marker='s')
        
                    a_2 = h-0.5
                    b_2 = y_scalar*\
                    (x_reflection*a_2-h)**2 + k
                    ax.scatter(\
                    a_2, b_2,\
                    label='({:f}, {:f})'.format(a_2, b_2),\
                    c='cyan',\
                    s=100, marker='s')
                
                    a_3 = h+0.5
                    b_3 = y_scalar*\
                    (x_reflection*a_3-h)**2 + k
                    ax.scatter(\
                    a_3, b_3,\
                    label='({:f}, {:f})'.format(a_3, b_3),\
                    c='purple',\
                    s=100, marker='s')
                    
                    flag = False
                    break
        
        # Plotting labeled ordered pairs for the parent
        p_1 = 1
        q_1 = p_1**2
        ax.scatter(p_1, q_1, label='({:f}, {:f})'.format(p_1, q_1),\
        c='red',\
        s=100, marker='>')
        
        p_2 = -1
        q_2 = p_2**2
        ax.scatter(p_2, q_2, label='({:f}, {:f})'.format(p_2, q_2),\
        c='blue',\
        s=100, marker='>')
        
        # Putting some restrictions and information on the graphing window
        plt.ylim(-10, 10)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=20)
        fig.suptitle('Polynomial Degree 2 Transform', fontsize=20)
        plt.legend(prop={'size': 15})
            
        # Saving the figure to the static folder
        fig.savefig(\
        'app/static/images/polynomial_degree_2_transform.png')






