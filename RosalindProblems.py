#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Rosalind Python
# Angela M.


# In[ ]:


# Problem 


# In[ ]:


import this


# In[ ]:





# In[ ]:


# Problem 2


# In[ ]:


import math


# In[ ]:


x = math.hypot(902, 922)


# In[ ]:


int(x)


# In[ ]:


x*x


# In[ ]:





# In[ ]:


# Program 3


# In[ ]:


sentence = "hMJ9ievdMDogVCWOJJJRBradypodioncUfLKRyBKM0VIEdNZi9PNIzHpzzGtPPIsTqg8TMhwab4enAQ5pmAPqpo0xPMI9YDTDlmaEkfI8W7ptl3M7EsB0IuJM7qEyrVF1z5SRtpcUaLda45F9WcWrOf80MXBCiKlI7mRarenarius7vM3JbwX."


# In[ ]:


print(sentence[20:31], sentence[164:173])


# In[ ]:





# In[ ]:


# Program 4


# In[4]:


z = 0
numbers = range(4000, 8486)


# In[5]:


for num in numbers:
    if num % 2 == 1:
        z += num


# In[6]:


print(z)


# In[ ]:





# In[ ]:


# Program 5


# In[9]:


i = 1
inFile = open('rosalind_ini5.txt')
for line in inFile.readlines():
    if i % 2 == 0 :
        print(line)
    i += 1


# In[ ]:





# In[ ]:


# Program 6


# In[20]:


sentence = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'.split()
from collections import Counter
for key,value in Counter(sentence).items():
    print (key,value)


# In[ ]:





# In[ ]:




