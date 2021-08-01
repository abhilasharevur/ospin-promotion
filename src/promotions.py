import itertools
from orders import log


def rebate_scheme(organ_to_purchase=None, available_cash=None, product_price=None, bonus_ratio=None):
    # the bonus scheme
    bonus_scheme = {
        "heart": ["heart"],
        "liver": ["lung"],
        "lung": ["liver", "heart"]
    }
    # to store the results
    bonus_results = {
        "heart": 0,
        "liver": 0,
        "lung": 0
    }

    count_of_purchases = available_cash // product_price

    try:
        bonus_to_be_received = count_of_purchases // bonus_ratio
        bonus_results.update(zip(bonus_scheme[organ_to_purchase], itertools.repeat(bonus_to_be_received)))
        bonus_results[organ_to_purchase] += count_of_purchases
        results = ",".join("{} {}".format(*i) for i in bonus_results.items())
        return results

    except ZeroDivisionError as zerr:
        print("Number of purchases is zero")
        log.error(zerr)
    except Exception as err:
        print(err)
        log.error(err)
