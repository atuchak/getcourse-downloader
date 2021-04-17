from getcourse_downloader.downloader import extract_video_chunks

video_playlist = '''\
#EXTM3U
#EXT-X-TARGETDURATION:4
#EXT-X-ALLOW-CACHE:YES
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PLAYLIST-TYPE:VOD

#EXTINF:3.033333,
https://vh-42-msk-storage-9ce96802-push.getcourse.kinescopecdn.net/media/805d210faad94a1468507a243fffb5bb/1080p_00000.ts?sig=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZDVfdXJsIjoiZjRjNTFjODJlYmMyZjU1YTAzMjRiZjAxZjBiODcxYTQifQ.sJE9gqv1uryF$
#EXTINF:3.000000,
https://vh-42-msk-storage-9ce96802-push.getcourse.kinescopecdn.net/media/805d210faad94a1468507a243fffb5bb/1080p_00001.ts?sig=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZDVfdXJsIjoiMDY2NDc5MTE4MjNlZDAyMjI3Y2E0ZGI4YzI0YThkZjgifQ.xs8pSS_VRk4P$
#EXTINF:3.000000,
https://vh-42-msk-storage-9ce96802-push.getcourse.kinescopecdn.net/media/805d210faad94a1468507a243fffb5bb/1080p_00002.ts?sig=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZDVfdXJsIjoiYjM2YmVkYWVmMTBiMjhhZDljODk5YzgxOTgzZTczNmUifQ.ekRC1ZQnsQrz$
#EXTINF:3.000000,
https://vh-42-msk-storage-9ce96802-push.getcourse.kinescopecdn.net/media/805d210faad94a1468507a243fffb5bb/1080p_00003.ts?sig=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZDVfdXJsIjoiNTA3NmI5NmM5ODgwYWI0Y2IzNDhlN2MwZmQ1MWU5ODEifQ.731heesH-C47$
'''


def test_extract_video_chunks():
    chunks_urls = extract_video_chunks(video_playlist)
    print(chunks_urls)


test_extract_video_chunks()
