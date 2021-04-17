from pathlib import Path

import requests
from typing import List

urls = {
    'test': 'https://player02.getcourse.ru/player/805d210faad94a1468507a243fffb5bb/2944c7f6180726e168593c2f03127f0e/master.m3u8?sid=sid&host=vh-40&user-cdn=&akamai-cdn-pr=0&v=4%3A2%3A1%3A0'
}


def download_playlist(url: str) -> str:
    resp = requests.get(url)
    if resp.status_code != 200:
        return
    return resp.content.decode()


def extract_1080_playlist_url(m3u_content: str) -> str:
    for line in m3u_content.split('\n'):
        if line.startswith('http') and '1080' in line:
            return line


def extract_video_chunks(video_chunks_playlist: str) -> List[str]:
    chunks_urls = []
    for line in video_chunks_playlist.split('\n'):
        if line.startswith('http'):
            chunks_urls.append(line)

    return chunks_urls


def download_video(playlist_url, output_filename: Path):
    video_quality_playlist = download_playlist(playlist_url)
    if video_quality_playlist is None:
        return

    video_chunks_playlist_url = extract_1080_playlist_url(video_quality_playlist)
    if video_chunks_playlist_url is None:
        return

    video_chunks_playlist = download_playlist(video_chunks_playlist_url)
    if video_chunks_playlist is None:
        return

    video_chunks_urls = extract_video_chunks(video_chunks_playlist)
    if not video_chunks_urls:
        return

    if output_filename.exists():
        print(f'File {output_filename} already exists. Skip.')
        return
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0',
    }
    with open(output_filename, 'wb') as f:
        for chunk_url in video_chunks_urls:
            res = requests.get(chunk_url, headers=headers)
            if res.status_code != 200:
                print('Chunk download error. File "{output_filename}" is broken.')
                return
            f.write(res.content)


def run(output_dir='/tmp/luisa_gov'):
    for filename, playlist_url in urls.items():
        print(f'Downloading "{filename}".')
        output_filename = Path(output_dir) / f'{filename}.ts'
        output_filename.parent.mkdir(parents=False, exist_ok=True)
        download_video(playlist_url=playlist_url, output_filename=output_filename)


run()
