import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import math

def isNA(input):
    if pd.isnull(input):
        return 1
    else:
        return 0
def isNA_column_make(data, NA_columns):
    for column in NA_columns:
        data['{}_isNA'.format(column)] = data[column].apply(isNA)
    return data

def fillNA(data, NA_columns, fill_NA_dt):
    for column in NA_columns:
        fill = fill_NA_dt[column]
        data[column] = data[column].fillna(fill)
    return data

#change categorical data into dummy variables, need to define a function so that 
#when new data comes into the pipeline, it can handle
def make_dummies(test_col, train_unique_vals, col_name):
    """
    Return a df containing len(train_unique_vals) columns for 
    each unique value in train_unique_vals. If the test_col has more 
    unique values that are not seen in train_unique_vals, value
    will be 0
    """
    dummies = {}
    for val in train_unique_vals:
        dummies[col_name + '_' + val] = (test_col == val).astype(int)
    return pd.DataFrame(dummies, index = test_col.index)

def make_dummy_columns(data, dummy_categories):
    data_transformed = data
    for category in dummy_categories:
        temp_df = make_dummies(data[category], data[category].unique(), category)
        data_transformed = pd.concat([data, temp_df], axis = 1)
        data = data_transformed
    return data

def make_isActive_column(data, cut_off_date):
    data['last_trip_date'] = pd.to_datetime(data['last_trip_date'])
    data['isActive'] = data['last_trip_date'] > pd.to_datetime(cut_off_date)
    return data

def drop_unrelated_vari(data, drop_lst):
    data.drop(drop_lst, axis = 1, inplace= True)
    return data

def clean_all(file_path, NA_columns, fill_NA_dt, dummy_categories, drop_lst, cut_off_date):
    data = pd.read_csv(file_path)
    data = isNA_column_make(data, NA_columns)
    data = fillNA(data, NA_columns, fill_NA_dt)
    data = make_dummy_columns(data, dummy_categories)
    data = make_isActive_column(data, cut_off_date)
    data = drop_unrelated_vari(data, drop_lst)
    return data


file_path = 'data/churn.csv'
NA_columns = ['avg_rating_of_driver', 'avg_rating_by_driver', 'phone']
fill_NA_dt = {'avg_rating_by_driver': 0, 'avg_rating_of_driver': 0, 'phone': 'Unspecified'}
dummy_categories = ['city', 'phone']
drop_lst = ['signup_date', 'phone', 'city','last_trip_date']
cut_off_date = '20140601'

data = clean_all(file_path, NA_columns, fill_NA_dt, dummy_categories, drop_lst, cut_off_date)


