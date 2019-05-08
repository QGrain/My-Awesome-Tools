# coding: utf-8
import re
import requests
from pathlib import Path
from time import time, perf_counter
from fake_useragent import UserAgent
 
 
def download_file_from_url(dl_url, file_name, headers):
    file_path = Path(__file__).parent.joinpath(file_name)
    if file_path.exists():
        dl_size = file_path.stat().st_size
    else:
        dl_size = 0
 
    headers['Range'] = f'bytes={dl_size}-'
    response = requests.get(dl_url, stream=True, headers=headers)
 
    print('\n\n' + '*' * 30 + '下载信息' + '*' * 30)
    total_size = int(response.headers['content-length'])
    print(
        f'\n\n文件名称:{file_name}\t\t已下载文件大小:{dl_size / 1024 / 1024:.2f}M\t\t文件总大小:{total_size/1024/1024:.2f}M\n\n')
    start = perf_counter()
 
    data_count = 0
    count_tmp = 0
    start_time = time()
    with open(file_path, 'ab') as fp:
        for chunk in response.iter_content(chunk_size=512):
            data_count += len(chunk)
            now_pross = (data_count / total_size) * 100
            mid_time = time()
            if mid_time - start_time > 0.1:
                speed = (data_count - count_tmp) / 1024 / (mid_time - start_time)
                start_time = mid_time
                count_tmp = data_count
                print(
                    f"\rDownloading.........{now_pross:.2f}%\t{data_count//1024}Kb/{total_size//1024}Kb\t当前下载速度:{speed:.2f}Kb/s", end='')
            fp.write(chunk)
    
    end = perf_counter()
    diff = end - start
    speed = total_size/1024/diff
 
    print(
        f'\n\n下载完成!耗时:{diff:.2f}秒,  平均下载速度:{speed:.2f}Kb/s!\n文件路径:{file_path}\n')
 
 
if __name__ == '__main__':
    url = 'https://software-download.microsoft.com/db/Win10_1803_Chinese(Simplified)_x64.iso?t=338bc034-92a0-4207-a311-029453b2a48c&e=1556284212&h=47a7b1f80674ca847194d13b14fd82e5'
    #filename = url.rpartition('/')[-1]
    filename = 'win10_1803_x64.iso'
    headers = {
        'User-Agent': UserAgent().random, }
    download_file_from_url(url, filename, headers)