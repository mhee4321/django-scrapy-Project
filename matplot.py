import requests
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from weather.models import Weather
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from weather.models import Weather
import seaborn as sns


def matplotlib_graph():
    weather_df = pd.DataFrame(list(Weather.objects.all().values()))

    sns.lineplot(x='date', y='speed', data = weather_df)
    plt.show()
    plt.savefig('/Users/mhee4/cloud-project/static/img/')

    # df_line = pd.DataFrame(weather_df.groupby(['date']).count())
    # plt.bar(df_line.index, weather_df['deg'])
    # plt.savefig('/Users/mhee4/cloud-project/static/img/')

    # a = weather_df.boxplot(column="weather_df[temp_max]", by="weather_df[date]")

    # sns_hist = sns.displot(seoul_pop_df['date'])
    # fig = sns_hist.get_figure()
    # fig.savefig('/Users/mhee4/cloud-project/static/img/')
    
    

if __name__=='__main__':
    matplotlib_graph()