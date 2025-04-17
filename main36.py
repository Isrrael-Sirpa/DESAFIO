import numpy as np
import matplotlib.pyplot as plt

T_vals = [7, 21, 35, 49, 63, 77, 91]  
a_vals = [8.5, 21, 50, 77, 89, 98]    
b_vals = [0.58629528, 1.50598086, 2.28263841, 1.36346548, 0.62064252]  
c_vals = [2.5808E-17, 0.06569183, -0.01021629, -0.05543892, 0.00238014]  
d_vals = [0.00156409, -0.00180734, -0.00107673, 0.00137664, -5.667E-05]  

plt.figure(figsize=(10, 6))

for i in range(len(b_vals)):
    x0 = T_vals[i]
    x1 = T_vals[i + 1]
    x_range = np.linspace(x0, x1, 100)
    y_vals = (
        a_vals[i]
        + b_vals[i] * (x_range - x0)
        + c_vals[i] * (x_range - x0)**2
        + d_vals[i] * (x_range - x0)**3
    )
    plt.plot(x_range, y_vals, label=f"S{i}(x) en [{x0}, {x1}]")

plt.scatter(T_vals[:-1], a_vals, color='black', label='Datos originales', zorder=5)

plt.title("Interpolación por Splines Cúbicos - Crecimiento de Planta")
plt.xlabel("Día")
plt.ylabel("Altura (in.)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
