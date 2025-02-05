import pandas as pd

# Load the Excel file using openpyxl engine
file_path = 'c:/Users/hp/Desktop/excel kora/mini.xlsx'
excel_data = pd.read_excel(file_path, engine='openpyxl')

# Get the header row names
header_names = list(excel_data.columns)

# Print the header names
print(header_names)

'''
['index','id', 'matchId', 'label', 'date', 'dateutc', 'winner',
'status', 'duration', 'gameweek', 'competitionId', 'competition_name', 
'seasonId', 'season_name', 'roundId', 'round_name', 'matchPeriod', 
'minute', 'second', 'matchTimestamp', 'videoTimestamp', 'relatedEventId', 
'event_type_name', 'second_event_type_name_1', 'second_event_type_name_2',
'second_event_type_name_3', 'second_event_type_name_4', 'second_event_type_name_5',
'start_x', 'start_y', 'accurate', 'angle', 'height', 'length', 'endLocation_x', 
'endLocation_y', 'recipient_id', 'recipient_name', 'recipient_position', 'team_id',
'team_name', 'team_formation', 'opt_team_id', 'opt_team_name', 'opt_team_formation',
'player_id', 'player_name', 'player_position', 'bodyPart', 'isGoal', 'onTarget',
'goalZone', 'xg', 'postShotXg', 'goalkeeperActionId', 'goalkeeper_id', 'goalkeeper_name', 
'opt_player_id', 'opt_player_name', 'opt_player_position', 'duelType', 'keptPossession',
'progressedWithBall', 'stoppedProgress', 'recoveredPossession', 'takeOn', 'side', 
'relatedDuelId', 'opt_player_height', 'opt_player_first_touch', 'opt_yellowCard', 
'opt_redCard', 'opt_infraction_type', 'carry_progression', 'carry_endLocation_x_1',
'carry_endLocation_y_1', 'possession_id', 'possession_duration', 'possession_types',
'possession_types_2', 'possession_types_3', 'eventsNumber', 'eventIndex', 'possession_start_x_1',
'possession_start_y_1', 'possession_endLocation_x_1', 'possession_endLocation_y_1', 'attack_withShot',
 'attack_withShotOnGoal', 'attack_withGoal', 'attack_flank', 'possession_xg', 'event_duration', 'side_home', 'side_away']

'''