import csv
import json

# Define the input and output file paths
input_file = "basketball_data.csv"
output_file = "prompt_completion_pairs.json"

# Define a function to generate the completion string for a given row of data


def generate_completion(row):
    completion = (f"{row['Player']} is a {row['Position']} for the {row['Team']}. "
                  f"In {row['GP  Games played']} games, they averaged {row['MPG  Minutes Per Game']} minutes per game, "
                  f"scoring {row['PPG  Points Per Game']} points per game. "
                  f"They made {row['FGM  Field Goals Made']} out of {row['FGA  Field Goals Attempted']} field goal attempts, "
                  f"for a shooting percentage of {row['FG%  Field Goal Percentage']}. "
                  f"They also made {row['3FGM  Three-Point Field Goals Made']} out of {row['3FGA  Three-Point Field Goals Attempted']} three-point attempts, "
                  f"for a three-point shooting percentage of {row['3FG%  Three-Point Field Goal Percentage']}. "
                  f"They made {row['FTM  Free Throws Made']} out of {row['FTA  Free Throws Attempted']} free throw attempts, "
                  f"for a free throw percentage of {row['FT%  Free Throw Percentage']}.")
    return completion


# Read the basketball data from the CSV file
with open(input_file, "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Generate the prompt and completion pairs
pairs = []
for row in rows:
    prompt = f"What are {row['Player']}'s basketball statistics?"
    completion = generate_completion(row)
    pair = {"prompt": prompt, "completion": completion}
    pairs.append(pair)

# Export the prompt and completion pairs to a JSON file
with open(output_file, "w") as f:
    json.dump(pairs, f)
