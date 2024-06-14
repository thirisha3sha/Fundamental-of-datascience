"""Scenario: Analyzing the performance of servers, you want to determine the 25th, 50th,
and 75th percentiles of response times to identify potential bottlenecks."""
import pandas as pd
import numpy as np
data={
    'server_id':list(range(102,115)),
    'response_time':[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    }
df=pd.DataFrame(data)
p25=np.percentile(df['response_time'],25)
p50=np.percentile(df['response_time'],50)
p75=np.percentile(df['response_time'],75)
print("25th percentile:",p25)
print("50th percentile:",p50)
print("75th percentile:",p75)
