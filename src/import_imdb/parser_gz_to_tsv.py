import gzip
import shutil
import os


def walk_dir(dir_path: str, file_type: str):
    result = []
    for root, dirs, files in os.walk(dir_path):
        result.extend(files)
    return [file for file in result if file.endswith(file_type)]


def parse(file_gz: str, gz_dir: str, tsv_dir: str):
    print(file_gz)
    file_tsv = ".".join(file_gz.split('.')[:-1])
    os.makedirs(tsv_dir, exist_ok=True)
    with gzip.open(f'{gz_dir}{file_gz}', 'rb') as f_in:
        with open(f'{tsv_dir}{file_tsv}', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def main(gz_dir: str, tsv_dir):
    for file in walk_dir(gz_dir, '.gz'):
        print(parse(file, gz_dir, tsv_dir))


if __name__ == "__main__":
    main('../../imdb/files/', '../imdb/files_tsv/')
