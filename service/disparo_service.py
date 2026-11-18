import pandas as pd
from random import randint

path_mock_file = 'base_dados/base_dados_api.csv'

df_mock = pd.read_csv(path_mock_file)

def mock_trigger():

    random_index = randint(0,df_mock.shape[1])
    return df_mock.iloc[random_index,:].to_dict()