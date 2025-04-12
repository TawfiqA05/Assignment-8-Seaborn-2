# Assignment 8: Seaborn Data Visualization Project

## Project Overview

This project demonstrates data visualization using the Seaborn library in Python, as required for INFO-B 211 Assignment 8. It involves analyzing two datasets:

1.  **Exercise Data:** A dataset (`Exercise_Data.csv`) collected by a gym to demonstrate the effects of diet and exercise on heart rate for an elementary school.
2.  **Planets Dataset:** A built-in dataset in Seaborn containing information about planets discovered around other stars.

The project aims to create compelling data visualizations using Seaborn to answer analytical questions and provide insights from these datasets.

## Files Included

* `exercise_data_visualization.py`: Python script for visualizing the `Exercise_Data.csv` dataset.
* `planets_data_visualization.py`: Python script for visualizing the built-in `planets` dataset.
* `Exercise_Data.csv`: The dataset containing gym and school heart rate data.
* `README.md`: This file, providing an overview, instructions, and details about the project.

## Requirements

* Python 3.x
* Pandas (for data manipulation)
* Seaborn (for data visualization)
* Matplotlib (for additional plotting control)

You can install the required libraries using pip:

```bash
pip install pandas seaborn matplotlib
Exercise Data Visualizations (exercise_data_visualization.py)
This script performs the following visualizations on the Exercise_Data.csv dataset:

Heatmap of Pulse Data: A heatmap showing the correlation between pulse measurements taken at 1 minute, 15 minutes, and 30 minutes. This helps visualize how pulse rates at different times are related.
Categorical Plot of Pulse by Diet and Exercise Type: Box plots showing the distribution of pulse rates at different time points, separated by the type of diet (low fat, no fat) and the kind of exercise (rest, walking, running). This allows for comparison of pulse rates across different categories.
Conclusions for Elementary School Students:

From the charts, we can see that when students did different activities, their heart rates changed. Resting had the slowest heart rates, walking made them a little faster, and running made their hearts beat the fastest! This shows that exercise makes your heart work harder. When we looked at the students who had a low-fat diet compared to those who had no-fat in their diet, it wasn't as clear if the food they ate made a big difference in their heart rates right away. It looks like the type of activity they did had a much bigger impact on how fast their hearts were beating.

Planets Data Visualizations (planets_data_visualization.py)
This script performs the following visualizations on the built-in planets dataset:

Distribution of Planet Mass: A histogram with a Kernel Density Estimate (KDE) overlay, using a logarithmic scale for the x-axis, to show the distribution of planet masses. This helps understand the typical mass range of discovered exoplanets.
Distribution of Planet Discovery Year: A Kernel Density Estimate (KDE) plot showing the distribution of the years in which planets were discovered. This illustrates the trend of exoplanet discoveries over time.
Planet Orbital Period Over Time: A scatter plot showing the relationship between the year of discovery and the orbital period of the planets. A logarithmic scale is used for the y-axis to better visualize the spread of orbital periods.
Planet Mass vs Distance from Star: A scatter plot showing the relationship between the distance of the planets from their stars and their mass. Logarithmic scales are used for both axes to handle the wide range of values.
Orbital Period by Discovery Method: A box plot comparing the distribution of orbital periods for planets discovered using different methods. A logarithmic scale is used for the y-axis to handle the wide range of orbital periods.
Number of Planets Discovered by Method: A count plot showing the number of planets discovered using each different method. This highlights the most successful exoplanet detection techniques.
Heatmap of Numerical Features: A heatmap showing the correlation matrix of the numerical features in the planets dataset. This reveals linear relationships between different planetary properties.
Notable Insights from Planets Data:

The histogram of planet mass shows that most of the discovered planets in this dataset have relatively low masses, similar to Jupiter or smaller. However, there are also some very massive planets that have been found. The KDE plot of the discovery year clearly shows that the number of planets being discovered has increased dramatically over time, especially in recent years. This indicates that our ability to find planets around other stars is getting much better. The count plot of the discovery method is particularly interesting as it highlights that the "Transit" method has been the most successful way to find new planets so far. This method looks for dips in a star's brightness as a planet passes in front of it.

Class Design and Implementation
For this assignment, a procedural approach was used to create the visualizations. The Python scripts directly load the data and use Seaborn and Matplotlib functions to generate the required plots without defining custom classes.

Limitations
One limitation of the Exercise Data is that it includes a relatively small number of participants and only two diet types and three exercise types. A larger and more diverse dataset could provide more robust conclusions. For the Planets dataset, the findings might be biased towards planets that are easier to detect with the current methods.

Usage
Make sure you have Python and the required libraries installed.
Place the Exercise_Data.csv file in the same directory as the exercise_data_visualization.py script.
Run the Python scripts from your terminal:
Bash

python exercise_data_visualization.py
python planets_data_visualization.py
The generated plots will be displayed.
