# House Price Prediction
This project builds a machine learning model that predicts house prices 
based on features like area, bedrooms, bathrooms, stories, and other 
factors using Linear Regression.
## Project Structure:
This project contains three files. The main script `Regression_model.py` handles 
everything from loading the data to training and predicting. The dataset 
`price.csv` contains all the housing information the model learns from. 
And `README.md` is this documentation file.

## Dataset:
The dataset `price.csv` contains real housing data. Each house entry 
includes its price  the area in square feet, number of bedrooms and bathrooms, and how many stories it has. It also tells us whether the house is connected to a main road, has a guestroom, basement, or hot water heating — all stored as simple yes/no values. Finally, it includes the furnishing status, which can 
be furnished, semi-furnished, or unfurnished.
## How It Works:
The model follows a simple but effective pipeline. We start by reading 
`price.csv` using pandas to bring all the housing data into our program. 
Since some columns contain yes/no values, we convert them to 1/0 so 
the model can understand them. We then divide the data — 80% goes to 
training the model and 20% is kept  for testing. A Linear 
Regression model is then used for  training the data to learn the 
relationship b/w features and price. Finally, we use the R² score 
to measure how well our predictions match the actual prices.

## Results:
The model achieved an accuracy of **65.3%**. Here are a few examples from the test data:
 It has predicted 5,164,654 when the actual price was 4,060,000
 It has predicted 7,224,722 when the actual price was 6,650,000
 It has predicted 3,109,863 when the actual price was 3,710,000
 It has predicted 4,612,075 when the actual price was 6,440,000
 It has predicted 3,294,646 when the actual price was 2,800,000
The  predictions are  in the right range, but not perfect. 
This tells that factors beyond our dataset — like location or market 
trends — also effects house pricing.

## Requirements:
 Python  along with two libraries — 
pandas for handling the data and scikit-learn for building the model. 
We can install both by running:
pip install pandas scikit-learn.

## How to Run:
First copy or download this repository. Make sure `price.csv` is in 
the same folder as `Regression_model.py`. Then open your terminal, Select 
the project folder and run:
python Regression_model.py
The terminal will display the predicted prices and the model accuracy.
