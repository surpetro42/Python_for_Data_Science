import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def graph(df: pd.DataFrame):
    """Display life expectancy projections for Armenia."""
    country = df.loc["Armenia"]
    years = country.index.astype(int)
    life_expectancy = country.values
    plt.title("Armenian Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.plot(years, life_expectancy)
    plt.show()
    print(country.index)
    print(country.index.dtype)


def main():
    """Load the life expectancy dataset and display the graph."""
    df = load("life_expectancy_years.csv")
    graph(df)


if __name__ == "__main__":
    main()
