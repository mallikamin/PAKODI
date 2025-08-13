import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

# === File path ===
file_path = r"C:\Users\Malik\Desktop\PKODI.xlsx"

# === Load Excel Data ===
df = pd.read_excel(file_path)
df.columns = ["Batsman", "Average_SR", "Innings", "Runs"]

# Sort by Strike Rate descending
df = df.sort_values(by="Average_SR", ascending=False)

# === Bar Chart: Strike Rates (Thinner Bars) ===
bar_fig = px.bar(
    df,
    x="Batsman",
    y="Average_SR",
    text="Average_SR",
    title="Pakistan ODI Strike Rates (2024-Present, Min 100 Runs)",
    labels={"Average_SR": "Average Strike Rate", "Batsman": "Player"},
    color="Average_SR",
    color_continuous_scale="Blues"
)
bar_fig.update_traces(
    texttemplate='%{text:.1f}', 
    textposition='outside',
    width=0.5  # thinner bars
)
bar_fig.update_layout(
    xaxis_tickangle=-45,
    height=500
)

# === Bubble Chart: Runs vs SR with Updated Axis Labels ===
bubble_fig = px.scatter(
    df,
    x="Average_SR",
    y="Runs",
    size="Innings",
    color="Batsman",
    text="Batsman",
    title="Runs vs Strike Rate (Bubble size = Innings)",
    hover_data={"Innings": True, "Average_SR": True, "Runs": True}
)
bubble_fig.update_traces(textposition="top center")
bubble_fig.update_layout(
    xaxis_title="Strike Rate (Year: 2024-25)",
    yaxis_title="Aggregate Runs (Year: 2024-25)",
    height=500
)

# === Save individual visuals ===
bar_fig.write_html(r"C:\Users\Malik\Desktop\PKODI_bar_chart.html")
bubble_fig.write_html(r"C:\Users\Malik\Desktop\PKODI_bubble_chart.html")

print("Bar chart and bubble chart saved!")
