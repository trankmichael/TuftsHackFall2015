import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('data/hotel_review_sent.csv')

sentiment = df['sentiment'].tolist()
rating = df['rating'].tolist()

trace0 = go.Scatter(
    x=sentiment,
    y=rating
)
data = [trace0]
plot_url = py.plot(data, filename='sentiment')