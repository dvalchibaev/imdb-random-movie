import os
import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import aiofile



URL = "https://datasets.imdbws.com/"
REPORTS_FOLDER = "../../imdb/"
FILES_PATH = os.path.join(REPORTS_FOLDER, "files")


def parse_site(url: str = URL, path: str = 'imdb-site.html'):
    page = requests.get(url)
    with open(path, 'w') as file:
        file.write(page.text)


def get_imdb_links(url: str = URL):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("a")
    output = []
    for result in results:
        output.append(result.get('href'))
    return output


# скопировано отсюда: https://gist.github.com/darwing1210/c9ff8e3af8ba832e38e6e6e347d9047a
def download_files_from_report(urls):
    os.makedirs(FILES_PATH, exist_ok=True)
    sema = asyncio.BoundedSemaphore(5)

    async def fetch_file(session, url):
        fname = url.split("/")[-1]
        async with sema:
            async with session.get(url) as resp:
                assert resp.status == 200
                data = await resp.read()

        async with aiofile.async_open(
            os.path.join(FILES_PATH, fname), "wb"
        ) as outfile:
            await outfile.write(data)

    async def main():
        total_timeout = aiohttp.ClientTimeout(total=30*60)
        async with aiohttp.ClientSession(timeout=total_timeout) as session:
            tasks = [fetch_file(session, url) for url in urls]
            await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


if __name__ == '__main__':
    links = get_imdb_links(URL)
    download_files_from_report(links[1:])
