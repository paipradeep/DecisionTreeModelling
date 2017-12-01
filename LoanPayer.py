import predict as pd
data = [['yes','single',125,'No'],['no','married',100,'No'],['no','single',70,'No'],
        ['yes','married',120,'No'],['no','divorced',95,'Yes'],['no','married',60,'No'],
        ['yes','divorced',220,'No'],['no','single',85,'Yes'],['no','married',75,'No'],
        ['no','single',90,'Yes']]

header = ["Home Owner","Marital Status","Annual Income"]
own = raw_input("Home Owner?(yes/no)")
mar = raw_input("Marital status(single/married/divorced)")
inc = int(raw_input("Annual Income"))
pd.predictor(data,[own,mar,inc],header,"Defaulted Borrower")
