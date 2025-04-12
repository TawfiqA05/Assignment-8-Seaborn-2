# Assignment-8-Seaborn-2
## Project Purpose
The goal of this project is to demonstrate data visualization skills using Python's Seaborn library. The project is divided into two main parts:
1. **Exercise Data Visualizations**: Using real-world data from a gym’s partnership with a local elementary school, we create:
   - A heatmap showing the average pulse by diet and type of exercise.
   - Categorical plots displaying the distribution of pulse values by diet and by exercise type.
   - A brief explanation of insights in simple language suitable for elementary school students.
2. **Planets Dataset Visualizations**: Utilizing Seaborn’s built-in planets dataset, we create two examples each of:
   - Relational plots
   - Distributional plots
   - Categorical plots
   A brief explanation is provided to identify which graphs best illustrate interesting properties of the data.

## Code Structure
- **Notebook (`Assignment8.ipynb`)**:
  - **Sections**:
    - **Data Import and Setup**: Reads the CSV and sets up the environment.
    - **Exercise Data Visualizations**: Creates the required heatmap and categorical plots.
    - **Planets Dataset Visualizations**: Produces six different graphs (2 relational, 2 distributional, and 2 categorical).
    - **Optional Class-Based Implementation**: A helper class (`DataVisualizer`) to organize the visualization functions.
  
- **Class Design (`DataVisualizer`)**:
  - **Attributes**:
    - `data`: A Pandas DataFrame holding the data.
  - **Methods**:
    - `plot_heatmap()`: Generates a heatmap from a pivot table.
    - `plot_categorical()`: Generates a categorical plot.
  - The class improves code readability and reusability.

## Usage Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/assignment8-seaborn.git
