import pandas as pd
import plotly.express as px
import base64
import os

# === File paths ===
excel_file = r"C:\Users\Malik\Desktop\PKODI.xlsx"
image_folder = r"C:\Users\Malik\Desktop\BatsmanImages"

# === Load data ===
df = pd.read_excel(excel_file)
df.columns = ["Batsman", "Average_SR", "Innings", "Runs"]
df = df.sort_values(by="Average_SR", ascending=False)

# === Helper to convert image to base64 ===
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# === Bar Chart (images at base) ===
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
    width=0.5
)
bar_fig.update_layout(xaxis_tickangle=-45, height=600)

# Place images at bottom
for i, row in df.iterrows():
    img_path = os.path.join(image_folder, f"{row['Batsman']}.png")
    if not os.path.exists(img_path):
        img_path = os.path.join(image_folder, f"{row['Batsman']}.jpg")
    if os.path.exists(img_path):
        encoded_img = img_to_base64(img_path)
        bar_fig.add_layout_image(
            dict(
                source=f"data:image/png;base64,{encoded_img}",
                x=row["Batsman"],
                y=0,  # bottom of chart
                xref="x",
                yref="y",
                sizex=0.8,
                sizey=5,  # fixed small height so uniform
                xanchor="center",
                yanchor="bottom",
                layer="above"
            )
        )

# === Bubble Chart (bigger images) ===
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
    height=600
)

# Place images inside bubbles (slightly larger)
for i, row in df.iterrows():
    img_path = os.path.join(image_folder, f"{row['Batsman']}.png")
    if not os.path.exists(img_path):
        img_path = os.path.join(image_folder, f"{row['Batsman']}.jpg")
    if os.path.exists(img_path):
        encoded_img = img_to_base64(img_path)
        bubble_fig.add_layout_image(
            dict(
                source=f"data:image/png;base64,{encoded_img}",
                x=row["Average_SR"],
                y=row["Runs"],
                xref="x",
                yref="y",
                sizex=6,  # increased
                sizey=60,  # increased
                xanchor="center",
                yanchor="middle",
                layer="above"
            )
        )

# === Save outputs ===
bar_output = r"C:\Users\Malik\Desktop\PKODI_bar_with_images_clean.html"
bubble_output = r"C:\Users\Malik\Desktop\PKODI_bubble_with_images_big.html"

bar_fig.write_html(bar_output)
bubble_fig.write_html(bubble_output)

print(f"Bar chart saved to: {bar_output}")
print(f"Bubble chart saved to: {bubble_output}")
