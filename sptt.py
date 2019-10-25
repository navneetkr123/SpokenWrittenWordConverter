#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Creating dictionary of values to transform

dic = {"double a": "aa", "double b" : "bb", "double c" : "cc", "double d" : "dd", "double e" : "ee",      "double f" : "ff", "double g" : "gg", "double h" : "hh", "double i" : "ii", "double j" : "jj",      "double k" : "kk", "double l" : "ll", "double m" : "mm", "double n" : "nn", "double o" : "oo",      "double p" : "pp", "double q" : "qq", "double r" : "rr", "double s" : "ss", "double t" : "tt",       "double u" : "uu", "double v" : "vv", "double w" : "ww", "double x" : "xx", "double y" : "yy",       "tripple a": "aaa", "tripple b" : "bbb", "tripple c" : "ccc", "tripple d" : "ddd", "tripple e" : "eee",      "tripple f": "fff", "tripple g" : "ggg", "tripple h" : "hhh", "tripple i" : "iii", "tripple j" : "jjj",      "tripple k": "kkk", "tripple l" : "lll", "tripple m" : "mmm", "tripple n" : "nnn", "tripple o" : "ooo",      "tripple p": "ppp", "tripple q" : "qqq", "tripple r" : "rrr", "tripple s" : "sss", "tripple t" : "ttt",      "tripple u": "uuu", "tripple v" : "vvv", "tripple w" : "www", "tripple x" : "xxx", "tripple y" : "yyy",      "double z" : "zz", "tripple z" : "zzz",      "one dollor": "$1", "two dollor": "$2", "three dollor": "$3", "four dollor": "$4", "five dollor": "$5",      "six dollor": "$6", "seven dollor" : "$7", "eight dollor" : "$8", "nine dollor" : "$9", "dollor" : "$",      "double one" : "11", "double two" : "22", "double three" : "33", "double four" : "44", "double five" : "55",      "double six" : "66", "double seven" : "77", "double eight" : "88", "double nine" : "99", "tripple one" : "111",      "tripple two" : "222", "tripple three" : "333", "tripple four" : "444", "tripple five" : "555",      "tripple six" : "666", "tripple seven" : "777", "tripple eight" : "888", "tripple nine" : "999",      "one rupee": "₹1", "two rupee": "₹2", "three rupee": "₹3", "four rupee": "₹4", "five rupee": "₹5",      "six rupee" : "₹6", "seven rupee" : "₹7", "eight rupee" : "₹8", "nine rupee" : "₹9", "rupee" : "₹"
      }
       
       
#This function will convert spoken words to written words
# Only applicable for dataframe, list and string       
def SpokenToText(val, dic):
    if isinstance(val, list)==True:
        val = [str(i) for i in val]
        val = " ".join(val)
        for i, j in dic.items():
            val = val.replace(i, j)
        val = val.split(" ")
        return val
    elif isinstance(val, str)==True:
        for i, j in dic.items():
            val = val.replace(i, j)
        return val
    else:
        val = val.replace(to_replace = dic.keys(), value =dic.values(), regex=True) 
        return val           
    
# This function will add keys and value to dictionary    
def add(dic, key, value): 
    dic[key] = value
    return dic
        


# In[ ]:




