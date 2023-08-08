##open ai controller class
import pandas as pd
import interface
import docParser
import apiHelper
import writer

#initialize interface
interData = interface.getDirection()

#send interface data to parser
df = docParser.parse(interData[0])

ap = apiHelper.aiHelper(interData[2])

#send parsed data to api helper
df['apiDecision'] = df['text'].apply(ap.askQuestion)
df = df.drop(columns=['text'])
#send api data to writer
print(df.head)

writer.write(interData[1], df)
