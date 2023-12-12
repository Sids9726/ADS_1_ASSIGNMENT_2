import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


countries = ["Argentina","Bangladesh","Pakistan","Indonesia","Latin America & Caribbean","Spain","Denmark"]

column_name=["Country Name","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]

# plot-1 (line plot)-----------------------------------------------------------
df_1 = pd.read_csv("carbon_emission.csv",skiprows=4)
car_emission_df = df_1.loc[df_1["Country Name"].isin(countries),column_name]
#print(car_emission_df)


# plot - 2 (line plot)----------------------------------------------------------
df_2 = pd.read_csv("urban_population.csv",skiprows=4)
urban_population_df = df_2.loc[df_2["Country Name"].isin(countries),column_name]
#print(urban_population_df)

# plot - 3(bar plot)----------------------------------------------------------
#df_3 = pd.read_csv("urban_population.csv",skiprows=4)
#electric_power_df = df_3.loc[df_3["Country Name"].isin(countries),column_name]
#print(electric_power_df)


# transpose 
def transpose_func(ref_df):
    ref_df = pd.DataFrame.transpose(ref_df)
    header = ref_df.iloc[0].values.tolist()
    ref_df.columns = header
    ref_df = ref_df.iloc[1:]
    ref_df.index = ref_df.index.astype(int)
   #print(ref_df)
    return ref_df

# lineplot------------------------------------------------------------------------------

def generate_line_plot(x,y):
    car_emission_df = x
    urban_population_df = y
    
    plt.figure(figsize=(10 , 6))
    plt.plot(car_emission_df.index,car_emission_df["Argentina"],label="Argentina")
    plt.plot(car_emission_df.index,car_emission_df["Bangladesh"],label="Bangladesh")
    
    plt.plot(car_emission_df.index,car_emission_df["Indonesia"],label="Indonesia")
    plt.plot(car_emission_df.index,car_emission_df["Denmark"],label="Denmark") #iceland and greenland area
    plt.plot(car_emission_df.index,car_emission_df["Spain"],label="Spain")
    plt.legend(loc="upper right")
    
    plt.figure(figsize=(10 , 6))
    plt.plot(urban_population_df.index,urban_population_df["Argentina"],label="Argentina")
    plt.plot(urban_population_df.index,urban_population_df["Bangladesh"],label="Bangladesh")
    plt.plot(urban_population_df.index,urban_population_df["Indonesia"],label="Indonesia")
    plt.plot(urban_population_df.index,urban_population_df["Denmark"],label="Denmark") #iceland and greenland area
    plt.plot(urban_population_df.index,urban_population_df["Spain"],label="Spain")
    plt.legend(loc="upper right")
    


# bar plot-------------------------------------------------------------------------------
def generate_bar_plot():
    countries = ["Argentina","Latin America & Caribbean","Pakistan","Indonesia","Bangladesh","Spain","Denmark"]
    column_name=["Country Name","1990","1992","1994","1996","1998","2000"]
    df_3 = pd.read_csv("urban_population.csv",skiprows=4)
    electric_power_df = df_3.loc[df_3["Country Name"].isin(countries),column_name]
    electric_power_df.plot.bar(x="Country Name")
    plt.title("Country Name")
    plt.xticks(rotation=80)
    plt.xlabel("")
    plt.legend()


#function define
x = transpose_func(car_emission_df) #urban_population_df
y = transpose_func(urban_population_df)
generate_line_plot(x,y)
generate_bar_plot()
plt.show()
