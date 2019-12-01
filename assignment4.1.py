#!/usr/bin/env python
# coding: utf-8

# # Assignment 4
# 
# Welcome to Assignment 4. This will be the most fun. Now we will prepare data for plotting.
# 
# Just make sure you hit the play button on each cell from top to down. There are three functions you have to implement. Please also make sure than on each change on a function you hit the play button again on the corresponding cell to make it available to the rest of this notebook. Please also make sure to only implement the function bodies and DON'T add any additional code outside functions since this might confuse the autograder.
# 
# So the function below is used to make it easy for you to create a data frame from a cloudant data frame using the so called "DataSource" which is some sort of a plugin which allows ApacheSpark to use different data sources.
# 

# Sampling is one of the most important things when it comes to visualization because often the data set gets so huge that you simply
# 
# - can't copy all data to a local Spark driver (Watson Studio is using a "local" Spark driver)
# - can't throw all data at the plotting library
# 
# Please implement a function which returns a 10% sample of a given data frame:

# In[1]:


def getSample(df,spark):
    #TODO Please enter your code here, you are not required to use the template code below
    #some reference: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame
    #https://spark.apache.org/docs/latest/api/sql/
    return df.sample(False,0.1)


# Now we want to create a histogram and boxplot. Please ignore the sampling for now and return a python list containing all temperature values from the data set

# In[2]:


def getListForHistogramAndBoxPlot(df,spark):
    #TODO Please enter your code here, you are not required to use the template code below
    #some reference: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame
    #https://spark.apache.org/docs/latest/api/sql/
    return df.rdd.map(lambda row: row.temperature).filter(lambda val: val is not None).collect()


# Finally we want to create a run chart. Please return two lists (encapsulated in a python tuple object) containing temperature and timestamp (ts) ordered by timestamp. Please refer to the following link to learn more about tuples in python: https://www.tutorialspoint.com/python/python_tuples.htm

# In[11]:


#should return a tuple containing the two lists for timestamp and temperature
#please make sure you take only 10% of the data by sampling
#please also ensure that you sample in a way that the timestamp samples and temperature samples correspond (=> call sample on an object still containing both dimensions)
def getListsForRunChart(df,spark):
    #TODO Please enter your code here, you are not required to use the template code below
    #some reference: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame
    #https://spark.apache.org/docs/latest/api/sql/
    result = spark.sql("SELECT temperature, ts FROM washing WHERE temperature IS NOT NULL ORDER BY ts ASC")
    result_rdd = result.rdd.sample(False, 0.1)
    temperature_list = result_rdd.map(lambda row: row.temperature).collect()
    ts_list = result_rdd.map(lambda row: row.ts).collect()
    result_tuple = (temperature_list, ts_list)
    return tuple(result_tuple)
    


# ### PLEASE DON'T REMOVE THIS BLOCK - THE FOLLOWING CODE IS NOT GRADED
# #axx
# ### PLEASE DON'T REMOVE THIS BLOCK - THE FOLLOWING CODE IS NOT GRADED

# Now it is time to grab a PARQUET file and create a dataframe out of it. Using SparkSQL you can handle it like a database. 

# In[12]:


get_ipython().system('wget https://github.com/IBM/coursera/blob/master/coursera_ds/washing.parquet?raw=true')
get_ipython().system('mv washing.parquet?raw=true washing.parquet')


# In[13]:


df = spark.read.parquet('washing.parquet')
df.createOrReplaceTempView('washing')
df.show()


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[15]:


plt.hist(getListForHistogramAndBoxPlot(df,spark))
plt.show()


# In[16]:


plt.boxplot(getListForHistogramAndBoxPlot(df,spark))
plt.show()


# In[17]:


lists = getListsForRunChart(df,spark)


# In[18]:


plt.plot(lists[0],lists[1])
plt.xlabel("time")
plt.ylabel("temperature")
plt.show()


# Congratulations, you are done! Please download the notebook as python file, name it assignment4.1.py and submit it to the grader.

# In[ ]:





# In[ ]:





# In[ ]:




