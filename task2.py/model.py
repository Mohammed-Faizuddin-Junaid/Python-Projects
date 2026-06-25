import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv("price.csv")
# Converting the  alphabatical data into numarical data.
for col in ["mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea"]:
    df[col]=df[col].map({"yes": 1,"no":0})
df=pd.get_dummies(df,columns=["furnishingstatus"])
df=df.astype({col: int for col in df.select_dtypes(bool).columns})
# Droping the price column for traing the model.
X=df.drop(columns=["price"])
Y=df["price"]
# Preparing the model for training and testing
# test_size tells how much  of the total data will it be testing
# Spliting the data for training and testing 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2,random_state=42)
# Creating a empty model for training named Linear Regression
# fit trains the model and builds a relationship b/w houses and prices
model = LinearRegression()
model.fit(X_train, y_train)
# Testing the
predictions = model.predict(X_test)
print(predictions)
# Checking  if the model is showing  the accurate prices or not 
from sklearn.metrics import r2_score
score = r2_score(y_test, predictions)
print(f"Model Accuracy: {score*100:.1f}%")
# Comparing the Actual prices with  the pridictions
print("\n=== Sample Predictions vs Actual Price ===")
for i in range(5):
    print(f"Predicted: {predictions[i]:.0f} | Actual: {y_test.values[i]}")