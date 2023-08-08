#apiHelper
import openai
import time


class aiHelper():
    def __init__(self,question):
        self.question = question

    #come back to fix this!
    def askQuestion(self,text):
        time.sleep(1.05) #wait to avoid exceeding usage limit
        openai.api_key = open("M:/divin/ReposHard/pharma mergers/key.txt").read()
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {   "role": "system", "content": "responses cannot be more than one letter long"},
            {   "role": "user", "content": text + "\n" + self.question}
            ],
            max_tokens=1
        )

        return response['choices'][0]['message']['content']