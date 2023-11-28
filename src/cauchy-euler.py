import numpy as np
import matplotlib.pyplot as plt
import sys;


### Función del método de Euler
def metodo_euler_multiple(x,y0,h):    
    ### Número de EDOs a resolver    
    n    = len(y0)    
    y    = np.zeros([len(x),n])    
    y[0] = y0    
    # sys.exit()    
    for i in range(1,len(x),1):        
        y[i] = y[i-1] + np.array(fx_edo(x[i-1],y[i-1]))*h   
        #End for    

        #Impresión en pantalla    
        print("Método de Euler para el sistema de EDOs")    
        for i in range(0,len(x),1):        
            print("x:",x[i],"\t",end=' ')        
            for j in range(0,n,1,):            
                print("y",j+1,":",y[i,j],"\t",end= ' ')        
            #End for        
            print('')    
        #End for        
        
        fig = plt.figure(figsize=(6,5))    
        colors = plt.get_cmap('jet')(np.linspace(0.1, 0.9,n))   
        for i in range(0,n,1):        
            plt.plot(x,y[:,i],'-',color=colors[i],lw = 1.5,label='Método de Euler:y'+str(i+1))      
            plt.legend(frameon=True,fontsize=14,loc=0,ncol=1)    
            plt.yticks(fontsize=10)    
            plt.xlabel("x",fontsize = 16, color = 'black')    
            plt.ylabel("y",fontsize = 16, color = 'black')    
            titulog = 'Fig_metodo_euler.png'    
            plt.title('Aproximación de EDO \n',fontsize=10,fontweight='bold')    
            plt.grid(True)    
            plt.grid(color = '0.5', linestyle = '--',linewidth = 1)    
            plt.xticks(rotation=0,fontweight='bold')    
            plt.yticks(fontweight='bold')    
            plt.show()    
            plt.savefig(titulog, dpi = 600)    
            # fig.clear()    
            plt.close(fig)
            
#End function

""" ZDeclaración de parámetros"""
# ### Condiciones iniciales
x0 = 0.0                # Valor de variable independiente inicial
y0 = np.array([4,6])    # Valor de variables dependientes iniciales
### Valor final de variable independiente
xf = 2.0
### Intervalo o paso
h  = 0.5
### Variables de x a evaluar
x = np.arange(x0,xf+h,h)
### Declaración de EDO
def fx_edo(x,y):    
    fx1 = -0.5*y[0]    
    fx2 = 4-0.3*y[1]-0.1*y[0]    
    return fx1,fx2
#End function### Llamado del método
metodo_euler_multiple(x,y0,h)