#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def convert_text():
    date = ""
    time = ""
    name = ""
    message = ""
    seperator = " "
    #Import TXT File
    inputFile = "INPUT"
    #Export as CSV File
    outputFile = "OUTPUT"
    dateFormat = re.compile('([12]\d{3}\.(0[1-9]|1[0-2])\.(0[1-9]|[12]\d|3[01]))')
        #10
    timeFormat = re.compile('(([0-1][0-9]|2[0-3])\:([0-5][0-9]))')
        #5
    file = open(inputFile+".txt", 'r', encoding = "utf-8")
    csv = open(outputFile+".csv",'w', encoding="utf-8")
    csv.write("date"+","+"time"+","+"name"+","+"message"+"\n")
    text = file.readline()
    data = text.split()
    while len(data) != 0:
        if dateFormat.match(data[0]) is not None:
            date = data[0]
            text = file.readline()
            data = text.split()
        if timeFormat.match(data[0]):
            time = data[0]
            name = data[1]
            message = seperator.join(data[2:len(data)])
            text = file.readline()
            data = text.split()
        else:
            message = message + seperator.join(data[0:len(data)])
            text = file.readline()
            data = text.split()
        csv.write(date+","+time+","+name+","+message+"\n")
    print("DONE")