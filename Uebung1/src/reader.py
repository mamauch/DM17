# -*- coding: utf-8 -*-
# Class gets a path to a csv file
# open this file as a csv

class reader:

    def __init__(self, pathToFile):
        self.pathToFile = pathToFile

    def readConvertCsv(self):
        import pandas as pd
        import numpy as np
        import os

        os.path.exists(self.pathToFile)

        df = pd.read_csv(self.pathToFile, header=None)

        return df
