# here we create:
    # - API calls functions (possibly several depending on needs)
    # - each function returns a df

import pandas as pd
import requests
import os

APIKEY = os.environ.get('DEALROOMAPIKEY')
URL = 'https://api.dealroom.co/api/v1'

print(APIKEY)
# def getbatchdata(company_id_list, fields) :
#     response = requests.get(
#                         url = f"{URL}/companies/batch?ids={company_id_list}&fields={fields}",\
#                         auth = (APIKEY, '')

#                         )
#     return response.json()

# for loop in order to iterate by batch on the csv file
