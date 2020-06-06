import pandas as pd 
import requests 
from datetime import datetime, timedelta
from pytz import timezone
import re

clean = re.compile('.*(?=,)')

def centralnow():
    central = timezone('US/Central')
    return datetime.now(tz=central)

def last_30_days():
    df = pd.DataFrame(columns=['date_time','stream_flow','gage_height'])

    now = centralnow()
    end = datetime.strftime(now, '%Y-%m-%dT00:00:00%z')

    start_dt = now + timedelta(days=-30)
    start = datetime.strftime(start_dt, '%Y-%m-%dT00:00:00%z')

    base_url = 'https://waterservices.usgs.gov/nwis/iv/'

    payload = {
        'format': 'json',
        'indent': 'on',
        'sites': '07164500',
        'startDT': start,
        'endDT': end,
        'parameterCd': '00060,00065',
        'siteStatus': 'all'
    }

    r = requests.get(base_url,params=payload)

    data = r.json()
    results = data['value']['timeSeries']
    for variable in results:
        variable_name = clean.match(variable['variable']['variableName']).group()
        values = variable['values'][0]['value']
        dates = []
        info = []
        for v in values:
            dates.append(v['dateTime'])
            info.append(v['value'])
        if (variable_name == 'Streamflow'):
            df.stream_flow = info
            df.date_time = dates
        if (variable_name == 'Gage height'):
            df.gage_height = info

    print(df.head())