import pandas as pd

def load_excel(file_path):
    return pd.read_excel(file_path, engine='openpyxl')

def extract_first_row_columns(excel_data, columns_to_extract):
    first_row = excel_data[columns_to_extract].iloc[0]
    for column in columns_to_extract:
        print(f"{column} : {first_row[column]}")

def get_unique_teams(excel_data):
    selected_columns = excel_data[['team_id', 'team_name', 'team_formation']]
    unique_teams = selected_columns.drop_duplicates(subset=['team_id'])
    for index, row in unique_teams.iterrows():
        print(f"team_name: {row['team_name']}, team_id: {row['team_id']}, team_formation: {row['team_formation']}")

def get_unique_players(excel_data):
    selected_columns = excel_data[['team_name', 'player_id', 'player_name']]
    unique_players = selected_columns.drop_duplicates()
    unique_players = unique_players[unique_players['player_id'] != 0]
    grouped_teams = unique_players.groupby('team_name')
    for team_name, group in grouped_teams:
        print(f"Team: {team_name}")
        for index, row in group.iterrows():
            print(f"Player ID: {row['player_id']}, Player Name: {row['player_name']}")
        print("\n")

def get_unique_goalkeepers(excel_data):
    selected_columns = excel_data[['goalkeeper_id', 'goalkeeper_name', 'team_name']]
    unique_goalkeepers = selected_columns.drop_duplicates(subset=['goalkeeper_id'])
    unique_goalkeepers = unique_goalkeepers.dropna(subset=['goalkeeper_id'])
    
    # Get the unique team names
    unique_teams = unique_goalkeepers['team_name'].unique()
    if len(unique_teams) == 2:
        reversed_team_names = {unique_teams[0]: unique_teams[1], unique_teams[1]: unique_teams[0]}
    else:
        reversed_team_names = {team: team for team in unique_teams}

    for index, row in unique_goalkeepers.iterrows():
        reversed_team_name = reversed_team_names[row['team_name']]
        print(f"goalkeeper_name: {row['goalkeeper_name']}, goalkeeper_id: {row['goalkeeper_id']}, team_name: {reversed_team_name}")


def get_unique_team_roles(excel_data):
    home_away_columns = excel_data[['side_home', 'side_away']]
    teams_roles = []
    for index, row in home_away_columns.iterrows():
        home_team = {'team_id': row['side_home'], 'role': 'side_home'}
        away_team = {'team_id': row['side_away'], 'role': 'side_away'}
        if home_team not in teams_roles:
            teams_roles.append(home_team)
        if away_team not in teams_roles:
            teams_roles.append(away_team)
    team_info_columns = excel_data[['team_id', 'team_name']].drop_duplicates()
    team_roles_df = pd.DataFrame(teams_roles)
    unique_teams_with_roles = pd.merge(team_roles_df, team_info_columns, left_on='team_id', right_on='team_id')
    for index, row in unique_teams_with_roles.iterrows():
        print(f"team_name: {row['team_name']}, team_id: {row['team_id']}, role: {row['role']}")

def check_is_goal(excel_data):
    goal_data = excel_data[excel_data['isGoal'] == True]
    for index, row in goal_data.iterrows():
        print(f"Player Name: {row['player_name']}, Team Name: {row['team_name']}, Match Timestamp: {row['matchTimestamp']}")

def get_unique_event_types_with_counts_and_teams(excel_data):
    event_columns = [
        'event_type_name', 'second_event_type_name_1', 'second_event_type_name_2',
        'second_event_type_name_3', 'second_event_type_name_4', 'second_event_type_name_5'
    ]
    
    for column in event_columns:
        print(f"Unique values in {column}:")
        unique_values_counts = excel_data[column].value_counts().dropna()
        
        for value, count in unique_values_counts.items():
            teams_count = excel_data[excel_data[column] == value]['team_name'].value_counts().to_dict()
            teams_str = ', '.join([f"{team}: {team_count}" for team, team_count in teams_count.items()])
            print(f"{value}: {count}, {teams_str}")
        print("\n")

def get_event_counts_for_each_player(excel_data):
    event_columns = [
        'event_type_name', 'second_event_type_name_1', 'second_event_type_name_2',
        'second_event_type_name_3', 'second_event_type_name_4', 'second_event_type_name_5'
    ]

    # Dictionary to hold event counts for each player
    player_event_counts = {}

    # Iterate over each event column
    for column in event_columns:
        for index, row in excel_data.dropna(subset=[column]).iterrows():
            player_name = row['player_name']
            team_name = row['team_name']
            event_type = row[column]

            if pd.isna(player_name):
                continue

            if team_name not in player_event_counts:
                player_event_counts[team_name] = {}

            if player_name not in player_event_counts[team_name]:
                player_event_counts[team_name][player_name] = {}

            if event_type not in player_event_counts[team_name][player_name]:
                player_event_counts[team_name][player_name][event_type] = 0

            player_event_counts[team_name][player_name][event_type] += 1

    # Print the results
    for team_name, players in player_event_counts.items():
        print(f"Team: {team_name}")
        for player_name, events in players.items():
            events_str = ', '.join([f"{event}: {count}" for event, count in events.items()])
            print(f"{player_name}: {events_str} \n")
        print("\n")

def get_event_counts_for_each_goalkeeper(excel_data):
    event_columns = [
        'event_type_name', 'second_event_type_name_1', 'second_event_type_name_2',
        'second_event_type_name_3', 'second_event_type_name_4', 'second_event_type_name_5'
    ]

    # Dictionary to hold event counts for each goalkeeper
    goalkeeper_event_counts = {}

    # Iterate over each event column
    for column in event_columns:
        for index, row in excel_data.dropna(subset=[column]).iterrows():
            goalkeeper_name = row['goalkeeper_name']
            team_name = row['team_name']
            event_type = row[column]

            if pd.isna(goalkeeper_name):
                continue

            if team_name not in goalkeeper_event_counts:
                goalkeeper_event_counts[team_name] = {}

            if goalkeeper_name not in goalkeeper_event_counts[team_name]:
                goalkeeper_event_counts[team_name][goalkeeper_name] = {}

            if event_type not in goalkeeper_event_counts[team_name][goalkeeper_name]:
                goalkeeper_event_counts[team_name][goalkeeper_name][event_type] = 0

            goalkeeper_event_counts[team_name][goalkeeper_name][event_type] += 1

    # Get the unique team names
    unique_teams = list(goalkeeper_event_counts.keys())
    if len(unique_teams) == 2:
        reversed_team_names = {unique_teams[0]: unique_teams[1], unique_teams[1]: unique_teams[0]}
    else:
        reversed_team_names = {team: team for team in unique_teams}

    # Print the results with reversed team names for goalkeepers
    for team_name, goalkeepers in goalkeeper_event_counts.items():
        reversed_team_name = reversed_team_names[team_name]
        print(f"Team: {reversed_team_name}")
        for goalkeeper_name, events in goalkeepers.items():
            events_str = ', '.join([f"{event}: {count}" for event, count in events.items()])
            print(f"{goalkeeper_name}: {events_str}")
        print("\n")



# Main execution
file_path = 'c:/Users/hp/Desktop/excel kora/AL_Ein_Match_event.xlsx'
excel_data = load_excel(file_path)

columns_to_extract = [
    'matchId', 'label', 'date', 'dateutc', 'winner', 'status', 'duration',
    'gameweek', 'competitionId', 'competition_name', 'seasonId', 'season_name',
    'roundId', 'round_name', 'matchPeriod'
]

extract_first_row_columns(excel_data, columns_to_extract)
print("\nUnique Teams:")
get_unique_teams(excel_data)
print("\nUnique Players:")
get_unique_players(excel_data)
print("\nUnique Goalkeepers:")
get_unique_goalkeepers(excel_data)
print("\nUnique Team State:")
get_unique_team_roles(excel_data)
print("\nGoals Information:")
check_is_goal(excel_data)
print("\nUnique Event Types with Counts and Teams:")
get_unique_event_types_with_counts_and_teams(excel_data)
print("\nEvent Counts for Each Player:")
get_event_counts_for_each_player(excel_data)
print("\nEvent Counts for Each Goalkeeper:")
get_event_counts_for_each_goalkeeper(excel_data)

