import numpy as np
from scipy import signal as sig
from scipy import optimize as opt
import pandas as pd 
import matplotlib.pyplot as plt

class TF_identificator:
    def __init__(self):
        self.tf = None
        self.inputs = None

    def first_order_mdl(self, t, k, pole):
        self.tf = sig.TransferFunction(k, [pole, 1])
        to, yo, xo = sig.lsim2(self.tf, U=self.inputs, T=t)
        return yo

    def second_order_mdl(self, t, k, wn, delta):
        self.tf = sig.TransferFunction(k*(wn**2), [1, 2*delta*wn, wn**2])
        to, yo, xo = sig.lsim2(self.tf, U=self.inputs, T=t)
        return yo

    def identify_first_order(self, t, u, orig_output, method='lm', p0=[1.0, 1.0]):
        self.inputs = u
        params, params_cov = opt.curve_fit(self.first_order_mdl, t, orig_output,
                                           method=method, maxfev=1000, p0=p0)
        return {'k': params[0], 'tau': params[1]}

    def identify_second_order(self, t, u, orig_output, method='lm', p0=[1.0, 1.0, 0.1]):
        self.inputs = u
        params, params_cov = opt.curve_fit(self.second_order_mdl, t, orig_output,
                                           method=method, maxfev=1000, p0=p0)
        return {'k': params[0], 'wn': params[1], 'zeta': params[2]}
    

if __name__=='__main__':
    df = pd.read_csv('09_06_2023_23_58.csv')
    t = list(df['time'])
    y = list(df['RPM'])
    u = len(df)*[1]
    plt.plot(t,y)
    plt.xlabel('Tempo(s)')
    plt.ylabel('RPM')
    plt.show()
    tf = TF_identificator()
    print(tf.identify_second_order(t,u,y))
    print(tf.identify_first_order(t,u,y))