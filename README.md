Aim of this project is to build a system to see real time graph of ECG and EMG.
ECG is detected using AD8232 and EMG using Muscle Sensor V3 modules.
Modules are connected to patient using disposable adhesive electrodes.
A Raspberry Pi 4B has been used to read data from the ECG and EMG modules using ADS1115 ADC.
ADS1115 is a 16 bit ADC and is I2C enabled.
PyQT5 is used to display interactive real time signals.
