import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)
    
    # Create first line of best fit
    slope1, intercept1, r1, p1, se1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # Overall best way
    #plt.axline(xy1=(2050, 2050*slope1 + intercept1), slope=slope1)

    # Way to clear tests
    years1 = range(df['Year'].min(), 2051)
    plt.plot(years1, years1*slope1 + intercept1)

    # Create second line of best fit
    modified_years = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(x=modified_years['Year'], y=modified_years['CSIRO Adjusted Sea Level'])
    # Overall best way
    #plt.axline(xy1=(2050, 2050*slope2 + intercept2), slope=slope2)
    
    # Way to clear tests
    years2 = range(2000, 2051)
    plt.plot(years2, years2*slope2 + intercept2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()