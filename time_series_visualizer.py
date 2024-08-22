import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# DO THIS FIRST pip install seaborn --upgrade

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')
print(df.info())
print(df.head())

# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
print(df.info())
print(df.head())

def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(32, 10))
    sns.lineplot(data=df, x=df.index, y=df['value'], ax=axes) 
    
    # Setting the title of the figure
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Labeling the x-axis
    axes.set_xlabel('Date')
    # Labeling the y-axis
    axes.set_ylabel('Page Views')  
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Extracting month and year from index
    df_copy = df.copy()
    df_copy['month'] = df_copy.index.month
    df_copy['year'] = df_copy.index.year
    df_bar = df_copy.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()
    print(df_bar)
    
    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, figsize=(13, 6), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    print(df_box)

    # Define the order of months
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))
    sns.boxplot(data=df_box, x=df_box['year'], y=df_box['value'], ax=ax1)
    # Setting the title of the figure
    ax1.set_title('Year-wise Box Plot (Trend)')
    # Labeling the x-axis
    ax1.set_xlabel('Year')
    # Labeling the y-axis
    ax1.set_ylabel('Page Views')  


    sns.boxplot(data=df_box, x=df_box['month'], y=df_box['value'], ax=ax2, order=month_order)
    # Setting the title of the figure
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    # Labeling the x-axis
    ax2.set_xlabel('Month')
    # Labeling the y-axis
    ax2.set_ylabel('Page Views')  




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
