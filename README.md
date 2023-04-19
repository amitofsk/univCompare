Here's my entry for the April 2023 AngelHack Data Visualization contest.

This project is written by Andy Mitofsky. It is openly licensed under the terms of the MIT license.

Data plotted comes from the Times Higher Education World University Rankings for 2023 available at https://www.kaggle.com/datasets/r1chardson/the-world-university-rankings-2011-2023.

For this contest, I wrote code in Python and used Python's Matplotlib library. The code produces a static 2D image in .png format. This repository contains both the python code and the image file produced.

The data set is quite large. It contains information for 2011 to 2023. It contains information on 2345 universities, and it contains information on universities from hundreds of countries. I wanted to produce a static figure that summarizes this data. 

For each university, the data set contains scores for teaching, research, citations, and international outlook. It also contains rankings, student to staff ratio, and more. I decided to focus on teaching and research scores. I know some universities focus more on teaching and others focus more on research. I wanted to see if there were trends in the teaching to research emphasis.

There are two subplots in the visualization. The plot on the left looks at variations by country. I included data from the six countries with the top GDP. For each of these countries, I selected the ten highest ranked universities in the provided data set. The plot on the right looks at variation within Universities in the United States by athletic conference. I included six major athletic conferences. I included all points in the provided data set for universities in these conferences, but not all universities in the conference were included in the data set. 

 

