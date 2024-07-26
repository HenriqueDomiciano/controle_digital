import control as ct 
import sympy as sp 
import numpy as np 

sp.init_printing(use_unicode=True,wrap_line=False)
z = sp.Symbol('z')

if __name__=="__main__":
    
    pole1 = complex(0.5,0.2)
    pole2 = pole1.conjugate() 
    
    A = np.array([[1,1],[0,.5]])
    b = np.array([[1],[1]])

    C = np.array([b.T[0],np.dot(A,b).T[0]]).T
    print(np.linalg.det(C))
    if np.linalg.det(C)==0:
        
        print("Sistema não controlavel")
        quit()
    
    func = sp.expand((z-pole1)*(z-pole2))
    
    print(f'Applying the function k = [0 1]C⁻1*P(A)')
    print(f'Function is {func}')
    print(f"Replacing the z with A")
    
    A_squared = sp.Matrix(np.dot(A,A))
    A_simb = sp.Matrix(A)
    P = func.replace(z,A_simb)

    numeric = P.args[0]
    
    P = (P-numeric)+numeric*sp.eye(len(A))
    
    print(f"{P},\nb = {b.T}\n\nC inv:  \n{np.linalg.inv(C)},\n\n C:{C}")
    k = np.dot(np.dot([0,1],np.linalg.inv(C)),np.array(P.tolist()))
    
    print(f"k = {k}")
