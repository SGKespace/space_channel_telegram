import requests
from pathlib import Path


def download_file(path_to_save_files, url):
    response = requests.get(url)
    response.raise_for_status()

    with path_to_save_files.open('wb') as file:
        file.write(response.content)


def latest_spacex_launch():
    api_url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def spacex_launch_urls(response):
    url = response['links']['flickr']['original']
    return url


def main():
    file_name = 'hubble.jpeg'
    path_to_save_files = Path(f'images/{file_name}')
    path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # download_file(path_to_save_files, url)

    responce = latest_spacex_launch()
    url = spacex_launch_urls(responce)
    if not url:
        print('Ссылки еще не выложили')
    else:
        print(url)




if __name__ == '__main__':
    main()