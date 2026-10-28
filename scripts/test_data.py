from dense_retrieval.data import load_dataset


def main() -> None:
    examples = load_dataset()

    print(f"Loaded {len(examples)} examples.")
    print(f"First query: {examples[0]['query']}")
    print(f"First positive passage: {examples[0]['positive']}")


if __name__ == "__main__":
    main()