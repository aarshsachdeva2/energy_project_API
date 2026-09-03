from sqlalchemy import text,inspect
from src.db import engine
import pandas as pd

# query_grp_tbl="""
# create table grp_tbl as
# select to_timestamp(datetime_beginning_ept,'FMMM/FMDD/YYYY HH24:MI')::date as date,sum(mw) as total_mw 
# from energy_data
# group by date
# order by date
# """
# query_feature_tbl="""
# create table feature_tbl as
# select date,
# extract(month from date):: int as month,
# extract(day from date):: int as day,
# lag(total_mw,7) over (order by date) as "t-7",
# lag(total_mw,1) over (order by date) as "t-1" from grp_tbl
# """

query="""
alter table feature_tbl add primary key(date)
"""
inspector=inspect(engine)

print(inspector.get_pk_constraint('feature_tbl'))


# with engine.begin() as connection:
# #     connection.execute(text(query_grp_tbl))
#     connection.execute(text(query))
    
    
# df=pd.read_sql("Select * from feature_tbl limit 10",engine)
# print(df)