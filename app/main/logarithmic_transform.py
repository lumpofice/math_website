import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


class LogarithmicTransform():
    """
    This class will serve as the template for constructing and graphing
    logarithmic functions with user-chosen bases between 0.1 and 3.1.
    """
    
    def __init__(self):
        pass
    
    
    def general_logarithmic(self, base, h, x_scalar, x_reflection, y_scalar, k):
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
                x = np.linspace(0.001, 10, 1000)
                y_parent = np.log(x)/np.log(base)
                y_parent[y_parent>10] = np.inf
                y_parent[y_parent<-10] = np.inf
                ax.plot(x, y_parent, label=r'$f(x)=\log_B (x)$')
                flag = False
                break
        
            elif x_scalar == 0:
                x = np.linspace(0.001, 10, 1000)
                y_parent = np.log(x)/np.log(base)
                y_parent[y_parent>10] = np.inf
                y_parent[y_parent<-10] = np.inf
                ax.plot(x, y_parent, label=r'$f(x)=\log_B (x)$')
                flag = False
                break
            
            elif x_reflection == 0:
                x = np.linspace(0.001, 10, 1000)
                y_parent = np.log(x)/np.log(base)
                y_parent[y_parent>10] = np.inf
                y_parent[y_parent<-10] = np.inf
                ax.plot(x, y_parent, label=r'$f(x)=\log_B (x)$')
                flag = False
                break
            
            else:
                
                if x_scalar != 1:
                
                    if h != 0:
                
                        if h < 0:
                            
                            if x_reflection > 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10, 1000)
                                y_parent = np.log(x_parent)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=log_{B} (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10, -(h+0.001), 1000)
                                y_parent = np.log(x_parent)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=log_{B} (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = h-1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h-2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h-3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
            
                        elif h > 0:
                            
                            if x_reflection > 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10+h, 1000)
                                y_parent = np.log(x_parent)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=log_{B} (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10-h, -h-0.001, 1000)
                                y_parent = np.log(x_parent)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=log_{B} (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = -h-1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = -h-2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = -h-3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
                
                    else:
                        
                        if x_reflection > 0:
                            x_parent = np.linspace(0.001, 10, 1000)
                            y_parent = np.log(x_parent)/np.log(base)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_scalar*x_reflection*x_parent)/\
                            np.log(base) + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x_parent, y_parent,\
                            label=r'$f(x)=log_{B} (x)$')
                            ax.plot(x_parent, y_transform, label=r'$g(x)=a$'\
                            r'$log_{B}(bcx) + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = 1
                            b_1 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_1)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = 2
                            b_2 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_2)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = 3
                            b_3 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_3)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                        
                            flag = False
                            break
                        
                        elif x_reflection < 0:
                            x_parent = np.linspace(0.001, 10, 1000)
                            x_transform = np.linspace(-10, -0.001, 1000)
                            y_parent = np.log(x_parent)/np.log(base)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_scalar*x_reflection*x_transform)/\
                            np.log(base) + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x_parent, y_parent,\
                            label=r'$f(x)=log_{B} (x)$')
                            ax.plot(x_transform, y_transform, label=r'$g(x)=a$'\
                            r'$log_{B}(bcx) + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = -1
                            b_1 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_1)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = -2
                            b_2 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_2)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = -3
                            b_3 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_3)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                        
                            flag = False
                            break
                
                else:
                    
                    if h != 0:
                        
                        if h < 0:
                    
                            if x_reflection > 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10+h, 1000)
                                y_parent = np.log(x)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=log_{B} (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10-h, -h-0.001, 1000)
                                y_parent = np.log(x)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=log_{B} (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = h-1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h-2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h-3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                            
                        elif h > 0:
                    
                            if x_reflection > 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10+h, 1000)
                                y_parent = np.log(x)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=log_{B} (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10-h, -h-0.001, 1000)
                                y_parent = np.log(x)/np.log(base)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)/\
                                np.log(base) + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=log_{B}(x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$log_{B}(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = -h-1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = -h-2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = -h-3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)/\
                                np.log(base) + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                        
                    else:
                        
                        if x_reflection > 0:
                            x = np.linspace(0.001, 10, 1000)
                            x_transform = np.linspace(0.001, 10, 1000)
                            y_parent = np.log(x)/np.log(base)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_reflection*x_transform)/\
                            np.log(base) + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x, y_parent,\
                            label=r'$f(x)=log_{B} (x)$')
                            ax.plot(x_transform, y_transform,\
                            label=r'$g(x)=a$'\
                            r'$log_{B}(cx) + k$')
                    
                            # Plotting labeled ordered pairs
                            a_1 = 1
                            b_1 = y_scalar*\
                            np.log(x_reflection*a_1)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = 2
                            b_2 = y_scalar*\
                            np.log(x_reflection*a_2)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = 3
                            b_3 = y_scalar*\
                            np.log(x_reflection*a_3)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                    
                            flag = False
                            break
                        
                        elif x_reflection < 0:
                            x = np.linspace(0.001, 10, 1000)
                            x_transform = np.linspace(-10, -0.001, 1000)
                            y_parent = np.log(x)/np.log(base)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_reflection*x_transform)/\
                            np.log(base) + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x, y_parent,\
                            label=r'$f(x)=log_{B}(x)$')
                            ax.plot(x_transform, y_transform,\
                            label=r'$g(x)=a$'\
                            r'$log_{B}(cx) + k$')
                    
                            # Plotting labeled ordered pairs
                            a_1 = -1
                            b_1 = y_scalar*\
                            np.log(x_reflection*a_1)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = -2
                            b_2 = y_scalar*\
                            np.log(x_reflection*a_2)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = -3
                            b_3 = y_scalar*\
                            np.log(x_reflection*a_3)/\
                            np.log(base) + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                    
                            flag = False
                            break
        
        # Plotting labeled ordered pairs for the parent
        p_1 = 1
        q_1 = np.log(p_1)/np.log(base)
        ax.scatter(p_1, q_1, label='({:f}, {:f})'.format(p_1, q_1),\
        c='red',\
        s=100, marker='>')
        
        p_2 = 2
        q_2 = np.log(p_2)/np.log(base)
        ax.scatter(p_2, q_2, label='({:f}, {:f})'.format(p_2, q_2),\
        c='blue',\
        s=100, marker='>')
        
        p_3 = 4
        q_3 = np.log(p_3)/np.log(base)
        ax.scatter(p_3, q_3, label='({:f}, {:f})'.format(p_3, q_3),\
        c='green',\
        s=100, marker='>')
        
        p_4 = 8
        q_4 = np.log(p_4)/np.log(base)
        ax.scatter(p_4, q_4, label='({:f}, {:f})'.format(p_4, q_4),\
        c='pink',\
        s=100, marker='>')
        
        # Putting some restrictions and information on the graphing window
        plt.ylim(-10, 10)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=20)
        fig.suptitle('General Logarithmic Transform', fontsize=20)
        plt.legend(prop={'size': 15})
            
        # Saving the figure to the static folder
        fig.savefig(\
        'app/static/images/general_logarithmic_transform.png')


    def base_e_logarithmic(self, h, x_scalar, x_reflection, y_scalar, k):
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
                x = np.linspace(0.001, 10, 1000)
                y_parent = np.log(x)
                y_parent[y_parent>10] = np.inf
                y_parent[y_parent<-10] = np.inf
                ax.plot(x, y_parent, label=r'$f(x)=\ln (x)$')
                flag = False
                break
        
            elif x_scalar == 0:
                x = np.linspace(0.001, 10, 1000)
                y_parent = np.log(x)
                y_parent[y_parent>10] = np.inf
                y_parent[y_parent<-10] = np.inf
                ax.plot(x, y_parent, label=r'$f(x)=\ln (x)$')
                flag = False
                break
            
            elif x_reflection == 0:
                x = np.linspace(0.001, 10, 1000)
                y_parent = np.log(x)
                y_parent[y_parent>10] = np.inf
                y_parent[y_parent<-10] = np.inf
                ax.plot(x, y_parent, label=r'$f(x)=\ln (x)$')
                flag = False
                break
            
            else:
                
                if x_scalar != 1:
                
                    if h != 0:
                
                        if h < 0:
                            
                            if x_reflection > 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10, 1000)
                                y_parent = np.log(x_parent)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=ln (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10, -(h+0.001), 1000)
                                y_parent = np.log(x_parent)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=ln (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = h-1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h-2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h-3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
            
                        elif h > 0:
                            
                            if x_reflection > 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10+h, 1000)
                                y_parent = np.log(x_parent)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=ln (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x_parent = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10-h, -h-0.001, 1000)
                                y_parent = np.log(x_parent)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_scalar*(x_reflection*x_transform-h))\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x_parent, y_parent,\
                                label=r'$f(x)=ln (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(b(cx-h)) + k$')
                            
                                # Plotting labeled ordered pairs
                                a_1 = -h-1
                                b_1 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_1-h))\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = -h-2
                                b_2 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_2-h))\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = -h-3
                                b_3 = y_scalar*\
                                np.log(x_scalar*(x_reflection*a_3-h))\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                            
                                flag = False
                                break
                
                    else:
                        
                        if x_reflection > 0:
                            x_parent = np.linspace(0.001, 10, 1000)
                            y_parent = np.log(x_parent)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_scalar*x_reflection*x_parent)\
                            + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x_parent, y_parent,\
                            label=r'$f(x)=ln (x)$')
                            ax.plot(x_parent, y_transform, label=r'$g(x)=a$'\
                            r'$ln(bcx) + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = 1
                            b_1 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_1)\
                            + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = 2
                            b_2 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_2)\
                            + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = 3
                            b_3 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_3)\
                            + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                        
                            flag = False
                            break
                        
                        elif x_reflection < 0:
                            x_parent = np.linspace(0.001, 10, 1000)
                            x_transform = np.linspace(-10, -0.001, 1000)
                            y_parent = np.log(x_parent)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_scalar*x_reflection*x_transform)\
                            + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x_parent, y_parent,\
                            label=r'$f(x)=ln (x)$')
                            ax.plot(x_transform, y_transform, label=r'$g(x)=a$'\
                            r'$ln(bcx) + k$')
                            
                            # Plotting labeled ordered pairs
                            a_1 = -1
                            b_1 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_1)\
                            + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = -2
                            b_2 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_2)\
                            + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = -3
                            b_3 = y_scalar*\
                            np.log(x_scalar*x_reflection*a_3)\
                            + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                        
                            flag = False
                            break
                
                else:
                    
                    if h != 0:
                        
                        if h < 0:
                    
                            if x_reflection > 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10+h, 1000)
                                y_parent = np.log(x)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=ln (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10-h, -h-0.001, 1000)
                                y_parent = np.log(x)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=ln (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = h-1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h-2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h-3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                            
                        elif h > 0:
                    
                            if x_reflection > 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(h+0.001, 10+h, 1000)
                                y_parent = np.log(x)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=ln (x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = h+1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = h+2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = h+3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                            
                            elif x_reflection < 0:
                                x = np.linspace(0.001, 10, 1000)
                                x_transform = np.linspace(-10-h, -h-0.001, 1000)
                                y_parent = np.log(x)
                                y_parent[y_parent>10] = np.inf
                                y_parent[y_parent<-10] = np.inf
                                y_transform = y_scalar*\
                                np.log(x_reflection*x_transform-h)\
                                + k
                                y_transform[y_transform>10] = np.inf
                                y_transform[y_transform<-10] = np.inf
                                ax.plot(x, y_parent,\
                                label=r'$f(x)=ln(x)$')
                                ax.plot(x_transform, y_transform,\
                                label=r'$g(x)=a$'\
                                r'$ln(cx-h) + k$')
                    
                                # Plotting labeled ordered pairs
                                a_1 = -h-1
                                b_1 = y_scalar*\
                                np.log(x_reflection*a_1-h)\
                                + k
                                ax.scatter(\
                                a_1, b_1,\
                                label='({:f}, {:f})'.format(a_1, b_1),\
                                c='orange',\
                                s=100, marker='s')
        
                                a_2 = -h-2
                                b_2 = y_scalar*\
                                np.log(x_reflection*a_2-h)\
                                + k
                                ax.scatter(\
                                a_2, b_2,\
                                label='({:f}, {:f})'.format(a_2, b_2),\
                                c='cyan',\
                                s=100, marker='s')
                
                                a_3 = -h-3
                                b_3 = y_scalar*\
                                np.log(x_reflection*a_3-h)\
                                + k
                                ax.scatter(\
                                a_3, b_3,\
                                label='({:f}, {:f})'.format(a_3, b_3),\
                                c='purple',\
                                s=100, marker='s')
                    
                                flag = False
                                break
                        
                    else:
                        
                        if x_reflection > 0:
                            x = np.linspace(0.001, 10, 1000)
                            x_transform = np.linspace(0.001, 10, 1000)
                            y_parent = np.log(x)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_reflection*x_transform)\
                            + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x, y_parent,\
                            label=r'$f(x)=ln (x)$')
                            ax.plot(x_transform, y_transform,\
                            label=r'$g(x)=a$'\
                            r'$ln(cx) + k$')
                    
                            # Plotting labeled ordered pairs
                            a_1 = 1
                            b_1 = y_scalar*\
                            np.log(x_reflection*a_1)\
                            + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = 2
                            b_2 = y_scalar*\
                            np.log(x_reflection*a_2)\
                            + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = 3
                            b_3 = y_scalar*\
                            np.log(x_reflection*a_3)\
                            + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                    
                            flag = False
                            break
                        
                        elif x_reflection < 0:
                            x = np.linspace(0.001, 10, 1000)
                            x_transform = np.linspace(-10, -0.001, 1000)
                            y_parent = np.log(x)
                            y_parent[y_parent>10] = np.inf
                            y_parent[y_parent<-10] = np.inf
                            y_transform = y_scalar*\
                            np.log(x_reflection*x_transform)\
                            + k
                            y_transform[y_transform>10] = np.inf
                            y_transform[y_transform<-10] = np.inf
                            ax.plot(x, y_parent,\
                            label=r'$f(x)=ln(x)$')
                            ax.plot(x_transform, y_transform,\
                            label=r'$g(x)=a$'\
                            r'$ln(cx) + k$')
                    
                            # Plotting labeled ordered pairs
                            a_1 = -1
                            b_1 = y_scalar*\
                            np.log(x_reflection*a_1)\
                            + k
                            ax.scatter(\
                            a_1, b_1,\
                            label='({:f}, {:f})'.format(a_1, b_1),\
                            c='orange',\
                            s=100, marker='s')
        
                            a_2 = -2
                            b_2 = y_scalar*\
                            np.log(x_reflection*a_2)\
                            + k
                            ax.scatter(\
                            a_2, b_2,\
                            label='({:f}, {:f})'.format(a_2, b_2),\
                            c='cyan',\
                            s=100, marker='s')
                
                            a_3 = -3
                            b_3 = y_scalar*\
                            np.log(x_reflection*a_3)\
                            + k
                            ax.scatter(\
                            a_3, b_3,\
                            label='({:f}, {:f})'.format(a_3, b_3),\
                            c='purple',\
                            s=100, marker='s')
                    
                            flag = False
                            break
        
        # Plotting labeled ordered pairs for the parent
        p_1 = 1
        q_1 = np.log(p_1)
        ax.scatter(p_1, q_1, label='({:f}, {:f})'.format(p_1, q_1),\
        c='red',\
        s=100, marker='>')
        
        p_2 = 2
        q_2 = np.log(p_2)
        ax.scatter(p_2, q_2, label='({:f}, {:f})'.format(p_2, q_2),\
        c='blue',\
        s=100, marker='>')
        
        p_3 = 4
        q_3 = np.log(p_3)
        ax.scatter(p_3, q_3, label='({:f}, {:f})'.format(p_3, q_3),\
        c='green',\
        s=100, marker='>')
        
        p_4 = 8
        q_4 = np.log(p_4)
        ax.scatter(p_4, q_4, label='({:f}, {:f})'.format(p_4, q_4),\
        c='pink',\
        s=100, marker='>')
        
        p_5 = np.exp(1)
        q_5 = np.log(p_5)
        ax.scatter(p_5, q_5, label='({:f}, {:f})'.format(p_5, q_5),\
        c='red',\
        s=100, marker='o')
        
        # Putting some restrictions and information on the graphing window
        plt.ylim(-10, 10)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=20)
        fig.suptitle('Base e Logarithmic Transform', fontsize=20)
        plt.legend(prop={'size': 15})
            
        # Saving the figure to the static folder
        fig.savefig(\
        'app/static/images/base_e_logarithmic_transform.png')










