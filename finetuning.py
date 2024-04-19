import pandas as pd
import json
import os

if __name__ == "__main__":
    system_prompt = "You are a seasoned business development expert with in depth technical expertise in the field of data engineering, machine learning and AI. You have decades of experience in writing upwork proposals to win work on upwork."
    df = pd.read_csv("data/proposals.csv")

    # Create the output directory
    os.makedirs("data/finetuning", exist_ok=True)

    with open("data/proposals.jsonl", "w") as f:
        for i, row in df.iterrows():
            json.dump(
                {
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {
                            "role": "user",
                            "content": f"Title: {row['title']}\nDescription: {row['jd']}\n",
                        },
                        {"role": "assistant", "content": row["proposal"]},
                    ]
                },
                f,
            )
            f.write("\n")
