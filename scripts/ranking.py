import pandas as pd
import numpy as np

supply = pd.read_excel('data.xlsx', header=0, sheet_name=1, index_col=0)

def ranking(score_df,demand):
    score_df.set_index("Employee_ID", inplace=True)
    SL = supply.where(supply.Service_Line==demand['Service Line']).dropna()
    SSL = SL.where(SL.Sub_Service_Line==demand['Sub-Service Line']).dropna()
    SMU = SSL.where(SSL.SMU==demand['SMU']).dropna()
    SMU = score_df.loc[SMU.index.tolist(),:].sort_values(['Fitment Score'],ascending=False)
    SSL = SSL.where(SSL.SMU!=demand['SMU']).dropna()
    SSL = score_df.loc[SSL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False)
    SL = SL.where(SL.Sub_Service_Line!=demand['Sub-Service Line']).dropna()
    SL = score_df.loc[SL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False)
    NSL = supply.where(supply.Service_Line!=demand['Service Line']).dropna()
    NSL = score_df.loc[NSL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False)

    recommendation = pd.concat([SMU,SSL,SL,NSL])
    recommendation['Rank'] = list(range(1,recommendation.shape[0]+1))

    return recommendation