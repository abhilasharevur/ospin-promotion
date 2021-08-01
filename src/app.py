import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import orders
import customer
from orders import log
from summary import pd
from configparser import ConfigParser
from pathlib import Path

THIS_DIR = Path(__file__).parent
par_dir = THIS_DIR.parent


def config(filename='args.cfg'):
    # create a parser
    parser = ConfigParser()

    # read config file
    config_file = os.path.join(par_dir, "config", filename)
    parser.read(config_file)

    # get section, default to postgresql
    p_config = {}
    for section in parser.sections():
        params = parser.items(section)
        for param in params:
            p_config[param[0]] = param[1]

    for opt in ("input_path", "output_path"):
        p_config[opt] = os.path.join(par_dir, p_config[opt])
    return p_config


def get_orders(input_dir):
    """
    Read orders from csv file
    :param input_dir: "input"
    :return: pandas dataframe from the csv file
    """
    df = orders.main(input_dir)
    if df is not None:
        return df
    else:
        print("No input files")


def get_promo_results(order_df, promo_type, output_path):
    """
    Create customer object for each row and get the promotion results based on the type
    :param order_df: data (pandas dataframe) from the csv file
    :param promo_type: rebate_scheme
    :param output_path: "output/output.csv"
    :return: print to stdout and write to output.csv
    """
    try:
        customer_instances = [customer.CustomerPromo(promo_type, x.organ, x.cash,
                                                     x.price, x.bonus_ratio) for x in order_df.itertuples()]
        update_bonuses = list(map(lambda x: x.get_promo_results(), customer_instances))
        result_df = pd.DataFrame([t.__dict__ for t in customer_instances])
        print(result_df['bonus_to_receive'].to_string(index=False))

        # filter the columns and write the output to new csv file
        results = result_df[['organ', 'cash', 'price', 'bonus_ratio', 'bonus_to_receive']]
        results.to_csv(output_path, index=False)
    except Exception as err:
        print(err)
        log.error(err)


def main(input_directory, promotion_type, output_path):
    # get data from csv
    orders_data = get_orders(input_directory)
    get_promo_results(order_df=orders_data, promo_type=promotion_type, output_path=output_path)


if __name__ == "__main__":
    kwargs = config()
    input_dir = kwargs.pop('input_path')
    output_file = kwargs.pop('output_path')
    promo = kwargs.pop('promotion_type')
    main(input_directory=input_dir, promotion_type=promo, output_path=output_file)
