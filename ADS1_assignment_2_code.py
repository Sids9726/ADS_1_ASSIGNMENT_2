import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def read_data_all(filename):
     
    df = pd.read_csv(filename,skiprows=4)
    
    # set index
    df.index=df.iloc[:,0]
    df=df.iloc[:,1:]
    #countries = ["Argentina","Bangladesh","Pakistan","Indonesia","Latin America & Caribbean","Spain","Denmark"]
    countries = ["Argentina","Bangladesh","Indonesia","Spain","Denmark"]
    column_name=["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]
    df=df.loc[countries,column_name]
    
    # transpose the data
    df_t = df.T
    df_t.index = df_t.index.astype(int)
    return df,df_t

#def read_data_bars

 

def bar_inner_func(filename):
    
    
    df = pd.read_csv(filename,skiprows=4)
    
    # set index
    df.index=df.iloc[:,0]
    df=df.iloc[:,1:]
    #countries = ["Argentina","Latin America & Caribbean","Pakistan","Indonesia","Bangladesh","Spain","Denmark"]
    countries = ["Argentina","Bangladesh","Indonesia","Spain","Denmark"]
    column_name=["1990","1995","2000","2005","2010","2015"]
    #column_name=["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]
    df=df.loc[countries,column_name]
    
    return df
    

# lineplot------------------------------------------------------------------------------

def generate_line_plot(x,y):
    carbon_emission_df = x
    urban_population_df = y
    
    plt.figure(figsize=(10 , 6))
    plt.plot(carbon_emission_df.index,carbon_emission_df["Argentina"],label="Argentina")
    plt.plot(carbon_emission_df.index,carbon_emission_df["Bangladesh"],label="Bangladesh")
    plt.plot(carbon_emission_df.index,carbon_emission_df["Indonesia"],label="Indonesia")
    plt.plot(carbon_emission_df.index,carbon_emission_df["Denmark"],label="Denmark") #iceland and greenland area
    plt.plot(carbon_emission_df.index,carbon_emission_df["Spain"],label="Spain")
    plt.legend(loc="upper right")
    plt.xlabel("year")
    plt.ylabel("carbon emission rate")
    plt.title("co2 emission")
    plt.savefig("carbon_emission_linechart.png",dpi=200,va="center")
    
    plt.figure(figsize=(10 , 6))
    plt.plot(urban_population_df.index,urban_population_df["Argentina"],label="Argentina")
    plt.plot(urban_population_df.index,urban_population_df["Bangladesh"],label="Bangladesh")
    plt.plot(urban_population_df.index,urban_population_df["Indonesia"],label="Indonesia")
    plt.plot(urban_population_df.index,urban_population_df["Denmark"],label="Denmark") #iceland and greenland area
    plt.plot(urban_population_df.index,urban_population_df["Spain"],label="Spain")
    plt.legend(loc="upper right")
    plt.xlabel("year")
    plt.ylabel("urban population ratio")
    plt.title("urban population")
    plt.savefig("urban_population_linechart.png",dpi=200,va="center")
    


# bar plot-------------------------------------------------------------------------------
def generate_bar_plot():
    
    
    x="electric_power_consumption.csv"
    electric_power_df=bar_inner_func(x) 
    electric_power_df.plot.bar()
    plt.xticks(rotation=0)
    plt.legend()
    plt.xlabel("country")
    plt.ylabel("power consumption rate")
    plt.title("electric power consumption")
    plt.savefig("electric_power_consumption_bar.png",dpi=200,va="center")
    
    y="forest_area.csv"
    forest_area_df=bar_inner_func(y)
    forest_area_df.plot.bar()
    plt.xticks(rotation=0)
    plt.legend()
    plt.xlabel("country")
    plt.ylabel("forest area")
    plt.title("forest area")
    plt.savefig("forest_area_bar.png",dpi=200,va="center")
    
    return electric_power_df,forest_area_df

#hit map--------------------------------------------------
def generate_heatmap(country,carbon_emission_df,urban_population_df,electric_power_df,forest_area_df,poverty_count_df,agricultural_land_df,renewable_energy_df):
    
    
    df_corr = pd.DataFrame()
    
    df_corr["Co2 emission"]=carbon_emission_df[country].values
    df_corr["urban_population"]=urban_population_df[country].values
    df_corr["power_consume"]=electric_power_df[country].values
    df_corr["forest_area"]=forest_area_df[country].values
    df_corr["poverty_rate"]=poverty_count_df[country].values
    df_corr["agricultural_land"]=agricultural_land_df[country].values
    df_corr["renewable_energy"]=renewable_energy_df[country].values
    agricultural_land_df
    
    corr_mat = df_corr.corr().round(2)
    plt.figure()
    plt.imshow(corr_mat,cmap="Accent_r")
    plt.colorbar()
    
    plt.xticks(np.arange(len(corr_mat.columns)),labels=corr_mat.columns,rotation=90)
    plt.yticks(np.arange(len(corr_mat.columns)),labels=corr_mat.columns)
    
    plt.title(country)
    
    #looping
    for(i,j), corr_xy in np.ndenumerate(corr_mat):
        plt.text(i,j,corr_xy,ha="center",va="center")
        
    plt.savefig(country+".png",dpi =200) #,va="center"


#function calling------------------------------------------------

# generate line chart
var_x = "carbon_emission.csv"
carbon_emission_df,carbon_emission_df_t=read_data_all(var_x)

var_x = "urban_population.csv"
urban_population_df,urban_population_df_t=read_data_all(var_x)

var_x = "electric_power_consumption.csv"
electric_power_df,electric_power_df_t=read_data_all(var_x)

var_x = "forest_area.csv"
forest_area_df,forest_area_df_t=read_data_all(var_x)

var_x = "poverty_count.csv"
poverty_count_df,poverty_count_df_t=read_data_all(var_x)

var_x = "agricultural_land.csv"
agricultural_land_df,agricultural_land_df_t=read_data_all(var_x)

var_x = "renewable_energy.csv"
renewable_energy_df,renewable_energy_df_t=read_data_all(var_x)


generate_line_plot(carbon_emission_df_t,urban_population_df_t)

#generate bar plot and accessing dataframe
electric_power_df,forest_area_df = generate_bar_plot()


#heatmap
all_country=["Denmark","Indonesia","Spain"]
for country in all_country:    
    generate_heatmap(country,carbon_emission_df_t,urban_population_df_t,electric_power_df_t,forest_area_df_t,poverty_count_df_t,agricultural_land_df_t,renewable_energy_df_t)

plt.show()
