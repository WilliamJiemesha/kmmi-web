class ModelRegression:
    def Regression(params):
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        import scipy.stats as st
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error
        from sklearn.preprocessing import LabelEncoder
        # pd.set_option('display.max_rows', None)

        url = 'https://raw.githubusercontent.com/hansrichard2000/DatasetML/main/listings.csv'
        listing_df = pd.read_csv(url)

        listing_df2 = listing_df[['neighbourhood_cleansed', 'room_type', 'accommodates', 'bathrooms_text',
                                  'bedrooms', 'beds', 'amenities', 'number_of_reviews', 'review_scores_rating', 'price']]

        listing_df2.review_scores_rating.fillna(value=0.0, inplace=True)
        listing_df2['price'] = listing_df2['price'].str.replace('$', '')
        listing_df2['price'] = pd.to_numeric(
            listing_df2['price'], errors='coerce')

        # Amenities One Hot Encoding (Manual)
        amenitiesCollectionString = []
        for arrayCollection in listing_df2['amenities']:
            arrays = []
            tempString = arrayCollection.replace('"', '')
            tempString = tempString.replace('[', '')
            tempString = tempString.replace(']', '')
            tempString = tempString.replace("'", '')
        #     tempString = tempString.replace(" ", '')
            arrays = tempString.split(',')
            for items in arrays:
                if items != '':
                    if items not in amenitiesCollectionString:
                        amenitiesCollectionString.append(items)
        for items in range(len(amenitiesCollectionString)):
            tempString = amenitiesCollectionString[items]
            if tempString[0] == ' ':
                tempString = tempString[1:]
            amenitiesCollectionString[items] = tempString

        amenitiesEncodingDf = pd.DataFrame()

        for items in amenitiesCollectionString:
            amenitiesEncodingList = []
            for rows in listing_df2['amenities']:
                if items != '':
                    if items in rows:
                        amenitiesEncodingList.append(1)
                    else:
                        amenitiesEncodingList.append(0)
            amenitiesEncodingDf[items] = amenitiesEncodingList

        listing_df2.drop('amenities', axis='columns', inplace=True)
        listing_df2 = pd.concat([listing_df2, amenitiesEncodingDf], axis=1)

        le = LabelEncoder()
        listing_df2['neighbourhood_cleansed'] = le.fit_transform(
            listing_df2['neighbourhood_cleansed'])
        listing_df2['room_type'] = le.fit_transform(listing_df2['room_type'])

        listing_df2['bathrooms_text'] = listing_df2['bathrooms_text'].str.split(
            ' ').str[0]
        listing_df2['bathrooms_text'] = listing_df2['bathrooms_text'].str.replace(
            'Shared', '0.5')
        listing_df2['bathrooms_text'] = listing_df2['bathrooms_text'].str.replace(
            'Half-bath', '0.5')
        listing_df2['bathrooms_text'] = listing_df2['bathrooms_text'].str.replace(
            'Private', '0.5')
        listing_df2.bathrooms_text.fillna(value=0, inplace=True)
        listing_df2['bathrooms_text'] = pd.to_numeric(
            listing_df2['bathrooms_text'], errors='coerce')

        listing_df2.dropna(inplace=True)

        listing_df2 = listing_df2[listing_df2['price'] < 300]
        listing_df2 = listing_df2[listing_df2['price'] > 0]

        X, y = listing_df2.loc[:, listing_df2.columns !=
                               'price'].values, listing_df2.loc[:, 'price'].values
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=0)
        
        predictionResult = {'Linear Regression': '', 'Super Vector Regression': ''}
        
        from sklearn.svm import SVR
        regressor = SVR(kernel='linear')
        regressor.fit(X, y)
        predictionResult['Super Vector Regression'] = regressor.predict([params])


        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        predictionResult['Linear Regression'] = regressor.predict([params])

        return predictionResult
