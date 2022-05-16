from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import csv
import time
import pandas as pd
import io
import matplotlib

app = Flask(__name__)



def get_datas():
    widhts = [(1, 4), (5, 8), (9, 10), (11, 16), (17, 24),
              (25, 35), (36, 46), (47, 50), (51, 58), (59, 63),
              (64, 71), (72, 81), (82, 91), (92, 101), (102, 109), (110, 118)]
    df = pd.read_fwf('ldp.dat', colspecs=widhts)
    return df


@app.route('/datas.png')
def datas_png():
    df = get_datas()
    fig = df.plot(kind="scatter", x="A", y="dW", xlim=(0, 300) , ylim=(-15, 10)).get_figure()
    output = io.BytesIO()
    fig.savefig(output, format="png")
    return output.getvalue(), 200, {"Content-Type": "image/png"}


@app.route('/datas1.png')
def datas1_png():
    df = get_datas()
    fig = df.plot(kind="scatter", x="A", y="ainf ", c ="aerr" ,xlim=(0, 250) , ylim=(5, 25)).get_figure()
    output = io.BytesIO()
    fig.savefig(output, format="png")
    return output.getvalue(), 200, {"Content-Type": "image/png"}

@app.route('/')
def index():
    df = get_datas()
    return render_template("index.html", title="Midterm Exercise", datas = df.to_html())



if __name__=="__main__":
    app.run()
