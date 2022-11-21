import instaloader
from flask import send_file
from instaloader import Post
import urllib.request
import requests
import random


def get_proxies(key):
    res = requests.get("https://proxy.webshare.io/api/proxy/list/", headers={"Authorization": f'Token {key}'})
    proxies = []
    for x in res.json()["results"]:
        proxy = f'{x["username"]}:{x["password"]}@{x["proxy_address"]}:{x["ports"]["http"]}'
        proxies.append(proxy)
    return proxies


def test():
    url = 'Cj1srKULYTx'
    j = instaloader.Instaloader()

    post = Post.from_shortcode(j.context, url)
    print(type(post))
    print(post.video_url)
    urllib.request.urlretrieve(post.video_url, 'abc2.mp4')
    return

    # i.download_post(post,target='download_post')


def download_post(url,media_type):
    # proxies = get_proxies('36qcz0kwoz6gxm1crsxuzun66h3nl2k07p6wpkgv')
    # proxy = random.choice(proxies)
    # proxy_fetch = {"https": f"http://{proxy}", "http": f"http://{proxy}"}
    # print(proxy_fetch)
    i = instaloader.Instaloader()
    post = Post.from_shortcode(i.context, url)

    # print(post.video_url)
    # print(post.url)
    # urllib.request.urlretrieve(post.video_url, 'abc3.mp4')
    #print(post.video_url)
    print(post.date_utc)

    st = str(post.date_utc)
    st = st.replace(':', '-')
    st = st.replace(' ', '_')
    if media_type == 'p':
        st = st + '_UTC_1.jpg'
    else:
        st = st + '_UTC.mp4'
    print(i.download_post(post, target='download_post'))
    print(st)


    #if post.video_url is not None:
        #send_file(path_or_file= post.video_url, as_attachment=True)
    return st

# test()
