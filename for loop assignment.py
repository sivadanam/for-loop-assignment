#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=5
for i in range(n):
    for j in range(0,i+1):
        print("ineuron",end=" ")
    print('\n')  


# In[25]:


n=3
for i in range(n):
    for j in range(i,n-1):
        print(" "*len(ineuron),end=" ")
        for j in range(i+1):
            print("ineuron",end=" ")
        
    print("\n") 
    


# In[2]:


l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':"sudh",'k2':"ineuron",'k3':"kumar",3:6,7:8},["ineuron","data science"]]


# In[3]:


#3:try to extract all the list entity
len(l)


# In[4]:


for i in l:
    if type(i)==list or type(i)==set:
        for j in i:
            if type(j)==set:
                print(j)
        print(i)


# In[5]:


#4:try to extract all the dict entities
for i in l:
    if type(i)==dict:
        print(i)


# In[6]:


for i in l:
    if type(i)==dict:
        for k,m in i.items():
            if type(k)==str or type(m)==int:
                print(k,":",m)
                


# In[7]:


#5try to extract all the tuple entities
for i in l:
    if type(i)==tuple:
        print(i)


# In[8]:


#6.try to extract all the numerical data it may be part of dict key and values
for i in l:
    if type(i)==dict :
        for j,k in i.items():
            if type(j)==int or type(k)==int:
                print(j)
                print(k)
       


# In[9]:


#6.try to extract all the numerical data it may be part of dict key and values
for i in l:
    if type(i)==dict :
        for j,k in i.items():
            if type(j)==int or type(k)==int:
                print(j,":",k)


# In[10]:


#7.try to give summation of all the numeric data
for i in l:
    if type(i)==dict or type(i)==tuple or type(i)==list or type(i)==set:
        for j in i:
            if type(j)==int:
                print(j)


# In[35]:


l1=[]
for i in l:
    if type(i)==dict or type(i)==tuple or type(i)==list or type(i)==set:
        for j in i:
            if type(j)==int:
                l1.append(j)
              


# In[36]:


l1


# In[20]:


#8.try to filter out all the odd values out all numeric data which is a part of list
for i in l:
    if type(i)==list :
        for j in range(1,i+2):
            if type(j)==int:
                    print(j)
            print(i)   
                
    


# In[ ]:





# In[14]:


#9.try to extract "ineuron" out of this data
for i in l:
    if  type(i)==tuple or type(i)==list or type(i)  :
        for j in i:
            if j=="ineuron":
                print(j)
        if type(i)==dict:
            for k in i.items():
                if k=="ineuron":
                    print(k)    


# In[23]:


#10.try to find out a number of occurances of all the data
l1
s=l1
set(s)
for i in set(s):
    print(i,":",s.count(i))


# In[ ]:





# In[24]:


#11.try to find out number of keys in dict elements
for i in l:
    if type(i)==dict:

        print(i.keys())


# In[15]:


#12.try to filter out all the string data
for i in l:
    if type(i)==tuple or type(i)==set or type(i)==list:
        for j in i:
            if type(j)==str:
                print(j)
    if type(i)==dict:
        for k,m in i.items():
            if type(k)==str or type(m)==str:
                print(k)
                print(m)
       


# In[19]:


#13.try to find out alphanum in data
x="l"
x1=x.isalnum()


# In[20]:


x1


# In[14]:


#14.try to find out multiplication of all numeric values in the individual collection inside data set
for i in l:
    if type(i)==list:
        for j in i:
            if type(j)==int:
                print(i*j)
            


# In[11]:


#15.try to unwrape all the collection inside collection and create a flat list
l1=[]
for i in l:
    if type(i)==set  or type(i)==list or type(i)==tuple or type(i)==dict:
        l1.extend(i)
                
            


# In[12]:


l1


# In[ ]:




