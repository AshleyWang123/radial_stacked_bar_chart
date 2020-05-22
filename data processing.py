import pandas as pd

#separate xls to three CSVs
xls=pd.ExcelFile("dataset_original.xls")
df1 = xls.parse(sheetname="People", index_col=None, na_values=['NA'])
df2 = xls.parse(sheetname="Men", index_col=None, na_values=['NA'])
df3 = xls.parse(sheetname="Women", index_col=None, na_values=['NA'])
df1.drop([0,1,2,3,4,5,6,7],inplace=True)
df2.drop([0,1,2,3,4,5,6,7],inplace=True)
df3.drop([0,1,2,3,4,5,6,7],inplace=True)
df1.to_csv('Employment.csv',index=False)
df2.to_csv('Men.csv',index=False)
df3.to_csv('Women.csv',index=False)

#convert DATE form: Mar-May 1992 to 1992 Mar-May
def covert(csv):
    df=pd.DataFrame(pd.read_csv(csv))
    date=df["DATE"].str.split(" ",expand=True)
    df["MONTH"]=date[0]
    df["DATE"]=date[1]
    df["DATE"]=df["DATE"].str.cat(df["MONTH"],sep="-")
    df=df.drop(df.columns[7],axis=1)
    df.to_csv("Men.csv",index=False)
