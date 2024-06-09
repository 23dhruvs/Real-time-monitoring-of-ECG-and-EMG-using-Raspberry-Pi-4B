import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
import RPi.GPIO as GPIO
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create ADC object
ads = ADS.ADS1115(i2c, data_rate = 860)
ads.gain = 1

# Single-ended input channel 0
ch = AnalogIn(ads, ADS.P0)

# Initialize plotting window
app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('Real-time Plot')
plot = win.addPlot(title='Voltage vs. Time')
curve = plot.plot(pen='y')

# Data storage for plotting
x_data = []
y_data = []

# Main loop
def update_plot():
    global x_data, y_data
    # Read the voltage value
    voltage = ch.voltage
    print(voltage)
    # Record the timestamp
    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch() / 1000
    # Add data to the time domain plot
    x_data.append(timestamp)
    y_data.append(voltage)
    # Update the time domain plot
    curve.setData(x_data, y_data)
    plot.setLabel('bottom', 'Time (s)')
    plot.setLabel('left', 'Voltage (V)')
    
    # Update x-axis range to show only the most recent data
    plot.setXRange(max(0, timestamp - 10), timestamp)

# Create a QTimer to update the plot
timer = QtCore.QTimer()
timer.timeout.connect(update_plot)
timer.start(100)  # Interval in milliseconds

# Start the application event loop
app.exec_()

# Cleanup GPIO
GPIO.cleanup()
