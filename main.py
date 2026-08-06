# def main():
#     print("Global Job Market ETL pipeline entry point")


# if __name__ == "__main__":
#     main()
from config.config import (
    ADZUNA_APP_ID,
    COUNTRY,
    RESULTS_PER_PAGE,
    RAW_DATA_PATH,
)

print("Configuration Loaded Successfully")
print("----------------------------------")
print(f"Country          : {COUNTRY}")
print(f"Results Per Page : {RESULTS_PER_PAGE}")
print(f"Raw Path         : {RAW_DATA_PATH}")
print(f"App ID Loaded    : {'YES' if ADZUNA_APP_ID else 'NO'}")