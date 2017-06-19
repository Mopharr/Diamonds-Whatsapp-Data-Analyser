import re
import csv
import time
import pandas as pd
import dateutil
import matplotlib.pyplot as plt
import seaborn as sns

file = open('DiamondsChat.txt', 'r')
data_file = file.read()
file.close()

my_data = []
data_found = re.findall('(\d+/\d+/\d+,\s+\d+\:\d+)\s+\-\s(\w+\s\w+\s\w+|\w+\s\w+|\w+)\:(.*)', data_file)

df = pd.DataFrame(data_found, columns = ['DateTime', 'Sender', 'Message'])
#df['Number of Messages Sent'] = ''

bigdemmy =  df[df['Sender'] == 'Bigdemmy']['Message']
print  bigdemmy
