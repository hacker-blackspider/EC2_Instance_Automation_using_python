#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3


# In[ ]:





# In[2]:


myec2 = boto3.resource(
            service_name="ec2", 
            region_name="ap-south-1" , 
            aws_access_key_id="", 
            aws_secret_access_key=""
) 


# In[3]:


myec1 = boto3.client("ec2",region_name="ap-south-1" , 
            aws_access_key_id="", 
            aws_secret_access_key="")


# In[4]:


def lwosterminate(n):
    myec1.terminate_instances(InstanceIds=[n])


# In[5]:


def lwoslaunch():
    myid = myec2.create_instances( 
                InstanceType="t2.micro", 
                ImageId="ami-0fd05997b4dff7aac",
                MinCount=1,
                MaxCount=1
    )

    return myid


# In[6]:


myos = lwoslaunch()


# In[7]:


myos[0].id


# In[8]:


myos[0].id


# In[9]:


myoslist.append( myos[0].id )


# In[10]:


myoslist


# In[11]:


myos = lwoslaunch()


# In[12]:


myoslist.append( myos[0].id )


# In[13]:


los = myoslist.pop()


# In[14]:


los


# In[15]:


lwosterminate(los)


# In[16]:


myoslist


# In[17]:


len(myoslist)


# In[18]:


myec2.


# In[ ]:




