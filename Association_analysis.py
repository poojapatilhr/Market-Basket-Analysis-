# =========================
# Association Analysis
# =========================
# Association analysis (commonly known as 'Market Basket Analysis') is used 
# to find the frequent patterns from huge amounts of data and produce 
# association rules from those frequent patterns.
# We will use the apriori algorithm to find the frequent itemsets.  From 
# each frequent itemset, we will produce the association rules using the  
# confidence and lift values.
# To understand this tutorial, you need to be familiar with the pandas 
# dataframe.
import pandas as pd
pip install apyori 
from apyori import apriori
import os; cwd = os.getcwd()
os.getcwd()


# if you have not installed 'apyori' yet, visit the following site for 
# installation: https://pypi.org/project/apyori/

# ===========================================
# Read the grocery transaction data.
# ===========================================

f = open('/Users/sujaygunjal/Desktop/Seattle University/Winter 2022/Machine Learning/Week 7/groceries.txt','r')


groceries = []

# Convert the text data to the list of lists.
for line in f:
    groceries.append(line.strip().split(","))
    
f.close()  
len(groceries)
groceries[0:10]
# Another option could be as follows:
#
# f = open('groceries.txt','r')
# groceries = []
# while True:
#     line = f.readline()
#     if  line =="":     
#         break
#     groceries.append(line.strip().split(","))
2
# arules = list(apriori(groceries))
# ====================================================
# Find frequent itemsets using the apriori algorithm.
# ====================================================
arules = list(\
    apriori(groceries, min_support=0.02, min_confidence=.1, min_lift=1))
 
# 'arules' contains a list of 'RelationRecord's.  Each 'RelationRecord'
# contains a frequent itemset and possible rules from the itemset.
# See below for an example for arules[65] at the bottom this tutorial.
# =================================
# Find the association rules.
# =================================
# Convert the lists to a dataframe 
cols_to_display = ['FreqItemSet','RelSup','LHS','RHS','Confidence','Lift']
association_rules = pd.DataFrame(columns=cols_to_display) 
# Initialize the association_rules 
for item in arules:
    r ={}
    f_itemset = item[0] # frequent itemset
    if len(f_itemset) == 1: # Do not use the rules with 1-frequent itemset.
        continue    
    for rule in item[2]:
        r['FreqItemSet'] = f_itemset
        rel_sup = item[1] # relative support
        r['RelSup'] = rel_sup
        LHS = rule[0]
        r['LHS']= LHS
        RHS = rule[1]
        r['RHS']= RHS
        Conf = rule[2]
        r['Confidence']= Conf
        Lift = rule[3]
        r['Lift'] = Lift
      
        association_rules = association_rules.append(r, ignore_index=True)
# Show some association rules
association_rules
association_rules.head()
association_rules.head()[['LHS','RHS','Confidence']]
3
print('Number of association rules: ', len(association_rules))
 # Show the top ten rules sorted by some attributes
  
# ==================
# # Queries
# ==================
# sorting_criteria = ['RelSup','Lift','Confidence']
sorted_rules = association_rules.sort_values(by=['Lift'], ascending=False)
print(sorted_rules.iloc[0:10, 1:7])
sorted_rules = association_rules.sort_values(by=['Confidence'], ascending=False)
print(sorted_rules.iloc[0:10, 1:7])
# Find the rules containing certain items from the if-part (LHS)
s = {'whole milk'}
# s = {'yogurt','whole milk'}
df = pd.DataFrame(columns=cols_to_display) 
for _, r in association_rules.iterrows():
  
    if r['LHS'].issuperset(s):
        df = df.append(r[cols_to_display], ignore_index=True)
        
ans = df.sort_values(by=['Lift'], ascending=False).iloc[0:10,1:7]
print(ans)
# Find the rules containing certain items from the then-part (RHS)
s = {'whole milk'}
# s = {'yogurt','whole milk'}
df = pd.DataFrame(columns=cols_to_display) 
for _, r in association_rules.iterrows(): 
    if r['RHS'].issuperset(s):
        df = df.append(r[cols_to_display], ignore_index=True)
df.sort_values(by=['Lift'], ascending=False).iloc[0:10,1:7]