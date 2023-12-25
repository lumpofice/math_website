import matplotlib.pyplot as plt
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


logging.debug('Start of program' + f'\n')


class SequencePointwise():


    def __init__(self):
        pass


    def par_x_par_over_par_x_plus_n_par(self, epsilon, x):
        """This function plots each function $f_{n}(x)$, from a sequence of
    functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
    numbers, from n=1 up to whatever value of n is required for the if 
    conditional to evaluate True. Once the if conditional evaluates True, 
    the function stores the number of natural numbers, n=K, for such an 
    evaluation to be reached. This sequence of functions converges pointwise 
    to f=0, on [0, \infty)"""
    
    
            
        # The statement below begins to assemble our figure
        fig, ax = plt.subplots(figsize=(15, 10))
        
        
        # Vector u is what defines our restricted domain of each function
        # with respect to x
        u = np.linspace(0, 1000, 1000)
        
        
        # We initiate the index n with a value of 1 to simulate a
        # mathematical sequence
        n = 1
        
        
        # Vector v will serve as the range of our restricted domain defined
        # by vector u
        v = u/(u+n)
        
        
        # We plot this first vector pair u and v.
        ax.plot(u, v)
        
        
        flag = True
        while flag:
            
            
            if abs(x/(x+n)) < epsilon:
                # Completing the plot
                ax.axvline(x=0, c='k')
                ax.axhline(y=0, c='k')
                ax.axhline(y=epsilon, c='m', label=r'$\epsilon$')
                ax.axvline(x=x, c='c', label='x')
                plt.xlabel('Restricted Domain with respect to x',\
                    fontsize=20)
                plt.xticks(fontsize=10)
                plt.ylabel('Range of Restricted Domain',\
                    fontsize=20)
                plt.yticks(fontsize=10)
                plt.ylim(0, 1 + epsilon)
                plt.xlim(0, 100 + epsilon)
                fig.suptitle(r'$f_{n}(x) = \dfrac{x}{x+n}$', fontsize=20)
                plt.legend(prop={'size':20})
                
                # Saving the figure to the static folder
                fig.savefig(\
                'app/static/images/pseq_par_x_par_over_par_x_plus_n_par.png')
                
                flag = False
                
                
            else:
                # We increase our index by 1
                n += 1
                
                
                # We keep the same restricted domain with vector u, but our
                # range with this new vector v will change, since n has
                # changed
                v = u/(u+n)
                
                
                # We plot the next vector pair u and v in the same plot as
                # the preceding vector pairs
                ax.plot(u, v)
                
                    


    def par_nx_par_over_par_one_plus_par_nx_par_squared_par(self, epsilon, x):
        """This function plots each function $f_{n}(x)$, from a sequence of
    functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
    numbers, from n=1 up to whatever value of n is required for the if conditional
    to evaluate True. Once the if conditional evaluates True, the function stores
    the number of natural numbers, n=K, for such an evaluation to be reached.
    This sequence of functions converges pointwise to f=0, on (-\infty, \infty).
    However, we observe convergence on the positive portion of the graph."""
        
        
                
        # The statement below begins to assemble our figure
        fig, ax = plt.subplots(figsize=(15, 10))
        
        
        # Vector u is what defines our restricted domain of each function
        # with respect to x
        u = np.linspace(0, 100, 2000)
        
        
        # We initiate the index n with a value of 1 to simulate a
        # mathematical sequence
        n = 1
        
        
        # Vector v will serve as the range of our restricted domain defined
        # by vector u
        v = (n*u)/(1+(n*u)**2)
        
        
        # We plot this first vector pair u and v.
        ax.plot(u, v)
        
        
        flag = True
        while flag:
            
            
            if abs((n*x)/(1+(n*x)**2)) < epsilon:
                # Completing the plot
                ax.axvline(x=0, c='k')
                ax.axhline(y=0, c='k')
                ax.axhline(y=epsilon, c='k', label=r'$\epsilon$')
                ax.axvline(x=x, c='c', label='x')
                plt.xlabel('Restricted Domain with respect to x',\
                    fontsize=20)
                plt.xticks(fontsize=10)
                plt.ylabel('Range of Restricted Domain',\
                    fontsize=20)
                plt.yticks(fontsize=10)
                plt.ylim(0, 0.02)
                plt.xlim(0, 100 + epsilon)
                fig.suptitle(r'$f_{n}(x) = \dfrac{nx}{1+(nx)^2}$',\
                    fontsize=20)
                plt.legend(prop={'size':20})
                
                # Saving the figure to the static folder
                fig.savefig(\
                'app/static/images/'\
                'pseq_par_nx_par_over_'\
                'par_one_plus_par_nx_par_squared_par.png')
                
                flag = False
                
                
            else:
                # We increase our index by 1
                n += 1
                
                
                # We keep the same restricted domain with vector u, but our
                # range with this new vector v will change, since n has
                # changed
                v = (n*u)/(1+(n*u)**2)
                
                
                # We plot the next vector pair u and v in the same plot as 
                # the preceding vector pairs
                ax.plot(u, v)
                        
                        
            
            
    def par_nx_par_over_par_one_plus_nx_par(self, epsilon, x):
        """This function plots each function $f_{n}(x)$, from a sequence of
    functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
    numbers, from n=1 up to whatever value of n is required for the if conditional
    to evaluate True. Once the if conditional evaluates True, the function stores
    the number of natural numbers, n=K, for such an evaluation to be reached.
    This sequence of functions converges pointwise to f=1, on [0, \infty)."""
        
        
                
        # The statement below begins to assemble our figure
        fig, ax = plt.subplots(figsize=(15, 10))
        
        
        # Vector u is what defines our restricted domain of each function
        # with respect to x
        u = np.linspace(0, 10, 1000)
        
        
        # We initiate the index n with a value of 1 to simulate a
        # mathematical sequence
        n = 1
        
        
        # Vector v will serve as the range of our restricted domain defined
        # by vector u
        v = (n*u)/(1+(n*u))
        
        
        # We plot this first vector pair u and v, as well as the 
        # absolute value of the difference of f_n(x)-f(x), where f_n(x) is 
        # the function from our sequence at n=1 and f(x) is the function to 
        # which the sequence of functions converges for a fixed x.
        ax.plot(u, v)
        
        
        flag = True
        while flag:
            
            
            if abs((n*x)/(1+(n*x)) - 1) < epsilon:
                # Completing the plot
                ax.axvline(x=0, c='k')
                ax.axhline(y=0, c='k')
                ax.axhline(y=1-epsilon, c='k', label=r'$1-\epsilon$')
                ax.axhline(y=epsilon, c='m', label=r'$\epsilon$')
                ax.axvline(x=x, c='c', label='x')
                plt.xlabel('Restricted Domain with respect to x',\
                    fontsize=20)
                plt.xticks(fontsize=10)
                plt.ylabel('Range of Restricted Domain',\
                    fontsize=20)
                plt.yticks(fontsize=10)
                plt.ylim(0, 1.02)
                plt.xlim(0, 10 + epsilon)
                fig.suptitle(r'$f_{n}(x) = \dfrac{nx}{1+(nx)}$',\
                    fontsize=20)
                plt.legend(prop={'size':20})
                
                # Saving the figure to the static folder
                fig.savefig(\
                'app/static/images/'\
                'pseq_par_nx_par_over_'\
                'par_one_plus_nx_par.png')
                
                flag = False
                
                
            else:
                # We increase our index by 1
                n += 1
                
                
                # We keep the same restricted domain with vector u, but our
                # range with this new vector v will change, since n has
                # changed
                v = (n*u)/(1+(n*u))
                
                
                # We plot the next vector pair u and v in the same plot as 
                # the preceding vector pairs, as well as the absolute value 
                # of the difference of f_n(x)-f(x), where f_n(x) is the
                # function from our sequence at n=k and f(x) is the function 
                # to which the sequence of functions converges, for fixed x.
                ax.plot(u, v)


class SequenceUniform():


    def __init__(self):
        pass


    def par_x_par_over_par_x_plus_n_par(self, k, x, a=50):
        """This function plots each function $f_{n}(x)$, from a sequence of
    functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
    numbers, from n=1 up to whatever value of n is required for the if conditional
    to evaluate True. Once the if conditional evaluates True, the function stores
    the number of natural numbers, n=K, for such an evaluation to be reached.
    This sequence of functions converges uniformly to f=0, on [0, a],
    where a=50"""


        # The statement below begins to assemble our figure
        fig, ax = plt.subplots(figsize=(15, 10))
        
        
        # Vector u is what defines our restricted domain of each function
        # with respect to x
        u = np.linspace(0, 101, 1000)
        
        
        # We initiate the index n with a value of 1 to simulate a
        # mathematical sequence
        n = 1
        
        
        # Vector v will serve as the range of our restricted domain defined
        # by vector u
        v = u/(n+u)
        
        
        # We plot this first vector pair u and v, as well as the 
        # absolute value of the difference of f_n(x)-f(x), where f_n(x) is 
        # the function from our sequence at n=1 and f(x) is the function to 
        # which the sequence of functions uniformly converges.
        ax.plot(u, v)
        ax.scatter(x, x/(n+x),\
            label=r'$| f_n(x) - f(x) |$')
        
        
        flag = True
        while flag:
            
            
            if abs(x/(n+x)) < a/k:
                # Completing the plot
                ax.axvline(x=0, c='k')
                ax.axhline(y=0, c='k')
                ax.axhline(y=a/k, c='k', label=r'$\dfrac{50}{k}$')
                plt.xlabel('Restricted Domain with respect to x',\
                    fontsize=20)
                plt.xticks(fontsize=10)
                plt.ylabel('Range of Restricted Domain',\
                    fontsize=20)
                plt.yticks(fontsize=10)
                plt.ylim(0, 1.02)
                plt.xlim(0, 101)
                fig.suptitle(r'$f_{n}(x) = \dfrac{x}{n+x}$', fontsize=20)
                plt.legend(prop={'size':20})
                
                # Saving the figure to the static folder
                fig.savefig(\
                'app/static/images/'\
                'useq_par_x_par_over_'\
                'par_x_plus_n_par.png')
                
                flag = False
                
                
            else:
                # We increase our index by 1
                n += 1


                
                # We keep the same restricted domain with vector u, but our
                # range with this new vector v will change, since n has
                # changed
                v = u/(n+u)
                
                
                # We plot the next vector pair u and v in the same plot as 
                # the preceding vector pairs, as well as the absolute value 
                # of the difference of f_n(x)-f(x), where f_n(x) is the
                # function from our sequence at n=k and f(x) is the function 
                # to which the sequence of functions uniformly converges.
                ax.plot(u, v)
                ax.scatter(x, x/(n+x))

    def par_x_par_plus_par_one_over_n_par(self, k, x):
        """This function plots each function $f_{n}(x)$, from a sequence of
    functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
    numbers, from n=1 up to whatever value of n is required for the if conditional
    to evaluate True. Once the if conditional evaluates True, the function stores
    the number of natural numbers, n=K, for such an evaluation to be reached.
    This sequence of functions converges uniformly to f=x, on (-\infty, \infty)"""

        # The statement below begins to assemble our figure
        fig, ax = plt.subplots(figsize=(15, 10))


        # Vector u is what defines our restricted domain of each function
        # with respect to x
        u = np.linspace(-1000, 1000, 1000)


        # We initiate the index n with a value of 1 to simulate a
        # mathematical sequence
        n = 1


        # Vector v will serve as the range of our restricted domain defined
        # by vector u
        v = u + (1/n)


        # We plot this first vector pair u and v, as well as the
        # absolute value of the difference of f_n(x)-f(x), where f_n(x) is
        # the function from our sequence at n=1 and f(x) is the function to
        # which the sequence of functions uniformly converges.
        ax.plot(u, v)
        ax.scatter(x, (1/n), label=r'$| f_n(x) - f(x) |$')


        flag = True
        while flag:


            if abs(1/n) < 1/k:
                # Completing the plot
                ax.axvline(x=0, c='k')
                ax.axhline(y=0, c='k')
                ax.axhline(y=1/k, c='m', label=r'$\dfrac{1}{k}$')
                ax.plot(u, u, c='k', label=r'$f(x)=x$')
                plt.xlabel('Restricted Domain with respect to x',\
                    fontsize=20)
                plt.xticks(fontsize=10)
                plt.ylabel('Range of Restricted Domain',\
                    fontsize=20)
                plt.yticks(fontsize=10)
                plt.ylim(0, 1.5)
                plt.xlim(-1 - (1/k), 1 + (1/k))
                fig.suptitle(r'$f_{n}(x) = x + \dfrac{1}{n}$', fontsize=20)
                plt.legend(prop={'size':20})
                # Saving the figure to the static folder
                fig.savefig(\
                'app/static/images/'\
                'useq_par_x_par_plus_'\
                'par_one_over_n_par.png')


                flag = False


            else:
                # We increase our index by 1
                n += 1


                # We keep the same restricted domain with vector u, but our
                # range with this new vector v will change, since n has
                # changed
                v = u + (1/n)


                # We plot the next vector pair u and v in the same plot as
                # the preceding vector pairs, as well as the absolute value
                # of the difference of f_n(x)-f(x), where f_n(x) is the
                # function from our sequence at n=k and f(x) is the function
                # to which the sequence of functions uniformly converges.
                ax.plot(u, v)
                ax.scatter(x, (1/n))

    def par_nx_par_over_par_one_plus_nx_par(self, k, x):
        """This function plots each function $f_{n}(x)$, from a sequence of
    functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
    numbers, from n=1 up to whatever value of n is required for the if conditional
    to evaluate True. Once the if conditional evaluates True, the function stores
    the number of natural numbers, n=K, for such an evaluation to be reached.
    This sequence of functions converges uniformly to f=1, on [a, \infty),
    where a>0"""

        # The statement below begins to assemble our figure
        fig, ax = plt.subplots(figsize=(15, 10))


        # Vector u is what defines our restricted domain of each function
        # with respect to x
        a = 0.1
        u = np.linspace(a, 12, 1000)


        # We initiate the index n with a value of 1 to simulate a
        # mathematical sequence
        n = 1


        # Vector v will serve as the range of our restricted domain defined
        # by vector u
        v = (n*u)/(1+(n*u))


        # We plot this first vector pair u and v, as well as the
        # absolute value of the difference of f_n(x)-f(x), where f_n(x) is
        # the function from our sequence at n=1 and f(x) is the function to
        # which the sequence of functions uniformly converges.
        ax.plot(u, v)
        ax.scatter(x, abs((n*x)/(1+(n*x)) - 1),\
            label=r'$| f_n(x) - f(x) |$')


        flag = True
        while flag:


            if abs((n*x)/(1+(n*x)) - 1) < 1/(a*k):
                # Completing the plot
                ax.axvline(x=0, c='k')
                ax.axhline(y=0, c='k')
                ax.axhline(y=1/(a*k), c='k', label=r'$\dfrac{1}{ak}$')
                ax.axhline(y=1-(1/(a*k)), c='m', label=r'$1-\dfrac{1}{ak}$')
                plt.xlabel('Restricted Domain with respect to x',\
                    fontsize=20)
                plt.xticks(fontsize=10)
                plt.ylabel('Range of Restricted Domain',\
                    fontsize=20)
                plt.yticks(fontsize=10)
                plt.ylim(0, 1)
                plt.xlim(0, 11)
                fig.suptitle(r'$f_{n}(x) = \dfrac{nx}{1+nx}$', fontsize=20)
                plt.legend(prop={'size':20})
                # Saving the figure to the static folder
                fig.savefig(\
                'app/static/images/'\
                'useq_par_nx_par_over_'\
                'par_one_plus_nx_par.png')


                flag = False


            else:
                # We increase our index by 1
                n += 1



                # We keep the same restricted domain with vector u, but our
                # range with this new vector v will change, since n has
                # changed
                v = (n*u)/(1+(n*u))


                # We plot the next vector pair u and v in the same plot as
                # the preceding vector pairs, as well as the absolute value
                # of the difference of f_n(x)-f(x), where f_n(x) is the
                # function from our sequence at n=k and f(x) is the function
                # to which the sequence of functions uniformly converges.
                ax.plot(u, v)
                ax.scatter(x, abs((n*x)/(1+(n*x)) - 1))
