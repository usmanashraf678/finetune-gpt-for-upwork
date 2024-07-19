# Finetuning GPT for upwork proposals

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate the Virtual Environment

```bash
Linux: source venv/bin/activate
Windows: .\venv\Scripts\activate

```

## Install the requirements
```bash
pip install -r requirements.txt
```

## Run the fomratting script
```bash
python finetuning.py
```

## Notes
- You can change the system prompt as per your preference in the `finetuning.py` file. 
- Also, feel free to use your own proposals. You would need to save them as the `proposals.csv` file in the `data` folder.

## Supporting materials
More details about the project can be found in [this](https://www.youtube.com/watch?v=lDnrPbJcm-E) youtube video.
