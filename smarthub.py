
# A very simple Flask Hello World app for you to get started with...
import os
from flask import Flask, render_template, request, url_for, redirect

#====================
smart_status = "off"
led_status = "on"
alarm_status = "off"
indoor_status = "off"


#=====================
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('detail.html')

@app.route('/detail/<name>')
def detail(name):
    normal = led_status
    smart = smart_status

    if name == "ALARM":
        normal = alarm_status
    elif name == "INDOOR":
        normal = indoor_status

    return render_template("config.html", name=name, normal=normal, smart=smart)

@app.route('/config', methods=['POST'])
def configure():
    device = request.form['hidden_data']

    if device == "LED":
        global led_status
        global smart_status
        led_status = request.form['normal']
        smart_status = request.form['smart']
    elif device == "ALARM":
        global alarm_status
        alarm_status = request.form['normal']
    else:
        global indoor_status
        indoor_status = request.form['normal']
        return redirect(url_for('detail', name='INDOOR'))

    return redirect(url_for('home'))

@app.route('/led', methods=['GET'])
def led():
    result = 'return:led' + led_status + ":smart" + smart_status
    return result

@app.route('/alarm', methods=['GET'])
def alarm():
    result = 'return:alarm' + alarm_status
    return result

@app.route('/indoor', methods=['GET'])
def indoor():
    result = 'return:indoor' + indoor_status
    return result

