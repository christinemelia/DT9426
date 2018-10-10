#!/usr/bin/env python
# coding: utf-8

# In[6]:


#caculating the volume of a sphere with radius 20mm
import math

pi = 3.1415926535897931  # float initialising pi value as opposed to using math.pi 
print(type(pi))


r = float(input('Please Enter the Radius of a Sphere using deccimals eg, 10mm = 0.01 '))

#r = 0.02   # float
#print (type(r))

V= 4.0/3.0*pi* r**3 
print('The volume of the sphere is: ',V)












# In[9]:


#calculate the volume of a cylinder allowing user input height and radius 



Radius = float(input('Please Enter the Radius of a Cylinder using deccimals eg, 10mm = 0.01 '))
Height = float(input("\nEnter Height of Cylinder :"))
#taking input from user via type string and converting to float 


PI = 3.14
Volume = PI * Radius * Radius * Height
Surface_Area = 2 * PI * Radius * (Radius + Height)

print ("\n\nVolume of Cylinder is :" , Volume)
print ("Surface Area of Cylinder is :" , Surface_Area)


# In[11]:


#calculate the volume of a cone allowing user to input  height and radius
import math 

pi=22/7 #setting a pi value 
height = float(input('Height of cylinder: '))
radius = float(input('Radius of cylinder: '))
volume = pi * radius * radius * height

print("Volume of a cone is: ", volume)


# In[21]:


# calculate fuel effeciency on a journey getting input from user of distance travelled ammount of fuel used 

import math

# String concatenation



distance_travelled = float(input('please enter the distance you have travelled: '))

km_per_litre = float(input('How many kilometers per litre does your vehicle get? '))

fuel_price = float(input('Please enter the price of your fuel per litre:€ '))





#ammount_of_fuel_used = int(input('please enter the total litres of fuel you have used: '))





fuel_used = distance_travelled // km_per_litre

fuel_cost = fuel_price * fuel_used
     
    
total_cost = fuel_used + fuel_cost
                                 


print("Your journey cost you €" , total_cost)




# In[ ]:




