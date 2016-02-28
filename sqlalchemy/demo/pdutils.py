import pandas as pd


def currency_column_to_number(df, columns):
    if isinstance(columns, str):
        columns = [columns]
    for column in columns:
        df[column] = df[column].replace('[$,]', '', regex=True).astype(float)
