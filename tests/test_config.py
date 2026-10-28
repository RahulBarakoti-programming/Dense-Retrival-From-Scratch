from dense_retrieval.config import load_config


def test_load_config_returns_expected_values() -> None:
    config = load_config()

    assert config["model"]["embedding_dim"] == 128
    assert config["model"]["max_length"] == 128
    assert config["training"]["batch_size"] == 32
    assert config["training"]["epochs"] == 10


def test_load_config_contains_evaluation_settings() -> None:
    config = load_config()

    assert config["evaluation"]["k_values"] == [1, 5, 10]