from palmerpenguins import load_penguins
import pandas as pd
import numpy as np
# drops island info
penguins = load_penguins()
# filters https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/ for only Torgersen penguins
penguins = penguins.loc[penguins['island'] == 'Torgersen']
# Adelie only
penguins = penguins.loc[penguins['species'] == 'Adelie']
# Only male
penguins = penguins.loc[penguins['sex'] == 'male']
# only data collected in 2009
penguins = penguins.loc[penguins['year'] == 2009]

# print(penguins)

# selects data of bill_length, flipper length, body mass
data = pd.DataFrame(penguins, columns=['bill_length_mm', 'flipper_length_mm', 'body_mass_g'])
# print(data.to_csv())
# converts to numpy array
matrix = pd.DataFrame(penguins, columns=['bill_length_mm', 'flipper_length_mm']).to_numpy()
# adds constant values
matrix = np.hstack((matrix, [[1] for i in range(matrix.shape[0])]))
# gets resultant vector
result_vector = pd.DataFrame(penguins, columns=['body_mass_g']).to_numpy()

# print(matrix)
# print(result_vector)

# gets values for the importance of bill length, flipper length, and the constant value
end = np.linalg.inv(matrix.transpose()@matrix)@matrix.transpose()@result_vector
print(end)
