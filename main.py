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
    responce = latest_spacex_launch()
    urls = spacex_launch_urls(responce)
    basis_file_name = responce['id'] + "_"
    if not urls:
        print('Ссылки еще не выложили')
    else:
        for urls_number, url in enumerate(urls):
            path_to_save_files = Path(f'images/{basis_file_name + str(urls_number)}.jpeg')
            path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
            download_file(path_to_save_files, url)


if __name__ == '__main__':
    main()