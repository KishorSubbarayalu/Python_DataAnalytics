#!/usr/bin/env python
# coding: utf-8

# #### Attempt to perform data analysis of Fifa 2019 players

# In[2]:


# Importing the packages

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')


# In[3]:


# Reading the data
master_data = pd.read_csv("Kaggle_Datasets/Fifa19Players.csv",index_col = 0) #Removing the defualt index


# In[4]:


pd.set_option('display.max_rows', None) # To display unlimited rows
pd.set_option('display.max_columns', None) # To display all the columns available


# In[203]:


master_data.shape


# In[6]:


fifaplayers_copy = master_data.copy() # Creating a deep copy to perform the analysis


# In[7]:


len(fifaplayers_copy.columns)


# In[8]:


fifaplayers_copy.columns


# In[9]:


fifaplayers_copy.drop(labels = ['Photo','Flag','Club Logo','Value','Wage','Body Type','Real Face','Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until',
       'Height', 'Weight','Release Clause'], axis = 1, inplace = True)


# In[10]:


len(fifaplayers_copy.columns) # Dropped non essential columns required to analyze players abolities


# In[11]:


fifaplayers_copy.head()


# In[12]:


pd.unique(fifaplayers_copy['Preferred Foot'])


# In[13]:


leftFootPlayers = fifaplayers_copy[fifaplayers_copy['Preferred Foot'] == 'Left']


# In[14]:


pd.unique(leftFootPlayers['Preferred Foot'])


# In[15]:


leftFootPlayers.head()


# In[16]:


leftFootPlayers.shape


# ### 1. Find the best left foot finisher in each club

# In[91]:


Best_finishers = leftFootPlayers[['ID','Club','Finishing','Name']]


# In[92]:


Best_finishers = Best_finishers.set_index(['ID'])


# In[708]:


Best_finishers.head()


# In[93]:


Best_finishers = Best_finishers.sort_values(by = ['Finishing','Club'] , ascending = False)


# In[41]:


#Best_finishers.Finishing.idxmax()


# In[128]:


mask = Best_finishers.groupby(['Club'], sort=False)['Finishing'].idxmax()


# In[129]:


mask = pd.DataFrame(mask)


# In[130]:


mask.rename(columns = {'Finishing':'ID'}, inplace = True)


# In[604]:


#mask = mask.reset_index()
mask.drop(labels = ['level_0','index'],axis = 1, inplace = True)


# In[605]:


mask


# In[116]:


Best_finishers


# In[133]:


Best_finishers = pd.merge(Best_finishers, mask, on = 'ID')


# In[135]:


Best_finishers.drop(labels = ['Club_y'], axis = 1, inplace = True)


# In[136]:


Best_finishers.rename(columns = {'Club_x':'Club'}, inplace = True)


# In[709]:


Best_finishers.head() # Best Finishers of left foot players in 2019


# ### 2. Categorize the players based on their finishing and show the count for each category using seaborn

# In[167]:


Best_finishers_copy = Best_finishers.copy()


# In[161]:


Best_finishers_copy


# In[196]:


for row_index,row in Best_finishers_copy.iterrows():
    if row.Finishing >= 85.0:
        Best_finishers_copy.loc[row_index,'SkillLevel'] = 'Professional'
    elif (row.Finishing >= 70.0) & (row.Finishing < 85.0) :
        Best_finishers_copy.loc[row_index,'SkillLevel'] = 'Advanced'
    elif (row.Finishing >= 50.0) & (row.Finishing < 70.0) :
        Best_finishers_copy.loc[row_index,'SkillLevel'] = 'Average'
    else:
        Best_finishers_copy.loc[row_index,'SkillLevel'] = 'Below Average'


# In[197]:


Best_finishers_copy


# In[201]:


sb.countplot("SkillLevel",
              data = Best_finishers_copy,
              palette = "Accent")

plt.show()


# ### 3. Top 7 Economical Club, Richest Club, Clubs paying the high wages to their players

# In[516]:


# Creating a copy of master data
fifaplayers_copy1 = master_data.copy()
fifaplayers_copy1.head()


# In[517]:


# Removing the non-essential rows for the analysis
fifaplayers_copy1 = fifaplayers_copy1[['ID','Name','Club','Value','Wage','Potential']]


# In[491]:


# Couting the null records
fifaplayers_copy1.isnull().sum()


# In[492]:


fifaplayers_copy1.shape


# In[518]:


# Dropping the players having no club details
fifaplayers_copy1.dropna(subset=['Club'], inplace = True)


# In[519]:


fifaplayers_copy1.shape # Removed the players with no club details (18207 - 17966 = 241)


# In[494]:


fifaplayers_copy1.head()


# In[226]:


# The Data type of Value and Wage are object, numerical operations could not be performed in this data type
# Data Cleaning must be done
fifaplayers_copy1.info()


# In[520]:


# As the Value and Wage has currency symbol in the value, running a loop to remove it
# Using for loop is one method, another method is using slicing operation
for row in fifaplayers_copy1.itertuples():
    fifaplayers_copy1.loc[row.Index,'Value'] = row.Value.lstrip('€')
    fifaplayers_copy1.loc[row.Index,'Wage'] = row.Wage.lstrip('€')


# In[496]:


fifaplayers_copy1.head() # Removed the currency symbol


# In[ ]:


# Lets try to create a function to covert K thousands to M millions for Value and Wage columns
# This is required to convert the data type of these attributes in order to derive the economical club


# In[521]:


def Conver_KtoM():
    for row in fifaplayers_copy1.itertuples():
        if (fifaplayers_copy1.loc[row.Index,'Value'][-1]) == 'M':
            fifaplayers_copy1.loc[row.Index,'Value'] = fifaplayers_copy1.loc[row.Index,'Value'].rstrip('M')
            fifaplayers_copy1.loc[row.Index,'Value'] = float(fifaplayers_copy1.loc[row.Index,'Value'])
        elif (fifaplayers_copy1.loc[row.Index,'Value'][-1]) == 'K':
            fifaplayers_copy1.loc[row.Index,'Value'] = fifaplayers_copy1.loc[row.Index,'Value'].rstrip('K')
            fifaplayers_copy1.loc[row.Index,'Value'] = float(fifaplayers_copy1.loc[row.Index,'Value'])
            fifaplayers_copy1.loc[row.Index,'Value'] /= 100
        else:
            fifaplayers_copy1.loc[row.Index,'Value'] = float(fifaplayers_copy1.loc[row.Index,'Value'])
        if (fifaplayers_copy1.loc[row.Index,'Wage'][-1]) == 'M':
            fifaplayers_copy1.loc[row.Index,'Wage'] = fifaplayers_copy1.loc[row.Index,'Wage'].rstrip('M')
            fifaplayers_copy1.loc[row.Index,'Wage'] = float(fifaplayers_copy1.loc[row.Index,'Wage'])
        elif (fifaplayers_copy1.loc[row.Index,'Wage'][-1]) == 'K':
            fifaplayers_copy1.loc[row.Index,'Wage'] = fifaplayers_copy1.loc[row.Index,'Wage'].rstrip('K')
            fifaplayers_copy1.loc[row.Index,'Wage'] = float(fifaplayers_copy1.loc[row.Index,'Wage'])
            fifaplayers_copy1.loc[row.Index,'Wage'] /= 100
        else:
            fifaplayers_copy1.loc[row.Index,'Wage'] = float(fifaplayers_copy1.loc[row.Index,'Wage'])
    


# In[475]:


fifaplayers_copy1.head()


# In[522]:


Conver_KtoM()


# In[523]:


fifaplayers_copy1.head()


# In[524]:


#Covert the datatype of Value and Wage column from object to numeric
fifaplayers_copy1[["Value", "Wage"]] = fifaplayers_copy1[["Value", "Wage"]].apply(pd.to_numeric) 


# In[525]:


#The data type of the Value and Wage are changed to float64
fifaplayers_copy1.info()


# In[526]:


fifaplayers_copy1.head()


# In[527]:


fifaplayers_copy1.rename(columns = {'Value':'€Value(M)','Wage':'€Wage(M)'}, inplace = True)


# In[657]:


Best_economical_club = fifaplayers_copy1.copy() #Creating a copy


# In[628]:


Best_economical_club.head()


# In[658]:


# Calculationg wages for each players per year
Best_economical_club['WagePerYear'] = Best_economical_club['€Wage(M)']*12 


# In[630]:


Best_economical_club.head()


# In[695]:


#Finding the sum for each attributes group by the club
Best_economical_club_fifa19 = Best_economical_club.groupby(['Club'], as_index=False, sort=False)[['€Value(M)','€Wage(M)','Potential','WagePerYear']].sum()


# In[696]:


Best_economical_club_fifa19 = pd.DataFrame(Best_economical_club_fifa19)


# In[663]:


Best_economical_club_fifa19


# In[659]:


#Best_economical_club_fifa19['NumberOfPlayers'] = Best_economical_club.groupby(['Club'], sort=False)[['ID']].count()


# In[697]:


Best_economical_club_fifa19.columns


# In[699]:


Best_economical_club_fifa19.head()


# In[700]:


#The club is said to be economical if the difference between its value and wage is high
Best_economical_club_fifa19['Economy'] = Best_economical_club_fifa19['€Value(M)'] - Best_economical_club_fifa19['WagePerYear']


# In[701]:


# The top 7 economical clubs
Best_economical_club_fifa19_Economy = Best_economical_club_fifa19.sort_values(by = 'Economy', ascending = False).head(7)


# In[702]:


Best_economical_club_fifa19_Economy.reset_index(drop = True)


# In[703]:


# Plotting the top 7 economical clubs
plt.subplots(figsize = (15,6))

sb.barplot(x = "Club",
            y = "Economy",
            data = Best_economical_club_fifa19_Economy,
            palette = 'Accent')

plt.show()


# In[704]:


# The top 7 high paying clubs in millions to their players
Best_economical_club_fifa19_Wage = Best_economical_club_fifa19.sort_values(by = 'WagePerYear', ascending = False).head(7)
Best_economical_club_fifa19_Wage.reset_index(drop = True)


# In[705]:


# Plotting the top 7 high paying clubs in millions to their players
plt.subplots(figsize = (15,6))

sb.barplot(x = "Club",
            y = 'WagePerYear',
            data = Best_economical_club_fifa19_Wage)

plt.show()


# In[706]:


# The top 7 richest clubs
Best_economical_club_fifa19_value = Best_economical_club_fifa19.sort_values(by = '€Value(M)', ascending = False).head(7)
Best_economical_club_fifa19_value.reset_index(drop = True)


# In[707]:


# Plotting the top 7 richest clubs
plt.subplots(figsize = (15,6))

sb.barplot(x = "Club",
            y = '€Value(M)',
            data = Best_economical_club_fifa19_value,
            palette = 'deep')

plt.show()


# ### 4. Find the strength of association between players age and overall performance and use scatter plot to display them

# In[710]:


fifaplayers_copy2 = master_data.copy()
fifaplayers_copy2.head()


# In[711]:


# Creating a dataframe with age and performance columns
age_performance = fifaplayers_copy2[['Age','Overall','Potential']]


# In[717]:


age_performance.head()


# In[715]:


#Check for null values
age_performance.isnull().sum()


# In[714]:


#Plotting the age distribution among players
plt.subplots(figsize=(12,6))

sb.distplot(age_performance["Age"],
             bins = 29,
             kde = False)

plt.show()


# In[718]:


# Creating age slabs
for row_index,row in age_performance.iterrows():
    if row.Age >= 35:
        age_performance.loc[row_index,'AgeGroup'] = 'Seniors'
    elif (row.Age >= 25) & (row.Age < 35) :
        age_performance.loc[row_index,'AgeGroup'] = 'Adults'
    elif (row.Age >= 20) & (row.Age < 25) :
        age_performance.loc[row_index,'AgeGroup'] = 'Youth'
    else:
        age_performance.loc[row_index,'AgeGroup'] = 'YoungLads'


# In[721]:


age_performance.AgeGroup.unique()


# In[731]:


with sb.axes_style("darkgrid"): #The darker hexagon represents the high density
    
    sb.jointplot('Age',
                  'Overall',
                   data = age_performance,
                   kind = 'hex',
                   color = 'r')
    
plt.show()


# In[726]:


sb.jointplot('Age',
                  'Overall',
                   data = age_performance,
                   color = 'g')
plt.show()


# In[728]:


sb.pairplot(age_performance,
             height = 4,
             vars = ["Age",
                     "Overall",
                     "Potential"],
             diag_kind = "kde")

plt.show()


# In[741]:


#Plotting the box plot based on age groups
plt.subplots(figsize = (15,8))

sb.boxplot(x = "AgeGroup",
            y = "Overall",
            data = age_performance)

plt.show()


# In[749]:


age_performance.describe()


# In[767]:


stat = ['count','mean','std','min','25%','50%','75%','max']


# In[768]:


age_performance_stat = pd.DataFrame(age_performance.describe())


# In[769]:


age_performance_stat.reset_index(drop = True)


# In[770]:


age_performance_stat['StatisticalParameters'] = stat


# In[771]:


age_performance_stat.shape


# In[777]:


age_performance_stat = age_performance_stat.reset_index(drop = True)


# In[783]:


age_performance_stat = age_performance_stat.loc[1:,:]


# In[784]:


age_performance_stat


# In[785]:


age_performance_stat.plot(x='StatisticalParameters',y=['Age','Overall','Potential'], kind = 'bar')


# In[ ]:




