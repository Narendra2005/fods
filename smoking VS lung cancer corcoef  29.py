import numpy as np
import matplotlib.pyplot as plt

smoking_patients=[200,220,240,260,300]
lung_cancer_patients=[25,30,35,40,55]

corcoeff=np.corrcoef(smoking_patients,lung_cancer_patients)
print(corcoeff)

# Create scatter plot
plt.scatter(smoking_patients, lung_cancer_patients, color='red')
plt.title('Sales vs Advertising')
plt.xlabel('Advertising spent')
plt.ylabel('Number of sales')
plt.grid(True)
plt.show()