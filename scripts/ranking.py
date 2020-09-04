import pandas as pd
import numpy as np

supply = pd.read_excel('data.xlsx', header=0, sheet_name=1, index_col=0)

def ranking(score_df,demand):
    segments = ['Best Fit', 'Stretched Fit', 'Best Bet', 'No Segment']
    data = []
    score_df = score_df.where(score_df['Fitment Score']>0).dropna()
    for segment in segments:
        segmented = score_df.where(score_df['Fitment Segment']==segment).dropna()
        segmented_supply = supply.loc[segmented.index.tolist(),:]
        SL = segmented_supply.where(segmented_supply.Service_Line==demand['Service Line']).dropna()
        SSL = SL.where(SL.Sub_Service_Line==demand['Sub Service Line']).dropna()
        SMU = SSL.where(SSL.SMU==demand['SMU']).dropna()
        SMU = segmented.loc[SMU.index.tolist(),:].sort_values(['Fitment Score'],ascending=False)
        SSL = SSL.where(SSL.SMU!=demand['SMU']).dropna()
        SSL = segmented.loc[SSL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False)
        SL = SL.where(SL.Sub_Service_Line!=demand['Sub Service Line']).dropna()
        SL = segmented.loc[SL.index.tolist(), :].sort_values(['Fitment Score'], ascending=False)
        NSL = segmented_supply.where(segmented_supply.Service_Line !=demand['Service Line']).dropna()
        NSL = segmented.loc[NSL.index.tolist(),:].sort_values(['Fitment Score'],ascending=False)
        df = pd.concat([SMU, SSL, SL, NSL])
        data.append(df)

    recommendation = pd.concat([data[0], data[1], data[2], data[3]])
    recommendation['Fitment Rank'] = list(range(1,recommendation.shape[0]+1))

    return recommendation
