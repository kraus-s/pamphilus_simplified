import requests
import os
from utils.constants import *
from tqdm import tqdm


def download_onp_data():
    print("Downloading ONP data...")
    if not os.path.exists(ONP_DATABASE_PATH):
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(ONP_DB_URL, stream=True)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                with open(ONP_DATABASE_PATH, 'wb') as file:
                    total_length = int(response.headers.get('content-length'))
                    with tqdm(total=total_length, unit='B', unit_scale=True) as pbar:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                file.write(chunk)
                                pbar.update(len(chunk))
                print(f"File downloaded and saved as '{ONP_DATABASE_PATH}'")
            else:
                print(f"Failed to download the file. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    print("Command line setup. Also available in WebApp. Run webapp by typing pipenv run run or continue here.")
    print("This script will download the ONP database and the Levenshtein database.")
    print("To run the analysis script, use the webapp or use 'pipenv run analysis'")
    input("Press Enter to continue...")
    print("Downloading ONP data...")
    download_onp_data()
    download_levenshtein_data()
    print("App setup successfull")
    print("All done. Bye!")