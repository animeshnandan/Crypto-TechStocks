# -*- coding: utf-8 -*-
"""BTC RUN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_QZAKxv4yVaoB3LfY3D_21tRrbrOKrrN
"""

# prompt: azure-iot-device and azure-iot-hub python libraries install

!pip install azure-iot-device
!pip install azure-iot-hub
!pip install azure.eventhub

import requests
import time
import json
from azure.eventhub import EventHubProducerClient, EventData

def fetch_bitcoin_price():
    # Define the API URL
    api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    # Send a GET request to the API
    response = requests.get(api_url)

    # Parse the response content as JSON if the request was successful
    data = response.json() if response.status_code == 200 else {}

    # Extracting USD data and timestamp
    usd_data = {
        'USD_price': float(data['bpi']['USD']['rate'].replace(',', '')) if 'bpi' in data and 'USD' in data['bpi'] else 'Unavailable',
        'timestamp': data['time']['updated'] if 'time' in data and 'updated' in data['time'] else 'Unavailable'
    }
    return usd_data

def send_to_event_hub(data):
    # Azure Event Hub connection details
    connection_str = "Endpoint=sb://btcstock.servicebus.windows.net/;SharedAccessKeyName=btcstockmanage;SharedAccessKey=5hY1IE5dBVjFmurqZy9ByrRh3x5htrvva+AEhChO0Ho=;EntityPath=btcstock"
    eventhub_name = "btcstock"

    # Create a producer client to send messages to the event hub
    producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=eventhub_name)
    event_data_batch = producer.create_batch()

    # Serialize the data to a JSON string and add it to the batch
    event_data_batch.add(EventData(json.dumps(data)))

    # Send the batch of events to the event hub
    with producer:
        producer.send_batch(event_data_batch)
        print("Bitcoin data sent to Event Hub")

def main():
    while True:
        # Fetch the Bitcoin price data
        data = fetch_bitcoin_price()

        # Send the fetched data to Azure Event Hub
        send_to_event_hub(data)

        # Wait for 30 seconds before fetching again
        time.sleep(30)

# Run the main function if this script is executed as the main program
if __name__ == "__main__":
    main()