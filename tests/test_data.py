import json

import pytest

from dense_retrieval.data import load_dataset


def test_load_dataset_returns_all_examples() -> None:
    examples = load_dataset()

    assert len(examples) == 10
    assert examples[0]["query"] == "What causes rain?"
    assert "water vapor" in examples[0]["positive"]


def test_load_dataset_rejects_empty_query(tmp_path) -> None:
    data_path = tmp_path / "invalid.jsonl"
    record = {"query": "  ", "positive": "A valid passage."}
    data_path.write_text(json.dumps(record) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="query"):
        load_dataset(data_path)


def test_load_dataset_rejects_invalid_json(tmp_path) -> None:
    data_path = tmp_path / "invalid.jsonl"
    data_path.write_text("{invalid json}\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid JSON"):
        load_dataset(data_path)