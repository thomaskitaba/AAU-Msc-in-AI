#!/usr/bin/python3
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns




if __name__ == "__main__":
    #import csv
    #step 1
    df = pd.read_csv("student-mat.csv", sep=";")
    #df_por = pd.read_csv("student-por.csv", sep=";")
    #df = pd.read_csv("student/student-merge.csv", sep=";")

    
    #step 2
    #do exploratory data analysis
    print('describe dataframe:')
    print(df.describe())
    print("================================")
    print(f'shape of dataframe:') 
    print({df.shape})
    print("================================")
    print(f'columns of dataframe:')
    #print({df_mat.columns})
    print(f'number of null values: {df.isnull().sum()}')
    
    # check for duplicate
    print("================================")
    print(f'number of duplicate values')
    print(df.duplicated().sum())
    #if there are duplicates remove them
    if df.duplicated().sum()>0:
        df.drop_duplicates(inplace=True)
        print("Duplicates removed")
    
    # TODO: to use classification algorithms, we need to convert categorical variables to numerical
    df['pass_fail'] = df['G3'].apply(lambda x: 1 if x >= 10 else 0)
    df.drop(columns=['G3'])
    
    print("================================")
    print(df)
    # Visualize distributions and potential outliers
    numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        sns.violinplot(x=df[col])
        plt.title(f"Boxplot of {col}")
        plt.show()
    #step 3:   SEPARATE FEATURES AND TARGET
    X_train = df.drop(columns=['G3'])
    y_train = df['G3']
    
    #STEP 4: SPLIT DATASET INTO TRAINING AND TEST SET
    #step 5: TRAIN THE MODEL
    