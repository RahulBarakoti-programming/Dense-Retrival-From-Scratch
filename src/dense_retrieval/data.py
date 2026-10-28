from pathlib import Path
import json
from typing import TypedDict


ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "samples" / "toy_retrieval.jsonl"

class RetrievalExamples(TypedDict):
    """A query paired with relevant passage"""

    query : str
    positive : str


def load_dataset(data_path : str | Path = DATA_PATH) -> list[RetrievalExamples]:
    """load and validate query-positive-passage pairs from a JSON file."""
    data_path = Path(data_path)
    examples : list[RetrievalExamples] = []
    if not data_path.is_file():
        raise FileNotFoundError(f"there is no data at {data_path}")
    with data_path.open('r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON on line {line_number} of {data_path}"
                ) from exc
            if not isinstance(record, dict):
                raise ValueError(
                    f"Excepted a JSON object on line {line_number}"
                )
            query = record.get("query")
            positive = record.get("positive")
            if not isinstance(query, str) or not query.strip():
                raise ValueError(
                    f"Missing or empty query on lilne {line_number}"
                )
            if not isinstance(positive, str) or not positive.strip():
                raise ValueError(
                    f"Missing or empty positive passage on line {line_number}"
                )
            examples.append(
                {
                    "query": query.strip(),
                    "positive": positive.strip()
                }
            )
        return examples