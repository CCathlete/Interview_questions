import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Setting random seed.
np.random.seed(42)

# Generating 500 samples with 4 features.
# Note, this data has linear relationships between features. 
# One imrovement might be non linear relationships like exsponents.
X: pd.DataFrame = pd.DataFrame({
  "Income": np.random.randint(20000, 100000, 500), # Annual income.
  "Credit_Score": np.random.randint(300, 850, 500),
  "Debt": np.random.randint(0, 50000, 500),
  "Age": np.random.randint(18, 100, 500),
  
})