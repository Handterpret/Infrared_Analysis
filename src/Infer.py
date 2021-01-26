import serial
import argparse
import time
import json
import numpy as np
import os
import datetime
from tensorflow import keras
import tensorflow as tf

parser = argparse.ArgumentParser()

parser.add_argument("--serial", default="COM7", help="Serial port to connect to for instance COM3 on windows or /dev/ttyUSB0 on Linux")
parser.add_argument("-b", "--baud", help="Baud rate for reading serial port", default="9600")
parser.add_argument("--model_path", help="Where model is saved", default=".")
parser.add_argument("--dataset_path", help="Where dataset is saved", default=None)

args = parser.parse_args()

def InferIRData(serialport, baud, model_folder, dataset_path):
    if dataset_path:
        labels_name = os.listdir(dataset_path)
    ser = serial.Serial(serialport, baud)
    model = keras.models.load_model(model_folder)
    while True:
        print("Reading data from serial port")
        line = ser.readline()
        data = eval(str(line).split("JSON")[1])
        message_number = str(line).split('Message')[1].split('JSON')[0]
        print(f"Message : {message_number}")
        retrieved_data = ParseJsonData(data)
        if dataset_path:
            print(f"result : {labels_name[tf.argmax(model.predict(tf.expand_dims(retrieved_data, axis=0)))]}\n")
        else:
            print(f"result : {model.predict(tf.expand_dims(retrieved_data, axis=0))}\n")

def ParseJsonData(json_data):
    """Parse Json from arduino

    Args:
        json_data (str): look like {'IR':[{'A':3, 'B':0, 'C':0, 'D':0, 'E':1, 'F':4, 'G':0, 'H':0, ...},...]}

    Returns:
        [np.array]: 3D array of containing slices with shape (n,len_diode,len_diode)
        with len_diode corresponding to number of diode defined in json
    """
    data_names = [chr(letter) for letter in range(65,65+len(json_data["IR"][0]))] # except data to be A,B,C ...
    one_led_array = np.array([])
    one_slice_array = np.array([])
    slices_array = np.array([])

    for led_array in json_data["IR"]:
            for letter in data_names:
                one_led_array = np.append(one_led_array, int(led_array[letter]))
            if one_slice_array.size == 0:
                one_slice_array = np.expand_dims(one_led_array, axis=0)
            else:
                one_slice_array = np.append(one_slice_array ,[one_led_array], axis=0)
            if one_slice_array.shape == (len(data_names), len(data_names)):
                if slices_array.size == 0:
                    slices_array =  np.expand_dims(one_slice_array, axis=0)
                else:
                    slices_array = np.append(slices_array, [one_slice_array], axis=0)
                one_slice_array = np.array([])
            one_led_array = np.array([])
    return slices_array


if __name__ == "__main__":
    InferIRData(args.serial, args.baud, args.model_path, args.dataset_path)