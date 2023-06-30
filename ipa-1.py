#!/usr/bin/env python
# coding: utf-8

# In[3]:


gross_pay = int(input("Gross pay: "))
tax_rate = float(input("Tax rate: "))
expenses = int(input("Expenses: "))

def savings(gross_pay, tax_rate, expenses):
    s = (1-tax_rate)*gross_pay - expenses
    return (s)

result = savings(gross_pay, tax_rate, expenses)
print(result)


# In[27]:


total_material = int(input("Total Material: "))
num_jobs = int(input("Number of Jobs: "))
job_consumption = int(input("Job Consumption: "))
material_units = str(input("Material Units: "))

def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste = total_material - (num_jobs*job_consumption)
    return(waste)

result = material_waste(total_material, material_units, num_jobs, job_consumption)
print(result, material_units, sep="")


# In[9]:


import math

principal = int(input("Amount invested: "))
rate = float(input("Rate per period: "))
periods = int(input("Number of Periods: "))

def interest(principal, rate, periods):
    i = (principal*rate*periods) + principal
    return(i)

result = interest(principal, rate, periods)
round_down = math.floor(result)
print(round_down)


# In[11]:


weight = float(input("Weight in pounds: "))
height = list(map(int, input("Height in inches: ").split()))

def body_mass_index(weight, height):
    weight_kg = weight*0.45
    height_inches = height[0] * 12 + height[1]
    height_m = int(height_inches) * 0.0254
    bmi = weight_kg / (height_m ** 2)
    return(bmi)

result = body_mass_index(weight, height)
print(result)

