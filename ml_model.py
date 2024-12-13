import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
data = pd.read_csv('data/dataset.csv')

# Feature extraction
X = data[['url_length', 'has_at_symbol', 'num_digits']]
y = data['is_phishing']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)

