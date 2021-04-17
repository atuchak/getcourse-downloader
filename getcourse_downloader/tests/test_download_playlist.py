from getcourse_downloader.downloader import download_playlist


def test_download_playlist_test():
    url = 'https://player02.getcourse.ru/player/805d210faad94a1468507a243fffb5bb/2944c7f6180726e168593c2f03127f0e/media/1080.m3u8?sid=sid&host=vh-40&user-cdn=&akamai-cdn-pr=0&v=4%3A2%3A1%3A0'
    url = 'https://player02.getcourse.ru/player/805d210faad94a1468507a243fffb5bb/2944c7f6180726e168593c2f03127f0e/master.m3u8?sid=sid&host=vh-40&user-cdn=&akamai-cdn-pr=0&v=4%3A2%3A1%3A0'
    playlist = download_playlist(url)
    print(playlist)


test_download_playlist_test()
