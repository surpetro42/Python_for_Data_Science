import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def graph(df0: pd.DataFrame, df1: pd.DataFrame):
    df_life_expectancy_data = df0["1900"]
    df_gdp = df1["1900"]

    plt.scatter(df_gdp, df_life_expectancy_data, label="1900")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.title("1900")

    plt.show()
    
def main():
    df0 = load("life_expectancy_years.csv")
    df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    graph(df0, df1)
    

if __name__ == "__main__":
    main()