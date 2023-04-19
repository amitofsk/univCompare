#Summary of the program... Written by Andy Mitofsky... open license?

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#Here's the data for the figure comparing universities of different countries.
#According to https://www.worldometers.info/gdp/gdp-by-country/ the top eigth countries by gdp are
#US, China, Japan, Germany, India, UK, France, and Brazil, so I used these countries.
us_teaching=[94.8, 94.2, 90.7, 90.9, 87.6, 86.4, 92.6, 89.4, 86.5,86]
us_research=[99,96.7, 93.6, 97, 95.9, 95.8, 92.7, 87.7, 88.8,88.8]
ch_teaching=[90.1,92.5,71.8,75.3,67.3,65,58.4,29.8,43.5,42.2]
ch_research=[97.4,96.7,75.8,82.9,74.8,64.9,58.2,42.9,40.5,42.6]
jp_teaching=[88.1,77.5,26.5,28.6,30.5,28.5,27.2,24.6,30.1,25.3 ]
jp_research=[91.4,79.1,18.3,18.3,12,9.2,17,18.9,15.9,13.5]
gr_teaching=[69.8,67.3,67.2,48.5,55.2,54.4,54.6,54.2,56.8,47.8]
gr_research=[82.2,78.3,61.5,52.2,64.3,58.2,56.1,62.4,64.5,52.8]
in_teaching=[20.1,39.3,40.9,21.5,23,36,29.1,23.8,30.2,24]
in_research=[12.6,14.7,24.2,13.1,8.9,16.2,16.5,13.7,22.3,21.9]
uk_teaching=[92.3,90.9,82.8,74.5,66.9,58,59.2,54.5,43.8,43.3]
uk_research=[99.7,99.5,90.8,85.4,74.5,72.9,74.3,63.7,53.4,50.8]
country_name=['US', 'China', 'Japan', 'Germany', 'India', 'UK']

#Here's the data for the figure comparing American universities of different conferences.
ivy_teaching=[94.8,87.6,92.6,89.4,86,80.2,64.5,59.8]
ivy_research=[99,95.9,92.7,87.7,88.8,86.1,58,40.4]
bigten_teaching=[79.3,71.7,67.1,59.7,55.1,48.1,56.2,53,55.9,47.8,45.5,43.5,42.5,34]
bigten_research=[84.6,80.7,78.9,62.9,56.9,57.7,55.6,51.2,64.2,53.8,39.4,43.6,31.6,31]
acc_teaching=[78.1,60.2,58.9,46.2,48.1,48.4,51,48.6,39.3,40.2,40.9,39.4,34.9,25.2]
acc_research=[76.2,75.9,59.7,42.9,39.8,33.5,40.5,31.5,36.2,37.3,38.2,20.2,28,21.4]
pac12_teaching=[94.2,86.4,80.4,71.6,58.9,45.6,44.8,45.8,39.9,33.4]
pac12_research=[96.7,95.8,88.9,82.8,58.6,46.3,47.9,47,34.9,32.7]
bigwest_teaching=[60.2,59.7,44.6,43.5,33,39.8]
bigwest_research=[77.2,66.3,61.5,51.6,32.7,41.7]
caa_teaching=[39.9,40.8,33.8,28.8,43.7,18.5]
caa_research=[30.2,26,26.8,39,21.4,8.1]
division_name=['Ivy League', 'Big Ten', 'Big West', 'CAA', 'ACC', 'Pac-12']


def setupAxis(axisA):
    axisA.set_xlabel("Teaching Score")
    axisA.set_ylabel("Research Score")
    axisA.set_xlim(0,100)
    axisA.set_ylim(0,100)
    axisA.grid(visible=True)

#Set up the axes, title, and textbox at the bottom.
fig, (ax1, ax2)=plt.subplots(1, 2, figsize=(14,7))
setupAxis(ax1)
setupAxis(ax2)
fig.tight_layout(pad=6)
plt.suptitle("Comparing Teaching and Research Scores For Various Universities", fontsize=22)
plt.text(0.02, 0.02, "Data for 2023 from The Times Higher Education world University Rankings, \
available at https://www.kaggle.com/datasets/r1chardson/the-world-university-rankings-2011-2023", fontsize=11, transform=plt.gcf().transFigure)

#Plot the figure comparing universities of different countries.
ax1.set_title("Top Ten Universities by Countries")
ax1.scatter(us_teaching, us_research, color='blue', marker='v')
ax1.scatter(ch_teaching, ch_research, color='red', marker='p')
ax1.scatter(jp_teaching, jp_research, color='orange', marker='s')
ax1.scatter(gr_teaching, gr_research, color='green', marker='D')
ax1.scatter(in_teaching, in_research, color='grey', marker='X')
ax1.scatter(uk_teaching, uk_research, color='purple', marker='d')
ax1.legend(country_name)

#Plot the figure comparing American universities of different conferences.
ax2.set_title("American Universities by Conference")
ax2.scatter(ivy_teaching, ivy_research, color='blue', marker='s')
ax2.scatter(bigten_teaching, bigten_research, color='red', marker='D')
ax2.scatter(bigwest_teaching, bigwest_research, color='orange', marker='X')
ax2.scatter(caa_teaching, caa_research, color='green', marker='d')
ax2.scatter(acc_teaching, acc_research, color='grey', marker='v')
ax2.scatter(pac12_teaching, pac12_research, color='purple', marker='p')
ax2.legend(division_name)

#Save and show the figure.
plt.savefig("TeachingResearch.png")
plt.show()

