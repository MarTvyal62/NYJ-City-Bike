def period_iterator(year:list,start_m:int, stop_m:int)->list:
    """
    year list of strings
    """
    YEAR = year
    MONTH =  [str(i+1) if i+1>9 else "0" + str(i+1) for i in range(start_m, stop_m)]

    periods = []

    for i in YEAR:
        for j in MONTH:
            k = i+j
            periods.append(k)
    return periods


import shutil
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError
from zipfile import ZipFile

def download_jersey_tripdata_zip_and_extract_to_local(periods:list, base_url:str, local_path:str)->None:
    """
    Download tripdata zip file from url and save to local path
    """
    for i in periods:

        try:
            file_name = f"JC-{i}-citibike-tripdata.csv.zip"
            url = f"{base_url}/{file_name}"

            zip_path = local_path / file_name
            urlretrieve(url, zip_path)

        except (HTTPError, URLError, FileNotFoundError):
            file_name = f"JC-{i}-citibike-tripdata.zip"
            url = f"{base_url}/{file_name}"

            zip_path = local_path / file_name
            urlretrieve(url, zip_path)

        with ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(local_path)
        print(f'{file_name}  Extracted')
        zip_path.unlink()
        print(f"{file_name} removed.")




