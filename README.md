
# Sugarcane Production Analysis

A Streamlit web application that provides comprehensive analysis of sugarcane production across various countries. The app includes univariate, bivariate, and continent-based analyses using data visualization tools such as Seaborn and Matplotlib.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SujalBochkar/sugarcane-production.git
   cd sugarcane-production
   ```

2. **Install the required dependencies**:
   You can install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```
   Make sure the `requirements.txt` file includes the following packages:
   ```
   streamlit
   pandas
   seaborn
   matplotlib
   ```

3. **Add your dataset**:
   Place the `List of Countries by Sugarcane Production.csv` file in the root directory.

4. **Run the application**:
   To run the Streamlit app, use the command:
   ```bash
   streamlit run app.py
   ```

5. **Access the app**:
   After running the command, open your browser and navigate to `http://localhost:8501` to view the application.

## Usage

- **Sidebar Options**: 
  The app allows users to select different analysis types through the sidebar:
  - **Univariate Analysis**: View country and continent data, top producers, and feature distributions.
  - **Bivariate Analysis**: Visualize relationships between variables such as land area and production.
  - **Continent Analysis**: Explore production and its distribution across continents.

## Features

- **Univariate Analysis**: 
  - View sugarcane production data across countries.
  - See the number of countries producing sugarcane by continent.
  - Explore the top 10 countries by production and the distribution of production features.
  
- **Bivariate Analysis**: 
  - Visualize the relationship between land area and production.
  - Visualize the relationship between yield per hectare and production.

- **Continent Analysis**: 
  - Explore sugarcane production summarized by continent.
  - Analyze the effect of the number of producing countries on overall production.
  - View continent-wise production distribution with visualizations.
  
![image](https://github.com/user-attachments/assets/460f3a63-62c7-4d41-8e34-425caa702214)
<!--![image](https://github.com/user-attachments/assets/754e839d-d7cb-48c4-8704-f34fc8536184)-->
<!--[//]: # (![image](https://github.com/user-attachments/assets/add44b7d-9d9b-47f1-9b20-dc1523ce18b7))-->
<!--(Hello)-->
## Data Cleaning

The dataset undergoes cleaning and transformation, including:
- Removing periods in numerical columns and converting them to proper numeric types.
- Replacing commas in numeric columns and converting them for analysis.
- Renaming columns for consistency and readability.
- Dropping null values and resetting the index for a clean data frame.

## Contribution

Feel free to submit pull requests for any improvements or new features.
