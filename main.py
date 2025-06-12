from src.config import Config
from src.data_loading.load_data import DATALoader


def main():
    cf = Config()

    # === data loading ===
    data_loader = DATALoader(data_path=cf.DATA_FOLDER)
    data = data_loader.load_data()
    print(f"Loaded {len(data)} data items from {cf.DATA_FOLDER}")
    

if __name__ == "__main__":
    main()