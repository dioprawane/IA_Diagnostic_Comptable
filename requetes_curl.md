1. Requête
```
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "purpose=fine-tune" \
  -F "file=@/c/Users/Diop Serigne Rawane/OneDrive/VsCode/IA/IA130624/ia_diagnostic_comptable/traning.jsonl"
```

1. Réponse
```
{
  "object": "file",
  "id": "file-tTmgegW968xkFs1yi8kSPX75",
  "purpose": "fine-tune",
  "filename": "traning.jsonl",
  "bytes": 1069,
  "created_at": 1718310229,
  "status": "processed",
  "status_details": null
}
```


2. Requête
```
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "purpose=fine-tune" \
  -F "file=@/c/Users/Diop Serigne Rawane/OneDrive/VsCode/IA/IA130624/ia_diagnostic_comptable/traning.jsonl"
```

2. Réponse
```
{
  "object": "file",
  "id": "file-iIB2MnYOJDzXVpwsNF8gket8",
  "purpose": "fine-tune",
  "filename": "traning.jsonl",
  "bytes": 1069,
  "created_at": 1718310290,
  "status": "processed",
  "status_details": null
}
```


3. Requête
```
curl https://api.openai.com/v1/fine_tuning/jobs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "training_file": "file-iIB2MnYOJDzXVpwsNF8gket8",
    "model": "gpt-3.5-turbo"
  }'
```

3. Réponse
```
{
  "object": "fine_tuning.job",
  "id": "ftjob-upihuK1CfCp1i6kv0b4FwSbV",
  "model": "gpt-3.5-turbo-0125",
  "created_at": 1718310423,
  "finished_at": null,
  "fine_tuned_model": null,
  "organization_id": "org-SaK9P3bNrttJbBOx6qeg3dOA",
  "result_files": [],
  "status": "validating_files",
  "validation_file": null,
  "training_file": "file-iIB2MnYOJDzXVpwsNF8gket8",
  "hyperparameters": {
    "n_epochs": "auto",
    "batch_size": "auto",
    "learning_rate_multiplier": "auto"
  },
  "trained_tokens": null,
  "error": {},
  "user_provided_suffix": null,
  "seed": 708328759,
  "estimated_finish": null,
  "integrations": []
}
```