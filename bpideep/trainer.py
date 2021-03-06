from bpideep.getdata import getjson, getfulldata
from bpideep.encoders import FeatEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.metrics import classification_report
import numpy as np
import joblib
# import pandas as pd


class Trainer():

    def __init__(self, X, y):
        '''
        instantiate trainer object with X and y
        '''
        self.pipeline = None
        self.X = X
        self.y = y


    def set_pipeline(self):
        '''
        create the pipeline and logisticregression model
        '''

        ratio_transformer = make_pipeline(
                                SimpleImputer(missing_values=np.nan, strategy='mean'),
                                RobustScaler())

        patent_transformer = make_pipeline(
                                SimpleImputer(missing_values=np.nan, strategy='constant', fill_value = 0),
                                RobustScaler())

        features_transformer = ColumnTransformer(
            [("ratio_preproc", ratio_transformer, ['funding_employees_ratio', 'stage_age_ratio']),
             ("patents_preproc", patent_transformer, ['nb_patents'])], remainder = 'passthrough')


        pipemodel = Pipeline(steps=[
                            ('featureencoder', FeatEncoder()),
                            ('features', features_transformer),
                            ('model', LogisticRegression(penalty = 'l1', C = 1.52))]
                            )
        self.pipeline = pipemodel


    def train(self):
        self.set_pipeline()
        self.pipeline.fit(self.X, self.y)


    def save_model(self):
        '''
        Save the model into a .joblib
        '''
        joblib.dump(self.pipeline, 'bpideepmodel.joblib')
        print("bpideepmodel.joblib saved locally")



if __name__ == "__main__":

    # importing data
    company_dict = getjson('deeptech.csv', 'non_deeptech.csv', 'almost_deeptech.csv')
    X, y = getfulldata(company_dict, 'fields_list.txt')

    t = Trainer(X, y)
    t.train()
    t.save_model()
