import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load your processed data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
daily_sales = df.groupby("date")["sales"].sum().reset_index()

fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Total Daily Sales of Pink Morsels"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)