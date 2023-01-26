# immo_eliza
data analysis project and data modeling project
Real Estate Analysis

For the data analysis project the script reads in a CSV file containing real estate data, uses the Pandas library to manipulate the data, and creates visualizations using Matplotlib and Seaborn to analyze the median prices of properties by region and whether they are furnished or not. and for the data modeling projectuses the Random Forest Regressor algorithm from the scikit-learn library to predict the price of a property based on various features such as the number of rooms, living area, terrace area, garden area, zipcode, surface area of the plot of land, and number of facades. The code first imports the necessary libraries and reads in a csv file containing the data. It then drops any rows with missing values, removes specified columns, and selects only numeric columns. The code also calculates the correlation between the features and the target variable (price) and normalizes the data. The data is then split into training and test sets, and the model is fit to the training data. Predictions are made on the test data and the accuracy of the model is calculated.
Installation

To run this script, you will need to have Python and the following libraries installed:

    Numpy
    Pandas
    Matplotlib
    Seaborn
    scikit-learn
    These libraries can be installed using pip by running the command "pip install numpy pandas matplotlib seaborn" and "pip install numpy pandas scikit-learn"
    
Usage



                                                                  
For the data analysis project:
    Download the script and the csv file "data_a.csv"
    Make sure the csv file is in the same folder as the script.
    open the script and change the file path in the script to the location of the data_a.csv file on your local machine.
    Run the script using the command python script_name.py
For the data modeling project: 
    Update the list of columns to drop in the "columns_to_drop" variable if necessary.
    Update the list of features used in the "X" variable if necessary.
    
   
    Run the code and the accuracy of the model will be printed out.
    You can use the "predict" function to make predictions on new data.
    You can also adjust the parameters of the model such as the number of estimators and maximum depth to optimize the performance of the model.



Visuals


For the Data analaysis project i made two graphs:
<table>
  <tr>
    <td>
      <img src="https://github.com/Mebatesfaye05/immo_eliza_project/blob/main/Data%20visualization/First_graph/1_graph.png" width ="400"
      height=""200">
    </td>
    <td>
      <img src="https://github.com/Mebatesfaye05/immo_eliza_project/blob/main/Data%20visualization/second%20graph/Location_graph_2.png" width ="400"
      height=""200">
    </td>
  </tr>
 </table>
 
 
 Model evaluation 
 1. To improve the result, try different feature selection methods, or try different models or tuning their hyperparameters.
 2. The feature selection step has the most impact on the results, as the chosen features will determine the model's ability to accurately predict the target variable.
 3. You should divide their time working on this project by first understanding the problem and the data, then feature selection, model selection and tuning, evaluating the model, and finally, interpreting and communicating the results.
 
 
Contributors

This script was created by Meba Tesfaye
Timeline

The script was created on January 17 2023 and January 26 2023
Personal situation

This script was created as a part of an exercise and is not intended for commercial use.

Please note that the code uses the file path r'C:\Users\Gebruiker\Downloads\data_a.csv' which is specific to the user's machine, if you want to run the code you need to change the path to the location of the data_a.csv file on your local machine.
