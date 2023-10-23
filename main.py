import requests
import json
import pandas as pd
from collections import ChainMap
from dotenv import load_dotenv
import os
import subprocess

url = 'https://www.themuse.com/api/public/jobs?page=50'
load_dotenv()

#get response from API
def api_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('Response Successful!')
    else:
        print('Request failed with status code: ', response.status_code)
    return response.json()


if __name__=='__main__':
    print('Reading API...')
    data = api_response(url)

    #publication date
    publication_date_list = [data['results'][x]['publication_date'] for x in range(len(data['results']))]
    publication_date = {'publication_date' : publication_date_list}

    #job title
    job_title_list = [data['results'][x]['name'] for x in range(len(data['results']))]
    job_title = {'job title': job_title_list}

    #job type
    job_type_list = [data['results'][x]['type'] for x in range(len(data['results']))]
    job_type = {'job type' : job_type_list }

    #location
    location_list = [data['results'][x]['locations'][0]['name'] for x in range(len(data['results']))]
    location = {'location' : location_list }

    #company
    company_list =[data['results'][x]['company']['name'] for x in range(len(data['results']))]
    company = { 'company name' : company_list }

    # merge the dictionaries with ChainMap and dict "from collections import ChainMap"
    data = dict(ChainMap(publication_date, job_title, job_type, location, company))
    df=pd.DataFrame.from_dict(data)

    # split location into city and county cols 
    df['city'] = df['location'].str.split(',').str[0]
    df['country'] = df['location'].str.split(',').str[1]
    df.drop('location', axis=1, inplace=True)

    df['publication_date'] = df['publication_date'].str[:10]

    df.to_csv('job2.csv', index=False)
    print('Dataframe saved to local')
    
    result = subprocess.run(['azcopy', 'copy', 'job2.csv', os.getenv('token')])

    if result.returncode == 0 :
        print('Upload successful!')
    else: 
        print('Upload failed with status: ', result.returncode)
