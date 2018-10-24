# Churn Classification

The problem is churn prediction with a fictional company that provides ride-share in Game of Thrones. If a certain user is predicted to churn, potentially a coupon or other marketing mechanisim could be sent.

We consider that a user has churned when the service has not been used for over a month. For this dataset, the cutoff date is June 1. See data details towards the end of this readme.

## General Approach
1. Data_Exploration.ipynb outlines the EDA process
    > Link https://nbviewer.jupyter.org/github/vivian5668/classify_churn/blob/master/Data_Exploration.ipynb
2. data_transform.py is a pipeline that cleans and transforms the data
    > link
    https://github.com/vivian5668/classify_churn/blob/master/data_transform.py
3. Conclusions.ipynb builds out models and draws conclusions on how to potentially lower churn rate by targeting customers with specific traits
    > Link
    https://nbviewer.jupyter.org/github/vivian5668/classify_churn/blob/master/Conclusions.ipynb

## Data Leakage
Upon first scan of data, I determined that last_trp_date should not be an independent variable in the model. The super correlation between last_trip_date and prediction conclusion is considered dta leakage.

## NAs
There were NAs for 'avg_rating_of_driver', 'avg_rating_by_driver', and 'phone'. I filled the NAs with 0, which is different from any of the other values in the columns. And A new column is added for each indicating where there was an NA, i.e. "'avg_rating_of_driver_isNA".

## Gradient Boosting Hyperparameter Tuning
 - n_estimator should be the where the log loss for testing data is the lowest. 
 See plot in jupyter notebook 'Conclusions'. The optimal n_estimator is 550.
 - sub-sampling in default setting is 1, which is no sampling. I changed it to 0.5. an empirically adequate value. 
 The resulting log loss has been improved a little compared to the previous default setting.

## Partial Dependence Plot
I am interested in the independent variables that contribute to the dependent variable most. Feature importance in a model can only show the feature importance relative ranking in the realm of that particular model. Partial Dependence plot will be used to better show the relationship I am looking for.

-- Interesting discoveries
- As average rating by driver increases, a customer is less likely to churn, until the rating hits 5. A possible reasoning could be that 5-star customers haven't had many trips. Maybe they are just trying it out, hence not loyal customers. Marketing material could potentially target this group to retain this group's interest

- Average surge doesn't appear to affect churn rate much
- trips in first 30 days has interesting ups and downs with an overall trend of increasing chance of churn. Attractive promotions are generally given for new customers. Some price-customers will stop using the app once promotion is used, hence the upward segments; some customers are retained in the process, hence the downward segments. A potential move to keep the price-concious segment of customers might be individualized coupon per month instead of giving all the promotions within the first month. 

note: the y-axis is in log odds units

## Data
a sample dataset of a cohort of users who signed up for an account in January 2014. The data was pulled on July
1, 2014; we consider a user retained if they were “active” (i.e. took a trip) in the preceding 30 days (from the day the data was pulled). In other words, a user is "active" if they have taken a trip since June 1, 2014.

- `city`: city this user signed up in phone: primary device for this user
- `signup_date`: date of account registration; in the form `YYYYMMDD`
- `last_trip_date`: the last time this user completed a trip; in the form `YYYYMMDD`
- `avg_dist`: the average distance (in miles) per trip taken in the first 30 days after signup
- `avg_rating_by_driver`: the rider’s average rating over all of their trips 
- `avg_rating_of_driver`: the rider’s average rating of their drivers over all of their trips 
- `surge_pct`: the percent of trips taken with surge multiplier > 1 
- `avg_surge`: The average surge multiplier over all of this user’s trips 
- `trips_in_first_30_days`: the number of trips this user took in the first 30 days after signing up 
- `luxury_car_user`: TRUE if the user took a luxury car in their first 30 days; FALSE otherwise 
- `weekday_pct`: the percent of the user’s trips occurring during a weekday





