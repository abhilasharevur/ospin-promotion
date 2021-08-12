import os
import pandas as pd
from multiprocessing import Pool
from summary import Summary
from functools import partial
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    level=logging.INFO
)

log = logging.getLogger(__name__)


def job(instance, func):
    try:
        data = getattr(instance, func)()
        return data
    except AttributeError:
        print(instance, " doesn't have attribute-", func)


def main(input_dir):
    """
    Create Summary instances for each csv file
    :param input_dir: path to input directory which can have multiple files
    :return: returns combined pandas dataframe
    """
    try:
        # get list of filenames
        files = os.listdir(input_dir)
        file_list = []
        for file_name in files:
            if os.path.isfile(input_dir+"/"+file_name):
                if file_name.split('.')[1] == 'csv':
                    file_list.append(input_dir + "/" + file_name)
        #file_list = [input_dir + "/" + file_name for file_name in files if file_name.split('.')[1] == 'csv']
        instances = [Summary(i) for i in file_list]

        # set up your pool or whatever your hardware can support
        with Pool() as pool:
            # have your pool map the file names to dataframes
            df_list = pool.map(partial(job, func="get_df"), instances)

            # reduce the list of dataframes to a single dataframe
            combined_df = pd.concat(df_list, ignore_index=True)
        return combined_df
    except FileNotFoundError as f_err:
        print("Input files not found")
        log.error(f_err)
    except IndexError as i_err:
        print(i_err)
        log.error(i_err)
