#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json 


# In[2]:








import sqlite3


# In[7]:


conn=sqlite3.connect('db.sqlite3')
cur=conn.cursor()


# In[9]:

filename=input("Enter file name : ")
f=open(filename)


# In[10]:


data=json.load(f)


# In[11]:


# print(data)


# In[29]:


query1='''create table if not exists student_studentdata(
    id integer not null primary key,
    name text not null,
    department text not null,
    hostel text not null,
    roll text not null unique);'''


# In[ ]:


cur.execute(query1)
conn.commit()


# In[23]:


maxq='select max(id) from student_studentdata'


# In[24]:


cur.execute(maxq)


# In[25]:


maxid=cur.fetchall()


# In[26]:


if len(maxid)!=0:
    maxid=maxid[0][0]
else:
    maxid=0


# In[27]:


print(maxid)


# In[ ]:





# In[28]:





# In[32]:


q2='insert into student_studentdata values(?,?,?,?,?)'

for a in data:
    maxid=maxid+1
    try:
        cur.execute(q2,[maxid,a['name'],a['department'],a['hostel'],a['roll']])
        conn.commit()
    except:
        croll=a['roll']
        print(f'{croll} already exists')
conn.commit()
    
cur.close()
conn.close()

# In[ ]:




