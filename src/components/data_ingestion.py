import os
import sys
from src.exception import Custom_Exception
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

import pandas as pd

@dataclass
class DataIngestion_Config:
    train_data_path : str = os.path.join('artifacts', 'train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.Ingestion_Config = DataIngestion_Config()
        
    def Initiate_DataIngestion(self):
        logging.info('Entered the data ingestion config or method')
        try:
            df = pd.read_csv('college_student.csv')
            logging.info('Reading Dataset as Dataframe')
            
            os.makedirs(os.path.dirname(self.Ingestion_Config.train_data_path), exist_ok=True)
            df.to_csv(self.Ingestion_Config.raw_data_path, index = False, header = True)
            
            logging.info('Train,Test,Split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.Ingestion_Config.train_data_path, index = False, header = True)
            test_set.to_csv(self.Ingestion_Config.test_data_path, index = False, header = True)
            
            logging.info('Ingestion of the data is completed')
            
            
            return(
                self.Ingestion_Config.train_data_path,
                self.Ingestion_Config.test_data_path
            )
        
        except Exception as e:
                raise Custom_Exception(e, sys)
            

if __name__ == "__main__":
    obj = DataIngestion()
    obj.Initiate_DataIngestion()