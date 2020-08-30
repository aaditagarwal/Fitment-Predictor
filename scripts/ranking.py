import pandas as pd
import numpy as np

supply = pd.read_excel('data.xlsx',header=0)

def ranking(score_df,demand):
    SL = supply.where(supply.Service_Line==demand['Service Line']).dropnna()
    SSL = SL.where(SL.Sub_Service_Line==demand['Sub Service Line']).dropna()
    SMU = SSL.where(SSL.SMU==demand['SMU']).dropna()
    SMU = score_df.loc[SMU.index.tolist(),:].sort_values(['Fitment Score'],ascending=False,ignore_index=True)
    SSL = SSL.where(SSL.SMU!=demand['SMU']).dropna()
    SSL = score_df.loc[SSL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False,ignore_index=True)
    SL = SL.where(SL.Sub_Service_Line!=demand['Sub Service Line']).dropna()
    SL = score_df.loc[SL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False,ignore_index=True)
    NSL = supply.where(supply.Service_Line!=demand['Service Line']).dropnna()
    NSL = score_df.loc[NSL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False,ignore_index=True)

    recommendation = pd.concat([SMU,SSL,SL,NSL],ignore_index=True)
    recommendation['Rank'] = list(range(1,recommendation.shape[0]))

    return recommendation