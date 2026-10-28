from dense_retrieval.config import load_config

def main()-> None:
    config = load_config()
    print("Config added successfully!")
    print(f"config: {config}")



if __name__ == "__main__":
    main()