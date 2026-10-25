import numpy as np
import matplotlib as plt
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

import os

from io import StringIO

from jedi.api import file_name


#def Read(name):
#    file_path = filedialog.askopenfilename(title="Select a File",
#                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
#    file_Name = os.path.split(file_path)[1].split('.')[0]

#    if str(file_Name) == name:

#        with open(file_path, 'r') as file:
#            file_content = ''
#            txt = file.read()
#        return txt

#    else:
#        raise Exception("File mismatch")




def Load_DNA_Seq():
    with open(
        r"genomic_dna.txt",
        "r"
    ) as file:
        DNA_Seq = file.read().strip()

    print("Original DNA_Seq \n" + str(DNA_Seq))

    return DNA_Seq

def Load_introns():
    with open(
        r"introns.txt",
        "r"
    ) as file:
        introns = file.read()

    for intron in introns.split("\n"):
        print(intron)

    return np.loadtxt(
        StringIO(introns),
        delimiter=",",
        dtype=int,
        ndmin=2
    )

def ExcludeIntrons():
    introns_indices = Load_introns()
    DNA = Load_DNA_Seq()

    DNA_modified = ""
    current_index = 0

    for intron in introns_indices:
        start = intron[0]
        end = intron[1]

        # Convert 1-based inclusive coordinates to Python slicing
        DNA_modified += DNA[current_index:start-1]
        current_index = end

    DNA_modified += DNA[current_index:]

    print(DNA_modified)
    return DNA_modified

ExcludeIntrons()



