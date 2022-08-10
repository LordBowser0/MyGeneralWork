import pandas as pd
import plotly.express as px

print('Hello World')
df = pd.read_csv('https://github.com/LordBowser0/MyGeneralWork/blob/main/Housing.csv')
df.sort_values(by='price')
print(df)
fig = px.line(df, x='price', y='area', title='area dependent on price ')
fig.show()


def importdata(data):
    df = pd.read_csv(data)
    print(df)


def scatterplot(xaxis, yaxis, name):
    plot = px.scatter(df, x=xaxis, y=yaxis, title=name)
    plot.show()


def lineplot(xaxis, yaxis, name):
    df.sort_values(by=xaxis)
    plot = px.line(df, x=xaxis, y=yaxis, title=name)
    plot.show()
