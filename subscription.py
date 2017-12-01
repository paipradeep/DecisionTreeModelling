import predict as pd
my_data=[['slashdot','USA','yes',18,'None'],
['google','France','yes',23,'Premium'],
['digg','USA','yes',24,'Basic'],
['kiwitobes','France','yes',23,'Basic'],
['google','UK','no',21,'Premium'],
['(direct)','New Zealand','no',12,'None'],
['(direct)','UK','no',21,'Basic'],
['google','USA','no',24,'Premium'],
['slashdot','France','yes',19,'None'],
['digg','USA','no',18,'None'],
['google','UK','no',18,'None'],
['kiwitobes','UK','no',19,'None'],
['digg','New Zealand','yes',12,'Basic'],
['slashdot','UK','no',21,'None'],
['google','UK','yes',18,'Basic'],
['kiwitobes','France','yes',19,'Basic']]
header = ['Company','Country','FAQ','No. of Visits']
name = raw_input("Company Name:")
country = raw_input("Country :")
faq = raw_input("Visited FAQ (yes/no)")
visits = int(raw_input("No. of Visits"))
tple = [name,country,faq,visits]
pd.predictor(my_data,tple,header,"Subscription Prediction")
