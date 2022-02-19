import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

cpu_price_df = pd.read_csv('../datasets/crypto-gpu-data/FACT_CPU_PRICE.csv')
ie_df: DataFrame = cpu_price_df.query('RegionId == 7 and TimeId > 20160101 and ProdId == 817 and MerchantId == 36')
ie_df = ie_df.astype({'TimeId': 'string'})
ax = plt.gca()
# CPU price IE
ie_df.plot(kind='line', x='TimeId', y='Price_Original', ax=ax)
plt.show()
