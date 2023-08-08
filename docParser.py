#parser
import pandas as pd


def parse(filePath):
    ret = pd.read_csv(filePath, sep='\t' ,usecols= ['id','text'])
    return ret