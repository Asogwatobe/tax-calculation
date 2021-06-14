#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#read in data
df = pd.read_excel(r"C:\Users\user\Downloads\stats.xlsx") #change this to your location of the excel file you downloaded

df

#replace spaces in column names with under score
names = []

for i in df.columns:
    a= i.replace(" ", "_")
    names.append(a)
    
#change column names
df.columns = names

#call the data
df


# In[2]:


def slip(df): #takes in a dataframe
    
    for row in df.itertuples():
        Name = row.Employee_Name
        Weekend = row.WEEK_ENDING
        Number = row.Employee_Number
        normalhrs = 39
        normalrate = row.HOURLY_RATE
        normalratetotal = normalhrs * normalrate
        overtime =  row.HOURS_WORKED - 39
        overtimerate = 22.50
        overtimetotal = overtime * overtimerate
        grosspay = normalratetotal + overtimetotal
        standard = 700
        Rate = 0.2
        Standardtotal = standard * Rate
        higherrate = 0.4
        higherrateTax = 42.5 * 0.4
        totaltax = Standardtotal + higherrateTax
        Taxcredit = 70
        Totaldeductions = totaltax - 70
        netpay = grosspay - Totaldeductions
        f = open(Name + ".txt", "w")
        print("\nPAYSLIP \nWeek Ending: {},              \nEmployeeName: {}\nEmployeeNumber: {} \n               {:<10} {:<10} {:<10}              \n{:<10}     {:<10} {:<10} {:<10}               \n{:<10}     {:<10} {:<10} {:<10}               \n \n{} {:<20}                \n{:<13} {:<10} {:<10}                \n{:<13} {:<10} {:<10}                \n{:<13} {:<10} {:<10}                \n{} \t \t {}                \n{} \t \t {}                \n{} \t {}                \n{} \t \t {}".format(Weekend,
                                                    Name, 
                                                    Number, "Hour", "Rate", "Total",
                                                    "normal", normalhrs, normalrate, normalratetotal,
                                                    "Overtime", overtime, overtimerate, overtimetotal,
                                                    "Grosspay", grosspay,
                                                    " ", "TaxAmt", "Total",
                                                    "Standard(700)", Rate, Standardtotal,
                                                    "Higher (42.5)", higherrate, higherrateTax,
                                                   "Total Tax", totaltax,
                                                    "Total Credit", Taxcredit,
                                                    "Total Deductions", Totaldeductions,
                                                    "Net Pay", netpay), file = f, end = "")


# In[3]:


#call the function to print out the pay slip
slip(df)

#The pay slip is printed out in the current working directory


# In[ ]:


#To check the current working directory
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

