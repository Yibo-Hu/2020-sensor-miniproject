#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).
It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.
Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import json
from datetime import datetime
import typing as T
import numpy as np
from matplotlib import pyplot as plt

def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:
    temperature = {}
    occupancy = {}
    co2 = {}
    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])
            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}
    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }
    return data

if __name__ == "__main__":
    file = Path(r'C:\Users\lh\PycharmProjects\pythonProject\sp_iotsim\YiboHu_DataLogger.txt')
    data = load_data(file)
    temp_val_temperature_lab1 = data['temperature']['lab1']
    check_sensor_isnan = np.isnan(temp_val_temperature_lab1)
    print('The number of logged value of temperature in lab1 is '+
          str(len(temp_val_temperature_lab1) - np.count_nonzero(temp_val_temperature_lab1 != temp_val_temperature_lab1)))
    print('The sum of temperature in lab1 is '+ str(np.nansum(temp_val_temperature_lab1)))
    print('The mean value of temperature in lab1 is '+str(np.nanmean(temp_val_temperature_lab1)))
    print('The variance of temperature in lab1 is ' + str(np.nanvar(temp_val_temperature_lab1)))

    temp_val_occupancy_lab1 = data['occupancy']['lab1']
    print('The number of logged value of occupancy in lab1 is ' +
          str(len(temp_val_occupancy_lab1) - np.count_nonzero(temp_val_occupancy_lab1 != temp_val_occupancy_lab1)))
    print('The sum of occupancy in lab1 is ' + str(np.nansum(temp_val_occupancy_lab1)))
    print('The mean value of occupancy in lab1 is ' + str(np.nanmean(temp_val_occupancy_lab1)))
    print('The variance of occupancy in lab1 is ' + str(np.nanvar(temp_val_occupancy_lab1)))

    temp_val_co2_lab1 = data['co2']['lab1']
    print('The number of logged value of co2 in lab1 is ' +
          str(len(temp_val_co2_lab1) - np.count_nonzero(temp_val_co2_lab1 != temp_val_co2_lab1)))
    print('The sum of co2 in lab1 is ' + str(np.nansum(temp_val_co2_lab1)))
    print('The mean value of co2 in lab1 is ' + str(np.nanmean(temp_val_co2_lab1)))
    print('The variance of co2 in lab1 is ' + str(np.nanvar(temp_val_co2_lab1)))

    temperature_pdf = pandas.Series(temp_val_temperature_lab1)
    temperature_pdf.plot(kind="kde")
    occupancy_pdf = pandas.Series(temp_val_occupancy_lab1)
    occupancy_pdf.plot(kind="kde")
    co2_pdf = pandas.Series(temp_val_co2_lab1)
    co2_pdf.plot(kind="kde")
    axes = plt.gca()
    axes.set_xlim([0, 30])
    plt.show()

    
    #for k in data:
        # data[k].plot()
        #time = data[k].index
        #data[k].hist()
        #plt.figure()
        #plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
        #plt.xlabel("Time (seconds)")
    #plt.show()
