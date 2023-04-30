import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import os
db_connect=os.environ['bb_connect_string']
engine = create_engine(db_connect,
                          connect_args={
        "ssl": {"ssl_ca": "/etc/ssl/cert.pem"

        }
    })






with engine.connect() as conn:
  result = conn.execute(text("select * from jobs_table"))
  column_names = result.keys()
    
  result_dicts = []
    
  for row in result.all():
    result_dicts.append(dict(zip(column_names, row)))
  print(result_dicts)
   