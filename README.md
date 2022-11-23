
<h1 align="center"> Logs Pipeline </h1>

 <p align="left">
   <img src="https://img.shields.io/badge/STATUS-%20DEV-green">
</p>

# Introduction
Project consists of implementing a tool that is able to analyze log files containing online visits and collect a couple of metrics based on the aggregates in a Memory and CPU efficient way.
The way to ensure good data processing performance depending on the size of the data is to offset the data in the file. 
Therefore it is separated into Chunks with a choice of size.
The project consists of the following file packages:

- pipelines/pipeline.py: Initial execution of data processing
- pipelines/load.py: Loading data into chunks
- pipelines/process.py: Data processing according to timestamp time unit
- pipelines/tester.py: Invalid data analysis
- pipelines/data: File where the .csv file is stored
- tests/test_tester.py: Running of Unit Tests

# Requirements
- SO == Windows 10
- Python == 3.9.7
- Pip == 21.3.1

# Installation and Run

- Install python==3.9.7

        sudo apt update

        sudo apt install python3.9.7

        python --version

- Clone the repository

        git clone https://github.com/MiguelBarriosAl/logs-pipeline.git

- Run Unit Test
        
         python3 -m unittest .\tests\test_tester.py


- Run Pipeline
        
         python3 .\pipelines\pipeline.py

# A Simple Example


`python3 .\pipelines\pipeline.py`

    {'1667233287': 'early_buyers', '1667236947': 'buyers_lead'}
    {'1667233287': 'google', '1667236947': 'bbva'}
    {'1667233287': 'social', '1667236947': 'social'}

# Recommendations
In case of production the project is intended to introduce Multithreading in which it would consist of 4 threads.
One thread for each method (campaign, source, medium), and another one for false user analysis. 
