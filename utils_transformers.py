################################################################################  IMPORT AND DEFINE TRANSFORMERS
import numpy as np
import pandas as pd
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import FeatureAgglomeration
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import Normalizer
import re
from sklearn.preprocessing import FunctionTransformer

#define dftransf
class DataframeFunctionTransformer():
    def __init__(self, func):
        self.func = func

    def transform(self, input_df, **transform_params):
        return self.func(input_df)

    def fit(self, X, y=None, **fit_params):
        return self
    

################################################################################ DROP FUNCTION

def columns_drop(df):
    for col in df.columns:
        df = df.drop(col,axis=1)
        #print('drop ',col)
    return df

#NUMERICAL FUNCTIONS
def num_encoder(df):
    for col in df.columns:
        df[col] = df[col].replace(to_replace=r'^<(.*)$', value=r'\1', regex=True)
        df[col] = df[col].apply(pd.to_numeric, errors='ignore')
    return df

def num_round(df):
    for col in df.columns:
        df[col] = df[col].round(decimals=2)
    return df



################################################################################ CROSS FEATURING
cross_featuring_candidates = ['cortisol','composé S','17OHP','Delta4A','Testostérone','Progestérone']
columns_to_drop = ['id']
categorical_features = ['sexe']
numerical_features = ['age'] # pas de overlap avec le cross features
numerical_transformer = Pipeline(steps=[
    ('num', FunctionTransformer(num_encoder)), 
    ('imputer', SimpleImputer(strategy='mean'))
    ])

def cross_features(data, strategy='all'):
    df = pd.DataFrame(data,columns=cross_featuring_candidates)
    df_ref=df.copy()
    for feature_i in df_ref.columns[:-1]:
        for feature_j in df_ref.columns[df_ref.columns.get_loc(feature_i)+1:]:
            if strategy == 'multiply':
                feature_name=feature_i+"x"+feature_j
                df[feature_name] = df[feature_i]*df[feature_j]
            elif strategy == 'divide':
                feature_name = feature_i+"/"+feature_j
                df[feature_name] = df[feature_i]/df[feature_j]
            else :
                feature_name_mult = feature_i+"x"+feature_j
                feature_name_div = feature_i+"/"+feature_j
                df[feature_name_mult] = df[feature_i]*df[feature_j]
                df[feature_name_div] = df[feature_i]/df[feature_j]
    return df

def cross_features_mult(data):
    return cross_features(data, strategy='multiply')

def cross_features_div(data):
    return cross_features(data, strategy='divide')

def cross_features_all(data):
    return cross_features(data, strategy='all')

def cross_features_pipeline(strategy='all'):
    if strategy == 'multiply':
        return Pipeline(steps=[("numerize", numerical_transformer),("cross_features", DataframeFunctionTransformer(cross_features_mult))])
    elif strategy == 'divide':
        return Pipeline(steps=[("numerize", numerical_transformer),("cross_features", DataframeFunctionTransformer(cross_features_div))])      
    else :
        return Pipeline(steps=[("numerize", numerical_transformer),("cross_features", DataframeFunctionTransformer(cross_features_all))])
    
crossfeatures_transformer = cross_features_pipeline(strategy='all')

################################################################################ NAME COLUMNS AFTER CROSS FEATURING

def column_names_out(X, columns_to_drop=None, categorical_features=None, cf_candidates=None, strategy='multiply', normalize=False):
    columns_in = list(X.columns)
    columns_out = list()
    if columns_to_drop != None:
        for column_drop in columns_to_drop:
            columns_in.remove(column_drop)
    
    if categorical_features != None:
        for column_feature in categorical_features:
            if len(X[column_feature].unique()) > 2:
                for val in X[column_feature].unique():
                    name = column_feature + "_" + val
                    columns_out.append(name)
            else:
                name = column_feature + "_" + X[column_feature].unique()[-1]
                columns_out.append(name)
                #columns_out.insert(columns_out.index(column_feature), name)
            columns_in.remove(column_feature)
    
    if len(columns_in) > 0:
        if normalize == True:
            columns_in = [col + "_norm" for col in columns_in]
        columns_out.extend(columns_in)
        
    if (cf_candidates != None) and (len(cf_candidates)>1):
        for feature_i in cf_candidates[:-1]:
            for feature_j in cf_candidates[cf_candidates.index(feature_i)+1:]:
                if strategy == 'multiply':
                    name=feature_i+"_x_"+feature_j
                    if normalize == True:
                        name+="_norm"
                    columns_out.append(name)
                elif strategy == 'divide':
                    if normalize == True:
                        name+="_norm"
                    name=feature_i+"_/_"+feature_j
                    columns_out.append(name)
                else:
                    name_mult = feature_i+"_x_"+feature_j
                    name_div = feature_i+"_/_"+feature_j
                    if normalize == True:
                        name_mult+="_norm"
                        name_div+="_norm"
                    columns_out.append(name_mult)
                    columns_out.append(name_div)
                   
    return columns_out