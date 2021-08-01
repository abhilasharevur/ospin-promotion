#!/usr/bin/python3

import os.path
import argparse
from src.app import main as app_main


def run():
    parser = argparse.ArgumentParser()

    # command line arguments
    parser.add_argument(
        "--input-path",
        help="Absolute path to input directory where .csv files reside",
        # nargs="+",
        required=True
    )
    parser.add_argument(
        "--promotion-type",
        default=None,
        help="The type of promotion scheme",
    )
    parser.add_argument(
        "--output-path",
        help="Absolute path to output directory to store results",
        default="output/output.csv"
    )

    argvs = parser.parse_args()

    if validate_path_dir(argvs, "input_path"):
        arg_input_path = argvs.input_path

    if validate_path_file(argvs, "output_path"):
        arg_output_path = argvs.output_path

    arg_promotion_type = argvs.promotion_type

    if arg_promotion_type is None:
        print("please input promotion type")
    else:
        app_main(arg_input_path, arg_promotion_type, arg_output_path)


def validate_path_dir(argvs, opt):
    path_ = getattr(argvs, opt)
    if not os.path.isdir(path_):
        print("Directory path {} of {} does not exists".format(path_, opt))
        return False
    return True


def validate_path_file(argvs, opt):
    path_ = getattr(argvs, opt)
    if not os.path.isfile(path_):
        print("File path {} of {} does not exists".format(path_, opt))
        return False
    return True


if __name__ == '__main__':
    run()
