import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# === File path ===
file_path = r"C:\Users\Malik\Desktop\PKODI.xlsx"

# === Load Excel Data ===
df = pd.read_excel(file_path)

# Ensure correct column names
df.columns = ["Batsman", "Average_SR", "Innings", "Runs"]

# Sort by Average_SR (Strike Rate) descending
df = df.sort_values(by="Average_SR", ascending=False)

# === Bar Chart: Strike Rates ===
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
bar_fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
bar_fig.update_layout(xaxis_tickangle=-45, height=500)

# === Bubble Chart: Runs vs SR ===
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
bubble_fig.update_layout(height=500)

# === Combine into Dashboard Layout ===
dashboard = make_subplots(
    rows=2, cols=1,
    subplot_titles=("Strike Rates Sorted (High → Low)", "Runs vs Strike Rate"),
    vertical_spacing=0.15
)

# Add bar chart to row 1
for trace in bar_fig.data:
    dashboard.add_trace(trace, row=1, col=1)

# Add bubble chart to row 2
for trace in bubble_fig.data:
    dashboard.add_trace(trace, row=2, col=1)

dashboard.update_layout(height=1000, showlegend=False)

# === Save and Show ===
output_file = r"C:\Users\Malik\Desktop\PKODI_dashboard.html"
dashboard.write_html(output_file)
print(f"Dashboard saved to {output_file}")
dashboard.show()
