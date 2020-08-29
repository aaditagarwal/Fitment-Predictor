import pandas as pd
import numpy as np

def ranking(data,supply,demand):
    SL = supply.where(supply.Service_Line==demand['Service Line']).dropnna()
    SSL = SL.where(SL.Sub_Service_Line==demand['Sub Service Line']).dropna()
    SMU = SSL.where(SSL.SMU==demand['SMU']).dropna()
    SMU = data.loc[SMU.index.tolist(),:].sort_values(['Score'],ascending=False)
    SSL = SSL.where(SSL.SMU!=demand['SMU']).dropna()
    SSL = data.loc[SSL.index.tolist(),:].sort_values(['Score'],ascending=False)
    SL = SL.where(SL.Sub_Service_Line!=demand['Sub Service Line']).dropna()
    SL = data.loc[SL.index.tolist(),:].sort_values(['Score'],ascending=False)
    NSL = supply.where(supply.Service_Line!=demand['Service Line']).dropnna()
    NSL = data.loc[NSL.index.tolist(),:].sort_values(['Score'],ascending=False)

    recommendation = pd.concat([SMU,SSL,SL,NSL])
    recommendation['rank'] = np.arange(1,recommendation.shape[0])

    return recommendation