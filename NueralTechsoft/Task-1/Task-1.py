
import pandas as pd

### import file, read data, converted data col as time serise data and sort according to time
raw_data = pd.read_csv("./RELIANCE.NS.csv")
raw_data['Date'] =  pd.to_datetime(raw_data['Date'])
data = raw_data.sort_values(by='Date',ascending = False)


### Take input from User
try:
    numberOfDays = int(input())
except:
    numberOfDays = 10


### Simple Moving Average Calculation
data['SMA'] = data['Close'].rolling(numberOfDays).mean()
data = data.dropna(axis=0)


### 2. Standard deviation Calculation
data['STD_DEV'] = data['SMA'].rolling(numberOfDays).std()
data = data.dropna(axis=0)

### 3. UB and LB calculation.
data["UB"] = data['SMA'] + 2*data["STD_DEV"]
data["LB"] = data['SMA'] - 2*data['STD_DEV']

### state filter ligic
def getState(p,ub,lb):
    if p>ub:
        return 'A'
    if ub>=p and p>=lb:
        return 'B'
    if p<lb:
        return 'C'

### State Calaculation
data['state'] = data.apply(lambda row : getState(row['Close'],  row['UB'], row['LB']), axis = 1) 

### Output data has been stored in output.csv file  
data.to_csv('./output.csv')





