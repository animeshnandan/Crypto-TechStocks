# Real-Time Stock and Cryptocurrency Dashboard

## Overview

This project involves the development of a real-time data visualization dashboard for monitoring stock prices and trading volumes of Apple and Microsoft, as well as Bitcoin prices. The dashboard is built using Azure services, including Event Hub, Blob Storage, Stream Analytics, and Power BI, to provide accurate and timely insights into market trends.

## Features

- **Real-Time Data Visualization**: Display live stock prices, trading volumes, and Bitcoin prices using Power BI.
- **Azure Event Hub**: Ingest real-time data streams from various sources.
- **Azure Stream Analytics**: Process and aggregate stock and cryptocurrency data.
- **Azure Blob Storage**: Store processed data for further analysis.
- **SQL Queries**: Aggregate and cast data for structured analysis.
- **Power BI Integration**: Create interactive dashboards for data visualization.

## Architecture

1. **Data Ingestion**: Real-time data is ingested through Azure Event Hub from multiple sources including stock markets and cryptocurrency exchanges.
2. **Data Processing**: Azure Stream Analytics processes the ingested data, converting and aggregating it into a usable format.
3. **Data Storage**: Processed data is stored in Azure Blob Storage for persistence and further analysis.
4. **Data Visualization**: Power BI is used to create interactive dashboards that visualize the real-time data for end-users.

## Project Structure

- `aapl_run.py`: Script for processing Apple stock data.
- `msft_run.py`: Script for processing Microsoft stock data.
- `btc_run.py`: Script for processing Bitcoin data.
- `QUERIES.txt`: SQL queries for data aggregation and processing.

- `INST751 Final Screenshot.png`: Screenshot of the final dashboard.

![INST751 Final Screenshot](https://github.com/animeshnandan/Crypto-TechStocks/assets/83339335/10c1ed22-67f2-4eb9-ade0-e72e0ceb03bc)


## SQL Queries

The project utilizes the following SQL queries to process and aggregate the data:

```sql
SELECT
    datetime, CAST([open] AS FLOAT) AS [open], CAST([high] AS FLOAT) AS [high], CAST([low] AS FLOAT) AS [low],
    CAST([close] AS FLOAT) AS [close], CAST([volume] AS [FLOAT]) AS [volume], EventProcessedUtcTime, partitionId, EventEnqueuedUtcTime
INTO
    [aapl-output]
FROM
    [aaplstock];

SELECT
    datetime, CAST([open] AS FLOAT) AS [open], CAST([high] AS FLOAT) AS [high], CAST([low] AS FLOAT) AS [low],
    CAST([close] AS FLOAT) AS [close], CAST([volume] AS [FLOAT]) AS [volume], EventProcessedUtcTime, partitionId, EventEnqueuedUtcTime
INTO
    [msft-output]
FROM
    [msftstock];

SELECT
    *
INTO
    [outputbtc]
FROM
    [btcstock];
```

## Getting Started

To get started with the project, follow these steps:

1. **Set up Azure Services**:
    - Create Azure Event Hub instances for data ingestion.
    - Set up Azure Stream Analytics jobs to process the data streams.
    - Configure Azure Blob Storage for data storage.
    - Integrate with Power BI for data visualization.

2. **Deploy Scripts**:
    - Deploy the `aapl_run.py`, `msft_run.py`, and `btc_run.py` scripts to ingest and process data from respective sources.

3. **Configure SQL Queries**:
    - Use the SQL queries provided in `QUERIES.txt` to aggregate and cast the data within Azure Stream Analytics.

4. **Build Power BI Dashboards**:
    - Create interactive Power BI dashboards to visualize the real-time data.

## Usage

Once everything is set up, the system will continuously ingest, process, and visualize real-time data from the configured sources. You can access the Power BI dashboards to monitor the stock prices, trading volumes, and Bitcoin prices in real-time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Azure Event Hub for real-time data ingestion.
- Azure Stream Analytics for data processing.
- Azure Blob Storage for data storage.
- Power BI for data visualization.

For any questions or support, please contact [your email address].

---

This README provides a comprehensive overview of the project, guiding users through the setup and usage of the real-time stock and cryptocurrency dashboard.
