import sympy as sp 
import lcapy

if __name__=="__main__":
    s,t = sp.symbols("s, t")
    model = 1/(s*(s**2+5*s+6))
    F = sp.inverse_laplace_transform(model, s, t)
    