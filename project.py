import pandas
import plotly.express

data_frame = pandas.read_csv("data.csv")
figure = plotly.express.scatter(data_frame, x = "Dates", y="Cases", color = "Country",)
figure.show()