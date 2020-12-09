import requests
import pandas as pd
import numpy as np
import datetime as dt
from model_functions import filter_columns, calc_distance, find_player, normalize, vorp, clean_dataframe, player_comparison_tool

today = dt.datetime.today().strftime('%m%d%Y')  

cols_to_norm = [
    'pts',
    'min',
    'fgm',
    'fga',
    'fg3m',
    'fg3a',
    'ftm',
    'fta',
    'oreb',
    'dreb',
    'ast',
    'stl',
    'tov',
    'blk']

ten_players = [
    201935,
    203081,
    201942,
    201937,
    202339,
    203496,
    203497,
    201567,
    202331,
    202691]

season_list = [
    '1996-97',
    '1997-98',
    '1998-99',
    '1999-00',
    '2000-01',
    '2001-02',
    '2002-03',
    '2003-04',
    '2004-05',
    '2005-06',
    '2006-07',
    '2007-08',
    '2008-09',
    '2009-10',
    '2010-11',
    '2011-12',
    '2012-13',
    '2013-14',
    '2014-15',
    '2015-16',
    '2016-17',
    '2017-18',
    '2018-19',
    '2019-20',
    '2020-21']

'''five_players = [
    1629027,
    1629029,
    1626164,
    2544,
    203076]'''

games_played = 10

df = pd.read_csv('player_general_traditional_per_game_data_{}.csv'.format(today), header=0)
df_final = clean_dataframe(df, '2019-20', 10)

# get just the names from nba_data.py run CSV
df_names = pd.read_csv('player_id_player_name.csv')
# save player_ids to a list to for loop over
all_player_ids = df_names['player_id'].to_list()

# create an empty list to append to
final_projections = []

# for baller_id in player_ids:
for baller_id in all_player_ids:
    current_player_id = baller_id
    current_player_season = '2019-20'
    projections = player_comparison_tool(df_final, current_player_season, current_player_id)
    if (projections == None):
        continue
    final_projections.append(projections)

# convert the list to a dataframe
my_projections = pd.DataFrame(final_projections)
my_projections.sample(5)

# join the player name to the projections so we know who to look at
final_stat_df = pd.merge(my_projections, df_names, left_on=['player_id'], right_on=['player_id'], how='inner')
# save it to a new CSV so we can read it into Sheets and own the draft!
final_stat_df.to_csv('2019_20_projections.csv', index = False)