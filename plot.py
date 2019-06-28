#!/usr/bin/env python2.7

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Read in the file
f = open("test", 'rb')

# Read data from file into an array
data = np.fromfile(f, dtype=np.int8)

# Close the file
f.close()

print(data.size)

I_data = data[0: 2046 : 2]
Q_data = data[1: 2047 : 2]

# Plot I and Q data separately

#plt.figure()
#plt.plot(I_data)
#plt.plot(Q_data)
#plt.show()

plt.figure()

data_complex = ( I_data + 1j ) * Q_data
plt.psd(data_complex, 1024, 2400000)
plt.show()




