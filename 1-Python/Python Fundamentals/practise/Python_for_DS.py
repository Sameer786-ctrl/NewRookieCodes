# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:48:20 2025

@author: sam77
"""
#######################################3
#######################################


#pandas
#create pandas dataframe using list
import pandas as pd
technologies=[ ["spark",2000,"30 days"],
              ["pandas",20000,"40 days"] ]
    
df=pd.DataFrame(technologies)
print(df)


#adding label to colums and rows
column_names=["Courses","Fees","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

###
df.dtypes

#assigning custom datatypes
types={"Courses":str,"Fee":float,"Duration":str}
df.dtypes
#still dtpes haven't changes we would learn later why

 
#####################################
#Creating dataframes from distionaries
#with dict we go columwise contrary to list where we went row wise

technologies={
    "Courses":["Spark","Pandas","Hadoop"],
    "Fee":[20000,25000,26000],
    "Duration":['30 days','45 days','35 days'],
    "Discount":[1000,2300,1500] 
    }
df=pd.DataFrame(technologies)
df

#convert and export dataframe to csv file
df.to_csv('data_file.csv')
import pandas as pd
#now convert the same csv to dataframe
df_same=pd.read_csv('data_file.csv')
df_same


#############################################3
#datadrame for basic opertaion with null/none

import pandas as pd
import numpy as np

technologies=({
     "Courses":["Spark","Pyspark","Hadoop","Python","Pandas",None,"Spark","Python"],
     "Fee":[22000,25000,23000,24000,np.nan,25000,25000,22000],
     "Duration":["50days","45days","35days","30days","25days","20days","","15days"],
     "Discount":[1000,1100,1200,1300,1400,1500,np.nan,None ]
     } )


row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_label)
print(df)

#Dataframe properties
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes

#accesing a single column
df['Fee']

#accesing  2 column
df[["Fee","Duration"]]

df2=df[6:8]
df2

df3=df[:5]
df3

#accesing specific cell
df['Duration'][3]

#modifying entire column
df["Fee"]=df["Fee"]-999
df['Fee']


#discription of data
df.describe()

#rename
df=pd.DataFrame(technologies,index=row_label)
df


#3 ways od renaming column using rename()
#same result
df.columns=['A','B','C','D']
df2=df.rename({'Fee':'c1','Courses':'c2'},axis=1)
df2
df2=df.rename({'Duration':'c3','Discount':'c4'},axis='columns')
df2
df2=df.rename(columns{['Courses':'A'],['Fee':'B']})
df2

##########################################################
##############3 to 5
import pandas as pd
import numpy as np

technologies=({
     "Courses":["Spark","Pyspark","Hadoop","Python","Pandas",None,"Spark","Python"],
     "Fee":[22000,25000,23000,24000,np.nan,25000,25000,22000],
     "Duration":["50days","45days","35days","30days","25days","20days","","15days"],
     "Discount":[1000,1100,1200,1300,1400,1500,np.nan,None ]
     } )


row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_label)
print(df)


#drop rows by labels

df1=df.drop(['r1','r2'])
df1
df=pd.DataFrame(technologies,index=row_label)
df

#delete rows by position
df1=df.drop(df.index[[1,3]])
df1

#delete rows by index range
df1=df.drop(df.index[2:])
df1

#when u have defaulr indes for rows
df=pd.DataFrame(technologies)
df1
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3])
df1=df.drop(range(0,2))
df1
 


#pandas select rows by index (position/label)
df=pd.DataFrame(technologies,index=row_label)

df2=df.iloc[2]#select row by index
df2=df.iloc[[2,3,6]]#select row by index list 
df2=df.iloc[1:5]#select rows by int index range
df2=df.iloc[:1]#select first row 
df2=df.iloc[:3]#select first 3 row 
df2=df.iloc[-1:]#select last row
df2=df.iloc[-3:]#select last 3 row 
df2=df.iloc[::2]#select alternate rows

df2



#select rows by index labels
df2=df.loc['r2']
df2=df.loc['r4']
df2=df.loc['r1':]
df2=df.loc['r1':'r7':2]




#by using df[] notation 
df2=df['Courses']
df2=df[["Courses","Fee","Duration"]]

#.loc[] used to take slices
df2=df.loc[:,["Courses","Fee","Discount"]]



########################
###################
#operation on new datset
import pandas as pd
df=pd.read_csv(r"C:/2-Python_DS/melb_data.csv")

#properties
df.shape
df.size
df.columns
df.index
df.values
df.index.values
df.dtypes

#accesing single column
df1=df["Price"]

#dropping 0th row usind direct indexing 
df1=df.drop(0)

#dropping 1 and 4th value
df1=df.drop([1,4])
df1=df.drop(range(2,6))


row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_label)

##################################################################
######################################################################
#np.nan, None and ''
import pandas as pd
import numpy as np
technologies={
    'Categories':["Spark","Pyspark","Hadoop","Python"],
    'Fee':[20000,25000,27000,22000],
    'Duration':['','40days',np.nan,None],
    'Discount':[1000,1500,1200,1700] 
    }
indexes=['r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=indexes)
print(df)
df=pd.DataFrame(technologies,index=indexes)
df2=df.dropna() ##dropping np.nan and None
print(df2)


#drop nan and None containing rows
df_clean=df.dropna(subset=['Duration'])

#removing empty strings containing rows as well
df_clean=df_clean[df_clean['Duration']!='']


#############################################
#Converting all the columns into same data type using astype

df=df.astype(str)
df.dtypes

#now converting some specific columni into integer and some to float
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

#doing the same conversionn using a list
cols=["Fee","Discount"]
df=pd.DataFrame(technologies)
df[cols]=df[cols].astype('float') #u are giving the data type with ''
df.dtypes

"""But Python (specifically, pandas) is designed to interpret that
 string as the name of a data type.
 'float' is a string → pandas internally
 looks it up in a type mapping dictionary.
It knows 'float' → maps to Python's float class (float).
So pandas reads it as: "Convert this column to type float."
"""
#by using for loop
for col in ['Fee','Discount']:
    df[col]=df[col].astype('float')
    
    
#Raising or ignoring error while conversion of column is failed
df=df.astype({"Categories":int},errors='ignore')
df.dtypes

df=df.astype({"Categories":int},errors='raise')

####################################################
#using DataFrame.to_numeric() to convert data to numeric
df["Fee"]=pd.to_numeric(df["Fee"])
df.dtypes
##
#converting multiple to numeric type using apply method
df=pd.DataFrame(technologies)
df.dtypes
 df[['Fee','Discount']]=df[['Fee','Discount']].apply(pd.to_numeric)
df.dtypes

#quic example to get number of rows in Data frame
rows_count=len(df.index)
row_count=len()

#Using DataFrame.apply to apply somwthing to column
import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])


#adding 3 into all cells using apply()
def add_3(x):
    return x+3
df2=df.apply(add_3)

#using apply() modify only single column
import pandas as pd
df=pd.DataFrame(data,columns=['A','B','C'])
def add_4(x):
    return x+4
df['B']=df['B'].apply(add_4)

#for multiple columns
#using lambda function

df["A"]=df["A"].apply(lambda x:x-2)
df

#using panads.dataframe.transform
df
def add_2(x):
    return x+2 
df=df.transform(add_2)

#using map function
df['A']=df['A'].map(lambda A:A/2)
print(df)









 