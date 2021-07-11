import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
df.reset_index(inplace=True)

# Clean data
df = df[(df['value']>=df['value'].quantile(0.025))& (df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df_line=df.copy()
    x= df_line.index.values
    y= df_line['value'].values
    fig,ax=plt.subplots(figsize=(10,5))
    plt.plot(x,y,color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel("Date")
    plt.ylabel("Page Views")





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year']=[d.year for d in df_bar.date]
    df_bar['Month']=[d.strftime('%b') for d in df_bar.date]
    df_bar=df_bar.groupby(['Year','Month'])['value'].mean()
    df_bar=df_bar.unstack()
    #label=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig=df_bar.plot(kind='bar', legend=True,figsize=(10,5)).figure
    plt.legend(title="Months", labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xlabel("Years")
    plt.ylabel('Average Page Views')




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
    fig,ax=plt.subplots(1,2,figsize=(10,5))
    sns.boxplot(data=df_box,x='year',y='value',ax=ax[0])
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_box,x='month', y='value', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],ax=ax[1])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
