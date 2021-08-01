# ospin-promotion

For every .csv files in the input directory, create a Summary object. Using multiprocessing.pool create a pool for each 
Summary object and read the csv file using *Pandas* library. *Pandas* creates dataframe for each csv file, and combines 
them into one dataframe. Create a customer class for each order (not required in this coding challenge) which can help save 
information for each customer, and gives the flexibility to performs actions on single customer. Based on user's input 
on promotions type, calculate the results.

### Library

Pandas library is used to read csv and convert into dataframe. More info - https://github.com/pandas-dev/pandas


### Requirement

```
>>> pip install -r requirements.txt
```

### Run

Two ways to run the application-
1. Using command line with options
```
>>> python ./main.py --input-path input --promotion-type rebate_scheme --output-path output/output.csv
```
- *<ins>:param</ins>* --input-path : Absolute path to input directory where .csv files reside
- *<ins>:param</ins>* --promotion-type : Type of promotion
- *<ins>:param</ins>* --output-path : Absolute path to output file to store results ``` not mandatory ```

2. Using .cfg file

Update configuration in config/args.cfg file
```
>>> python -m src.app
```

#### Results

The application prints the output as required to stdout. Also, the application writes the output to output/output.csv 
file as well. Currently, it just prints the columns *organ, cash, price, bonus_ratio, bonus_results*. The **big_orders.csv**
contains orders of million count. To test with this file, move the file to **_input_** directory and run the application.
