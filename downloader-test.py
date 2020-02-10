import os, sys
import requests
from tqdm import tqdm
from docopt import docopt


def download_file(link, filename=None, csize=1000 * 1000):
    r = requests.get(link, stream=True)
    file_size = int(r.headers['Content-Length'])
    if filename is None:
        filename = r.url.split("/")[-1]
    if os.path.exists(filename):
        first_byte = os.path.getsize(filename)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    r = requests.get(link, headers={"Range": "bytes=%s-%s" % (first_byte, file_size)}, stream=True)
    with tqdm(total=file_size, initial=first_byte, unit='B', unit_scale=True, desc=filename) as pbar:
        with open(filename, 'ab') as fp:
            for chunk in r.iter_content(chunk_size=csize):
                fp.write(chunk)
                pbar.update(csize)
    return file_size


def main(path):
    print("Task processing: 4/4")
    i = 0
    with open(path) as f:
        for line in f:
            download_file(line)
            print("download file: " + str(i))
            i += 1

    os.remove("./download_link.log")
    print("Task complete: 4/4")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        exit("Error path environment")

    main(sys.argv[0])
