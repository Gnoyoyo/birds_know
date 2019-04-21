#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def convert_text(inputFile, outputFile):
    date = ""
    time = ""
    name = ""
    message = ""
    seperator = " "
    delimiter = ","

    #Import TXT File
    #inputFile = "INPUT"
    inputFileType = ".txt"

    #Export as CSV File
    #outputFile = "OUTPUT"
    outputFileType = ".csv"

    dateFormat = re.compile('([12]\d{3}\.(0[1-9]|1[0-2])\.(0[1-9]|[12]\d|3[01]))') #10
    timeFormat = re.compile('(([0-1][0-9]|2[0-3])\:([0-5][0-9]))') #5


    file = open(inputFile + inputFileType , 'r', encoding = "utf-8")
    csv = open(outputFile + outputFileType ,'w', encoding = "utf-8")

    csv.write("date,time,name,message\n")
    text = file.readline().split()
    if len(text[0]) != 10:
        text[0] = text[0][1:]

    while len(text) != 0:

        if dateFormat.match(text[0]) is not None:
            date = text[0]
            text = file.readline().split()

        if timeFormat.match(text[0]) is not None:
            time = text[0]
            name = text[1]
            message = seperator.join(text[2:len(text)])
            text = file.readline().split()

        if len(text) != 0:
            while dateFormat.match(text[0]) is None and timeFormat.match(text[0]) is None:
                csv.write(date + "," + time + "," + name + "," + "\"" + message + "\"\n")
                message = seperator.join(text[0:len(text)])
                text = file.readline().split()

        csv.write(date + "," + time + "," + name + "," + "\"" + message + "\"\n")

    print("DONE")