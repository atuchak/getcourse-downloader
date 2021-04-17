from getcourse_downloader.downloader import extract_1080_playlist_url

playlist_content = '''\
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=768000,CODECS="mp4a.40.2, avc1.640028",RESOLUTION=640x360
https://player02.getcourse.ru/player/805d210faad94a1468507a243fffb5bb/2944c7f6180726e168593c2f03127f0e/media/360.m3u8?sid=sid&host=vh-40&user-cdn=&akamai-cdn-pr=0&v=4%3A2%3A1%3A0
#EXT-X-STREAM-INF:BANDWIDTH=1024000,CODECS="mp4a.40.2, avc1.640028",RESOLUTION=853x480
https://player02.getcourse.ru/player/805d210faad94a1468507a243fffb5bb/2944c7f6180726e168593c2f03127f0e/media/480.m3u8?sid=sid&host=vh-40&user-cdn=&akamai-cdn-pr=0&v=4%3A2%3A1%3A0
#EXT-X-STREAM-INF:BANDWIDTH=2560000,CODECS="mp4a.40.2, avc1.640028",RESOLUTION=1280x720
https://player02.getcourse.ru/player/805d210faad94a1468507a243fffb5bb/2944c7f6180726e168593c2f03127f0e/media/720.m3u8?sid=sid&host=vh-40&user-cdn=&akamai-cdn-pr=0&v=4%3A2%3A1%3A0
#EXT-X-STREAM-INF:BANDWIDTH=4096000,CODECS="mp4a.40.2, avc1.640028",RESOLUTION=1920x1080
https://player02.getcourse.ru/player/805d210faad94a1468507a243fffb5bb/2944c7f6180726e168593c2f03127f0e/media/1080.m3u8?sid=sid&host=vh-40&user-cdn=&akamai-cdn-pr=0&v=4%3A2%3A1%3A0
'''


def test_extract_1080_playlist():
    playlist_url = extract_1080_playlist_url(playlist_content)
    print(playlist_url)


test_extract_1080_playlist()