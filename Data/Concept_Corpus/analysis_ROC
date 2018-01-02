f=open("Data_wup.txt", 'r')
status = 1
syns = []
words = []
while True:
    data = f.readline()
    data = data.rstrip()
    if data == "END":
        break
    if data[0] == "0":
        words.append(float(data[2:]))
    else:
        if float(data[2:]) != 0.0:
            syns.append(float(data[2:]))

#full_data
minval = min(min(syns),min(words))
maxval = max(max(syns),max(words))

rangex = maxval-minval
adder = rangex/100
full_index = []

inter_index = []
for i in range(1,100):
    full_index.append(round(minval+(adder*i),2))    
tp_list = []
tn_list = []
for threshold in full_index:
    tp = round((sum(i >= threshold for i in syns))/len(syns)*100,2)
    tn = round((sum(i < threshold for i in words))/len(words)*100,2)
    tp_list.append(tp)
    tn_list.append(tn)
    
    
import numpy as np
import matplotlib.pyplot as plt
fp_list = list(map(lambda tn: 100-tn, tn_list))
fn_list = list(map(lambda tn: 100-tn, tp_list))
# Make some fake data.
a = full_index

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, tp_list, 'c', label='True Positives')
ax.plot(a, tn_list, 'c:', label='True Negatives')
ax.plot(a, fp_list, 'k', label='False Positives')
ax.plot(a, fn_list, 'k:', label='False Negatives')

legend = ax.legend(loc='lower left', shadow=True, fontsize='small')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.show()