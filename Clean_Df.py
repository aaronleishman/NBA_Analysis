import pandas as pd


# load detail csv file
g_details_df = pd.read_csv('games_details.csv')

# load summary csv file
g_summary_df = pd.read_csv('games.csv')
 
# Only need 2 columns from summary file
g_summary_df = g_summary_df[['GAME_DATE_EST','GAME_ID']]

# merge DF
merge_df = pd.merge(g_details_df,g_summary_df, on= 'GAME_ID', how='left')

# convert Date column to Date type
merge_df['GAME_DATE_EST'] = pd.to_datetime(merge_df['GAME_DATE_EST'])

#filter dates so it doesn't include 2019-2020 season
merge_df = merge_df.loc[merge_df['GAME_DATE_EST'] < '2019-07-01']

# Add column Year-Month 
merge_df['Year-Month'] = merge_df['GAME_DATE_EST'].map(lambda x: 100*x.year + x.month)
# Convert to string and add dash between year and month
merge_df['Year-Month'] = merge_df['Year-Month'].astype(str).map(lambda x: x[0:4] + '-' + x[4:6])

# remove text columns: 'Comment' and 'Start Postion'
merge_df = merge_df.drop(columns=['COMMENT','START_POSITION'])

# remove players that didn't play
merge_df = merge_df.dropna()




merge_df.to_pickle('dataset.pickle')
# ds_3pt = 

print(merge_df.head())
# print('filter', merge_df.info())




# example
# data.groupby(['month', 'network_type'])['date'].sum()