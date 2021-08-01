import pandas as pd


class Summary:
    def __init__(self, data):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.df = pd.read_csv(data)

    def get_df(self):
        return self.df

    def print_head(self, rows=5):
        return self.df.head(rows)

    def get_columns(self):
        return list(self.df.columns)

    def get_length(self):
        return {'Rows': len(self.df), 'Columns': len(list(self.df.columns))}

    def get_stats(self):
        return self.df.describe()
