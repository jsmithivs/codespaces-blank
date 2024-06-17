from datetime import datetime
import logging
import azure.functions as func
import requests


app = func.FunctionApp()

@app.schedule(schedule="0 0 0 * 1 1", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def agreement_auto_renewal(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


def get_inflation_rate():
    start_year = datetime.now().year
    end_year = start_year - 1

    url = f"https://api.bls.gov/publicAPI/v2/timeseries/data/CUUR0000SA0L1E?startyear={end_year}&endyear={start_year}&period=M"

    response = requests.get(url)

    data = response.json()

    if response.status_code != 200:
        print('Failed to get data:', data['message'][0])
        exit()

    if 'Series' not in data['Results']:
        print('No data found')
        exit()

    monthly_data = data['Results']['series'][0]['data']

    last_year_of_data = monthly_data[:13]

    inflation_rate = (float(last_year_of_data[0]['value']) - float(last_year_of_data[12]['value'])) / float(
        last_year_of_data[12]['value']) * 100

    return inflation_rate