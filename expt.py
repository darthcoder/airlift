import numpy as np
import matplotlib.pyplot as plt

sub1 = (13+63)/(113+23)
sub2 = (27+63)/(113+23)

# print(sub1)
# print(sub2)

first_run = np.array([295,590,917,1222,1540,1817,2125,2421,2733,3036,
                    3342,3625,3914,4210,4521])
time = np.array([20*i for i in range(1,16)])
# print(time)

second_run = np.array([412,830,1230,1650,2016,2389,2760,3120,3508,
                    3916,4300,4669,5036,5398,5781])

dig = plt.figure()
dia = dig.add_subplot(111)
dia.set_title("Experimental Flow rate with time")
dia.set_xlabel("Time Elapsed")
dia.set_ylabel("Flow in grams")

plt.plot(time,first_run,'ro',label="Submergence ratio = 0.57")
plt.plot(time, second_run,'bo',label="Submergence ratio = 0.67")

plt.legend(loc='upper left')
plt.show()
