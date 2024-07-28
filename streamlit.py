import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time


st.title('Fun Streamlit Plotting App')

st.write('Animating random data points')
fig, ax = plt.subplots()
max_x = 5
max_rand = 10

x = np.arange(0, max_x)
ax.set_ylim(0, max_rand)
line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
my_plot = st.pyplot(plt)

def init():  # create an empty plot
    line.set_ydata([np.nan] * len(x))

def animate(i):  # calculate and update values on the y axis
    line.set_ydata(np.random.randint(0, max_rand, max_x))
    my_plot.pyplot(plt)


init()
for i in range(50):
    animate(i)
    time.sleep(0.1)