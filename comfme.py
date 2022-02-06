from sys import argv
from tqdm import tqdm
from requests import get


def _help():
    print("usage : python3 comfme.py <url>")

def download(url):
    response = get(url, stream=True)
    file_name = url.split("/")[-1]
    
    total_size = int(response.headers['content-length'])
    
    return response, total_size, file_name

def assemble(url):    
    response, total_size, file_name = download(url)
    chunk_size = 1024
    with open(file_name, 'wb') as file:
       for data in tqdm(iterable = response.iter_content(chunk_size=chunk_size), total = total_size / chunk_size, unit="KB"):
           file.write(data)
        

assemble(argv[1]) if len(argv)>1 else _help()
