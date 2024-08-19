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
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
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
    df_bar = df.groupby(pd.Grouper(freq="M")).mean().reset_index()
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    print(df_bar)
    Months = ["January", "February", "March", "April", "June", "July", "August", "September", "October", "November", "December"]

    # Draw bar plot
    fig, axes = plt.subplots(figsize=(32, 10))
    sns.barplot(data=df_bar, x=df_bar.index, y=df_bar['value'], ax=axes)





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
