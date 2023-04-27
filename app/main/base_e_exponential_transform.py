import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


class BaseEExponentialTransform():
    """
    This class will serve as the template for constructing and graphing
    exponential functions with base e.
    """
    
    def __init__(self):
        pass
    
    
    def graph(self, h, x_scalar, x_reflection, y_scalar, k):
        """
        ORDER OF TRANSFORMATION:
        Let p be the parent function
        1) Let s_x(x) = bx. This is the x_scalar. Then p(s_x(x)) = p(bx). 
        2) Let h(x) = x-h. This is the horizontal shift.
        Then p(s_x(h(x))) = p(b(x-h)). 
        3) Let r_x(x) = -x. This is x_reflection (reflection across the y-axis).
        Then p(s_x(h(r_x(x)))) = p(b(-x-h))
        4) Let s_y(x) = ap(x). This is the y_scalar.
        Then s_y(p(s_x(h(r_x(x))))) = ap(b(-x-h))
        5) Let r_y(x) = -p(x). This is the y_reflection
        (reflection across the x-axis). The y_scalar and y_reflection can be
        consolidated to a single variable: y_scalar.
        Then r_y(s_y(p(s_x(h(r_x(x)))))) = -ap(b(-x-h))
        6) Let v(x) = p(x) + k. This is the vertical shift.
        Then v(r_y(s_y(p(s_x(h(r_x(x))))))) = -ap(b(-x-h)) + k
        With the preceding definitions, we have the following order that must
        be followed when constructing the graphs of these transforms:
        Let \circ represent the symbol for function composition. Then
        (v \circ r_y \circ s_y \circ p \circ s_x \circ h \circ r_x)(x)
        is the order in which a transform is to be constructed.
        """
        
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
                y_parent = np.exp(x)
                ax.plot(x, y_parent, label=r'$f(x)=e^{x}$')
                flag = False
                break
        
            elif x_scalar == 0:
                x = np.linspace(-10, 10, 1000)
                y_parent = np.exp(x)
                ax.plot(x, y_parent, label=r'$f(x)=e^{x}$')
                flag = False
                break
            
            elif x_reflection == 0:
                x = np.linspace(-10, 10, 1000)
                y_parent = np.exp(x)
                ax.plot(x, y_parent, label=r'$f(x)=e^{x}$')
                flag = False
                break
            
            else:
                if x_scalar != 1:
                
                    if h != 0:
                
                        if h < 0:
                            x = np.linspace(h-10, 10, 1000)
                            y_parent = np.exp(x)
                            y_transform = y_scalar*\
                            np.exp(x_scalar*(x_reflection*x-h)) + k
                            ax.plot(x, y_parent, label=r'$f(x)=e^{x}$')
                            ax.plot(x, y_transform, label=r'$g(x)=a$'\
                            r'$e^{b(cx-h)} + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h
                            b_1 = y_scalar*\
                            np.exp(x_scalar*(x_reflection*a_1-h)) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = h-0.5
                            b_2 = y_scalar*\
                            np.exp(x_scalar*(x_reflection*a_2-h)) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = h+0.5
                            b_3 = y_scalar*\
                            np.exp(x_scalar*(x_reflection*a_3-h)) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                            
                            flag = False
                            break
            
                        elif h > 0:
                            x = np.linspace(-10, h+10, 1000)
                            y_parent = np.exp(x)
                            y_transform = y_scalar*\
                            np.exp(x_scalar*(x_reflection*x-h)) + k
                            ax.plot(x, y_parent, label=r'$f(x)=e^{x}$')
                            ax.plot(x, y_transform, label=r'$g(x)=a$'\
                            r'$e^{b(cx-h)} + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = h
                            b_1 = y_scalar*\
                            np.exp(x_scalar*(x_reflection*a_1-h)) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = h-0.5
                            b_2 = y_scalar*\
                            np.exp(x_scalar*(x_reflection*a_2-h)) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = h+0.5
                            b_3 = y_scalar*\
                            np.exp(x_scalar*(x_reflection*a_3-h)) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                            
                            flag = False
                            break
                
                    else:
                        x = np.linspace(-10, 10, 1000)
                        y_parent = np.exp(x)
                        y_transform = y_scalar*\
                        np.exp(x_scalar*x_reflection*x) + k
                        ax.plot(x, y_parent, label=r'$f(x)=e^{x}$')
                        ax.plot(x, y_transform, label=r'$g(x)=a$'\
                        r'$e^{bcx} + k$')
                        
                        # Plotting labeled ordered pairs
                        a_1 = h
                        b_1 = y_scalar*\
                        np.exp(x_scalar*x_reflection*a_1) + k
                        ax.scatter(\
                        a_1, b_1,\
                        label='({:f}, {:f})'.format(a_1, b_1),\
                        c='orange',\
                        s=100, marker='s')
        
                        a_2 = h-0.5
                        b_2 = y_scalar*\
                        np.exp(x_scalar*x_reflection*a_2) + k
                        ax.scatter(\
                        a_2, b_2,\
                        label='({:f}, {:f})'.format(a_2, b_2),\
                        c='cyan',\
                        s=100, marker='s')
                
                        a_3 = h+0.5
                        b_3 = y_scalar*\
                        np.exp(x_scalar*x_reflection*a_3) + k
                        ax.scatter(\
                        a_3, b_3,\
                        label='({:f}, {:f})'.format(a_3, b_3),\
                        c='purple',\
                        s=100, marker='s')
                        
                        flag = False
                        break
                
                else:
                    x = np.linspace(-10, 10, 1000)
                    y_parent = np.exp(x)
                    y_transform = y_scalar*\
                    np.exp(x_reflection*x-h) + k
                    ax.plot(x, y_parent, label=r'$f(x)=e^{x}$')
                    ax.plot(x, y_transform, label=r'$g(x)=a$'\
                    r'$e^{cx-h} + k$')
                    
                    # Plotting labeled ordered pairs
                    a_1 = h
                    b_1 = y_scalar*\
                    np.exp(x_reflection*a_1-h) + k
                    ax.scatter(\
                    a_1, b_1,\
                    label='({:f}, {:f})'.format(a_1, b_1),\
                    c='orange',\
                    s=100, marker='s')
        
                    a_2 = h-0.5
                    b_2 = y_scalar*\
                    np.exp(x_reflection*a_2-h) + k
                    ax.scatter(\
                    a_2, b_2,\
                    label='({:f}, {:f})'.format(a_2, b_2),\
                    c='cyan',\
                    s=100, marker='s')
                
                    a_3 = h+0.5
                    b_3 = y_scalar*\
                    np.exp(x_reflection*a_3-h) + k
                    ax.scatter(\
                    a_3, b_3,\
                    label='({:f}, {:f})'.format(a_3, b_3),\
                    c='purple',\
                    s=100, marker='s')
                    
                    flag = False
                    break
        
        # Plotting labeled ordered pairs for the parent
        p_1 = 1
        q_1 = np.exp(p_1)
        ax.scatter(p_1, q_1, label='({:f}, {:f})'.format(p_1, q_1),\
        c='red',\
        s=100, marker='>')
        
        p_2 = -1
        q_2 = np.exp(p_2)
        ax.scatter(p_2, q_2, label='({:f}, {:f})'.format(p_2, q_2),\
        c='blue',\
        s=100, marker='>')
        
        # Putting some restrictions and information on the graphing window
        plt.ylim(-10, 10)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=20)
        fig.suptitle('Base e Exponential Transform', fontsize=20)
        plt.legend(prop={'size': 15})
            
        # Saving the figure to the static folder
        fig.savefig(\
        'app/static/images/base_e_exponential_transform.png')













