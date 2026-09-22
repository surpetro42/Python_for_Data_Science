import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def convert_population(value):
    """Convert population values from k or M to a number."""
    if value.endswith("k"):
        return float(value[:-1]) * 1000
    if value.endswith("M"):
        return float(value[:-1]) * 1000000
    else:
        return(float(value))


def graph(df: pd.DataFrame):
    """Display population projections for Armenia and France."""
    country_Armenia = df.loc["Armenia"]
    country_France = df.loc["France"]

    new_country_Armenia = country_Armenia.loc["1800":"2050"]
    new_country_France = country_France.loc["1800":"2050"]

    years_arm = new_country_Armenia.index.astype(int)
    years_frc = new_country_France.index.astype(int)

    population_arm = new_country_Armenia.apply(convert_population)
    population_frc = new_country_France.apply(convert_population)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.plot(years_arm, population_arm, label="Armenia")
    plt.plot(years_frc, population_frc, label="France")
    plt.legend()
    plt.show()



def main():
    """Load the population dataset and display the graph."""
    df = load("population_total.csv")
    graph(df)

if __name__ == "__main__":
    main()
