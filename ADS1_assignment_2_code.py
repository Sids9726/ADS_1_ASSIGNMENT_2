import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


countries = ["Argentina","Bangladesh","Pakistan","Indonesia","Latin America & Caribbean","Spain","Denmark"]

column_name=["Country Name","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]

# plot-1-----------------------------------------------------------
df = pd.read_csv("carbon_emission.csv",skiprows=4)
car_emission_df = df.loc[df["Country Name"].isin(countries),column_name]
#print(car_emission_df)



# plot - 2----------------------------------------------------------
df_2 = pd.read_csv("urban_population.csv",skiprows=4)
#print(df_2)
urban_population_df = df_2.loc[df_2["Country Name"].isin(countries),column_name]
#print(urban_population_df)

# plot - 3(electric power consumption)----------------------------------------------------------
df_3 = pd.read_csv("urban_population.csv",skiprows=4)
#print(df_2)
urban_population_df = df_2.loc[df_2["Country Name"].isin(countries),column_name]
#print(urban_population_df)


# transpose 
def transpose_func(ref_df):
    ref_df = pd.DataFrame.transpose(ref_df)
    header = ref_df.iloc[0].values.tolist()
    ref_df.columns = header
    ref_df = ref_df.iloc[1:]
    ref_df.index = ref_df.index.astype(int)
   #print(ref_df)
    return ref_df

# lineplot

def generate_line_plot(x,y):
    car_emission_df = x
    urban_population_df = y
    
    plt.figure(figsize=(10 , 6))
    plt.subplot(1,2,1)
    plt.plot(car_emission_df.index,car_emission_df["Argentina"],label="Argentina")
    plt.plot(car_emission_df.index,car_emission_df["Bangladesh"],label="Bangladesh")
    
    plt.plot(car_emission_df.index,car_emission_df["Indonesia"],label="Indonesia")
    plt.plot(car_emission_df.index,car_emission_df["Denmark"],label="Denmark") #iceland and greenland area
    plt.plot(car_emission_df.index,car_emission_df["Spain"],label="Spain")
    plt.legend(loc="upper right")
    
    plt.subplot(1,2,2)
    plt.plot(urban_population_df.index,urban_population_df["Argentina"],label="Argentina")
    plt.plot(urban_population_df.index,urban_population_df["Bangladesh"],label="Bangladesh")
    plt.plot(urban_population_df.index,urban_population_df["Indonesia"],label="Indonesia")
    plt.plot(urban_population_df.index,urban_population_df["Denmark"],label="Denmark") #iceland and greenland area
    plt.plot(urban_population_df.index,urban_population_df["Spain"],label="Spain")
    plt.legend(loc="upper right")
    


# bar plot-------------------------------------------------------------------------------

    """ 
        plot bar graph using bar function and give some parameters to make 
        effective look.
    """
'''
# size of figure
plt.figure(figsize=(10, 6))

# read the CSV file using pandas library
electric_power_df = pd.read_csv("electric_power_consumption.csv",
                       skiprows=4)
print(electric_power_df)

    # define total number of pillars to draw on bar graph
    number = 9
    outout = np.arange(number)
    width = 0.30

    plt.bar(outout, df_2["Clean energy"],
            width=width, color='r',
            label='Clean energy', edgecolor='black')
    plt.bar(outout + width, df_2["Fossil fuels"],
            width=width,  color='y',
            label='Fossil fuels', edgecolor='black')

    # xticks for giving the value of x axis
    labels = np.arange(2015, 2024)
    plt.xticks(outout, labels, rotation='horizontal')

    # labelling for x and y axis
    plt.xlabel("Year")
    plt.ylabel("billion USD (2022)")

    # to give title
    plt.title("Global energy investment [2015-2023]")

    # to save figure
    plt.savefig("bargraph.png")

    plt.legend()
'''
#-----------------------------------------------end-----------------------------------------------


#function define
x = transpose_func(car_emission_df) #urban_population_df
y = transpose_func(urban_population_df)
#z = transpose_func(electric_power_df)
generate_line_plot(x,y)
#print(z)

plt.show()
