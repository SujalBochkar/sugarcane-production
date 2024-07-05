import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the data
def load_data():
    df = pd.read_csv("List of Countries by Sugarcane Production.csv")
    return df


df = load_data()

# Data Cleaning
df["Production (Tons)"] = df["Production (Tons)"].str.replace(".", "").astype(float)
df["Production per Person (Kg)"] = (
    df["Production per Person (Kg)"]
    .str.replace(".", "")
    .str.replace(",", ".")
    .astype(float)
)
df["Acreage (Hectare)"] = df["Acreage (Hectare)"].str.replace(".", "").astype(float)
df["Yield (Kg / Hectare)"] = (
    df["Yield (Kg / Hectare)"].str.replace(".", "").str.replace(",", ".").astype(float)
)

# Renaming columns
df.rename(
    columns={
        "Production (Tons)": "Production(Tons)",
        "Production per Person (Kg)": "Production_per_person(Kg)",
        "Acreage (Hectare)": "Acreage(Hectare)",
        "Yield (Kg / Hectare)": "Yield(Kg/Hectare)",
    },
    inplace=True,
)

# Dropping null values
df = df.dropna().reset_index(drop=True)

# Sidebar to select analysis
st.sidebar.title("Choose Analysis")
analysis_choice = st.sidebar.radio(
    "Analysis", ("Univariate Analysis", "Bivariate Analysis", "Continent Analysis")
)

# Main content based on analysis choice
st.title("Sugarcane Production Analysis")

if analysis_choice == "Univariate Analysis":
    st.header("Univariate Analysis")

    st.subheader("Countries by Sugarcane Production")
    st.write(df.head())

    st.subheader("Number of Countries Producing Sugarcane from Each Continent")
    continent_counts = df["Continent"].value_counts().sort_index()
    st.write(continent_counts)

    st.bar_chart(continent_counts.sort_values(ascending=True))

    st.subheader("Top 10 Countries by Production (Tons)")
    st.write(df.nlargest(10, "Production(Tons)"))

    st.subheader("Distribution of Production Features")
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    sns.histplot(df["Production(Tons)"], ax=axes[0, 0], kde=True)
    axes[0, 0].set_title("Production(Tons)")
    sns.histplot(df["Production_per_person(Kg)"], ax=axes[0, 1], kde=True)
    axes[0, 1].set_title("Production_per_person(Kg)")
    sns.histplot(df["Acreage(Hectare)"], ax=axes[1, 0], kde=True)
    axes[1, 0].set_title("Acreage(Hectare)")
    sns.histplot(df["Yield(Kg/Hectare)"], ax=axes[1, 1], kde=True)
    axes[1, 1].set_title("Yield(Kg/Hectare)")
    st.pyplot(fig)

elif analysis_choice == "Bivariate Analysis":
    st.header("Bivariate Analysis")

    st.subheader("Scatter Plot: Land vs Production")
    fig_land, ax_land = plt.subplots()
    sns.scatterplot(
        data=df, x="Acreage(Hectare)", y="Production(Tons)", hue="Continent", ax=ax_land
    )
    st.pyplot(fig_land)

    st.subheader("Scatter Plot: Yield vs Production")
    fig_yield, ax_yield = plt.subplots()
    sns.scatterplot(
        data=df,
        x="Yield(Kg/Hectare)",
        y="Production(Tons)",
        hue="Continent",
        ax=ax_yield,
    )
    st.pyplot(fig_yield)

elif analysis_choice == "Continent Analysis":
    st.header("Continent Analysis")

    df_continent = df.groupby("Continent").sum()
    df_continent["number_of_countries"] = df.groupby("Continent").count()["Country"]

    st.subheader("Production of Sugarcane by Continent")
    st.write(df_continent["Production(Tons)"].sort_values(ascending=False))
    st.bar_chart(df_continent["Production(Tons)"].sort_values(ascending=False))

    st.subheader("Effect of Number of Countries on Production")
    st.line_chart(df_continent[["number_of_countries", "Production(Tons)"]])

    st.subheader("Production Distribution by Continent")
    fig, ax = plt.subplots()
    df_continent["Production(Tons)"].plot(kind="pie", autopct="%.2f%%", ax=ax)
    ax.set_ylabel("")  # Remove the ylabel to improve visualization
    st.pyplot(fig)

# Displaying footer or any additional information
st.sidebar.markdown("---")
st.sidebar.title("Developed by Sujal")
