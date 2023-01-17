# location graphs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # Read the csv file
    data_file = r'C:\Users\Gebruiker\Downloads\data_a.csv'
    data = pd.read_csv(data_file)

    data["zipcode"] = data["zipcode"].astype(str)

# Create a new column named 'region' in the dataframe
    data["region"] = ""

# Use the apply() function to iterate over the 'zipcode' column
    data["region"] = data["zipcode"].apply(lambda x: "Flanders" if x.startswith(("2", "3", "9")) else (
        "Wallonia" if x.startswith(("4", "5", "6", "7")) else "Brussels" if x.startswith(("1", "8")) else ""))

# Print the updated dataframe
    print(data)
   # Dropna based on Price column
    data = data.dropna(subset=['Price'])
    # Dropna based on Furniture column
    data = data.dropna(subset=['region'])

    # Separate the data into to rent and to sell
    data_to_sell = data[data['To sell'] == True]
    data_to_rent = data[data['To sell'] == False]

    # Calculate the median price by funished
    median_prices_to_sell = data_to_sell.groupby('region')['Price'].median()
    median_prices_to_rent = data_to_rent.groupby('region')['Price'].median()

    # Plot the median price by funished with sns in subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    sns.barplot(x=median_prices_to_sell.index,
                y=median_prices_to_sell.values, ax=ax[0])
    sns.barplot(x=median_prices_to_rent.index,
                y=median_prices_to_rent.values, ax=ax[1])
    # set y axis label
    ax[0].set_ylabel('Price in euros')
    ax[1].set_ylabel('Price in euros')
    # set x axis label
    ax[0].set_xlabel('region')
    ax[1].set_xlabel('region')
    # set title
    ax[0].set_title('Median price by location for sell')
    ax[1].set_title('Median price by location for rent')
    plt.show()
