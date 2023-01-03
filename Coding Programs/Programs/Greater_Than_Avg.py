# Greater than average

# importing statistics module
import statistics as st

input_list = [ [2,4,6,8,10], 4]

data=input_list[0]
check=input_list[1]

avg = sum(data)/len(data)
avg2 = st.mean(data)
if check > avg:
   print('True')
elif check < avg:
   print('False')

print(avg2)

