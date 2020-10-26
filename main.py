import pandas as pd
from sqlalchemy import create_engine

con = create_engine('mysql+pymysql://root:root@localhost:3306/material')
material = pd.read_excel("material.xlsx")
material.to_sql("student",con,if_exists="replace",index=False)
df_data = pd.read_sql("select * from student",con)
print(df_data)