import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# read csv data into a pandas dataframe
df = pd.read_csv("cleaned_data.csv")

# drop duplicates
#df = (df.drop_duplicates())

# drop NAN
#df = df.dropna()

# select only numeric columns
#df = df.select_dtypes(exclude='object')

# calculating correlation
#corr = data.corr()
price = df["Price"]
scaler = StandardScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])
df["Price"] = price

# Split data into features and target variable
X = df[['Number of rooms', 'Living Area', 'Terrace', 'Area of the terrace',
        'Area of the garden', 'zipcode', 'Surface area of the plot of land', 'Number of facades']]
y = df['Price']


# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

# create a model
rf = RandomForestRegressor(n_estimators=300, max_depth=250)

# Fit the model to the training data
rf.fit(X_train, y_train)


# save the model to disk
filename = 'finalized_model.pkl'
pickle.dump(rf, open(filename, 'wb'))
# create dictionaries

data = {
    "data": {
        "Number of Romms": [int],
        "Living area": [int],
        "Terrace": [bool],
        "Area of the garden": [int],
        "Area of the terrace": [int],
        "Garden": [bool],
        "Area of the Garden": [int],
        "Surface area of plot of land": [int],
        "Number of faced": [int],
        "zipcode": [int]
    }
}

# Convert dictionary to DataFrame
#df = pd.DataFrame.from_dict(data)
# print(df)
process_house_data = df

process_house_data = data
df.fillna(0, inplace=True)

rfr = RandomForestRegressor()
rfr.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rfr.predict(X_test)

# mean of price
print("This is the mean price of a house", df["Price"].mean())

# calculate accuracy before using mean
print("This is the accuracy of the data before using mean Price of a house :",
      rf.score(X_test, y_test))

# mean absolute error
error = abs(y_pred - y_test).mean()
print("This is the mean absolute error of the data : ", error)


# accuracy of the model
print("This is the accuracy of the data after using the mean price of a house: ",
      abs(1-error/df["Price"].mean())*100, "%")


process_house_data = df
