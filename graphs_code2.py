# furnished graph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # Read the csv file
    data_file = r'C:\Users\Gebruiker\Downloads\data_a.csv'
    data = pd.read_csv(data_file)

    # Get data info
    print(data.info())

    # Get data description
    print(data.describe())

    # Dropna based on Price column
    data = data.dropna(subset=['Price'])
    # Dropna based on Furniture column
    data = data.dropna(subset=['Furnished'])

    # Separate the data into to rent and to sell
    data_to_sell = data[data['To sell'] == True]
    data_to_rent = data[data['To sell'] == False]

    # Calculate the median price by funished
    median_prices_to_sell = data_to_sell.groupby('Furnished')['Price'].median()
    median_prices_to_rent = data_to_rent.groupby('Furnished')['Price'].median()

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
    ax[0].set_xlabel('Furnished')
    ax[1].set_xlabel('Furnished')
    # set title
    ax[0].set_title('Median price by furnished for to sell')
    ax[1].set_title('Median price by furnished for to rent')
    plt.show()
