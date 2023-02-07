import requests
from pathlib import Path


def download_file(file_name, url):
    path_to_save_files = Path(f'images/{file_name}')
    path_to_save_files.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with path_to_save_files.open('wb') as file:
        file.write(response.content)


def main():
    file_name = 'hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_file(file_name, url)


if __name__ == '__main__':
    main()