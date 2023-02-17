

# Fine-Tuning guide: https://platform.openai.com/docs/guides/fine-tuning/fine-tuning
# YouTube: https://www.youtube.com/watch?v=3EdEw4gyr-s

# The following Steps to fine-tuning:

# Step 1: Setup Environment:
### Install openai package on your machine:
>> ```pip install --upgrade openai```

### API key: export it as an environment variable:
>> ```export OPENAI_API_KEY="your-api-key" ```

# Step 2: Prepare json data:
### Prompt an Completion Formating: input file is basketball_data.csv, output file is going to be prompt_completion_pairs.json
>> ```python prompt-completion-formating-to-json.py```

# Step 3: Prepare training jsonl data:
### converting prompt_completion_pairs.json to jsonl, the jsonl is going to be training-file
>> ```openai tools fine_tunes.prepare_data -f <LOCAL_FILE>```
### Sample:
>>```openai tools fine_tunes.prepare_data -f prompt_completion_pairs.json```

# Step 3: Fine-Tune:
### create custom model by using the prompt_completion_pairs_prepared.jsonl file
>> ```openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>```
### Sample:
```openai api fine_tunes.create -t prompt_completion_pairs_prepared.jsonl -m curie```

