#writer

import pandas as pd

#writes a dataframe to a tsv file
def write(filePath, df):
    df.to_csv(filePath, sep='\t', index = False)
    
