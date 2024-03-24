import base64
import sqlite3
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template
from get_fieldwatcher_dht11_data import get_fieldwatcher_data
from get_vandtank_dht11_data import get_vandtank_data

app = Flask(__name__)

def vandtank_temp():
    timestamps, temp, hum = get_vandtank_data(10)
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.set_facecolor("#fff")
    ax.plot(timestamps, temp, linestyle="dashed", c="#F11", linewidth="1.5", marker="o", ms="5")
    ax.set_xlabel("Timestamps")
    ax.set_ylabel("Temperature celsius")
    fig.patch.set_facecolor("#fff") 
    ax.tick_params(axis="x", colors="black")
    ax.tick_params(axis="y", colors="blue")
    ax.spines["left"].set_color("blue")
    ax.spines["right"].set_color("blue")
    ax.spines["top"].set_color("blue")
    ax.spines["bottom"].set_color("blue")
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def vandtank_hum():
    timestamps, temp, hum = get_vandtank_data(10)
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.set_facecolor("#fff")
    ax.plot(timestamps, hum, linestyle="dashed", c="#F11", linewidth="1.5", marker="o", ms="5")
    ax.set_xlabel("Timestamps")
    ax.set_ylabel("Humidity %")
    fig.patch.set_facecolor("#fff") 
    ax.tick_params(axis="x", colors="black")
    ax.tick_params(axis="y", colors="blue")
    ax.spines["left"].set_color("blue")
    ax.spines["right"].set_color("blue")
    ax.spines["top"].set_color("blue")
    ax.spines["bottom"].set_color("blue")
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def fieldwatcher_temp():
    timestamps, temp, hum = get_fieldwatcher_data(10)
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.set_facecolor("#fff")
    ax.plot(timestamps, temp, linestyle="dashed", c="#F11", linewidth="1.5", marker="o", ms="5")
    ax.set_xlabel("Timestamps")
    ax.set_ylabel("Temperature celsius")
    fig.patch.set_facecolor("#fff") 
    ax.tick_params(axis="x", colors="black")
    ax.tick_params(axis="y", colors="blue")
    ax.spines["left"].set_color("blue")
    ax.spines["right"].set_color("blue")
    ax.spines["top"].set_color("blue")
    ax.spines["bottom"].set_color("blue")
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def fieldwatcher_hum():
    timestamps, temp, hum = get_fieldwatcher_data(10)
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.set_facecolor("#fff")
    ax.plot(timestamps, hum, linestyle="dashed", c="#F11", linewidth="1.5", marker="o", ms="5")
    ax.set_xlabel("Timestamps")
    ax.set_ylabel("Humidity %")
    fig.patch.set_facecolor("#fff") 
    ax.tick_params(axis="x", colors="black")
    ax.tick_params(axis="y", colors="blue")
    ax.spines["left"].set_color("blue")
    ax.spines["right"].set_color("blue")
    ax.spines["top"].set_color("blue")
    ax.spines["bottom"].set_color("blue")
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vandtank')
def vandtank():
    vandtank_temperature = vandtank_temp() 
    vandtank_humidity = vandtank_hum()
    return render_template('vandtank.html', vandtank_temperature=vandtank_temperature, vandtank_humidity=vandtank_humidity)

@app.route('/fieldwatcher')
def fieldwatcher():
    fieldwatcher_temperature = fieldwatcher_temp()
    fieldwatcher_humidity = fieldwatcher_hum()
    return render_template('fieldwatcher.html', fieldwatcher_temperature=fieldwatcher_temperature, fieldwatcher_humidity=fieldwatcher_humidity)

@app.route('/DMI')
def dmi():
    return render_template('dmi.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
