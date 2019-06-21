import requests


# :authority: spb.hh.ru
# :method: POST
# :path: /account/login?backurl=%2F
# :scheme: https
# cookie: ipp_uid1=1536749016595; ipp_uid2=QVfDm5clFksk07jI/tubOX5RRK2klQXNiB0uoJQ==; _ym_uid=1536749020925412210; __gads=ID=3584512de1a8fcfe:T=1536749021:S=ALNI_Mb-ur8OuWwhuRKUQ9vpgaUz9aqVUw; auth_user=4fc30a460afe05c1c82388bd0825a1e5; ipp_uid=1536749016595/QVfDm5clFksk07jI/tubOX5RRK2klQXNiB0uoJQ==; _ga=GA1.2.1999881560.1545837210; _fbp=fb.1.1549465209928.675361880; _ym_d=1552552983; hhuid=Z0cJBxj9Nol7JFxSuH4kJA--; clsc58=gcQZj8OVRcgWDHL8+DqJTT2dOR9ONoqYHpGaAxExk71oskDUajPfsZBXUROaQoeyeyX7B+RzjAeYXZ3kJLtfGVclE9Yi3Ai99NEphMmVC5MqvkCdkEfLTAbtq6xFhZuAbhEgL4iONncvmNQW3KORF0caVXc1lz2A6Obc4TES4tkPPCarqEYET0LkODXkaBmlubHdFRlriOpWblLThm5rZPeu61moE/rGwvz1+i1JhoLfKQcvOqv6A8MRQKC6lQuMUYeovr6v2n2KnACi8KlsSZqfgcYRh2cNs5tkUDgIlSM2nALV/4R0C9sr7ru0mqb38Kh8HJpaxxzycTGaHYc3nQ==; redirect_host=spb.hh.ru; region_clarified=spb.hh.ru; regions=2; _ga=GA1.1.1999881560.1545837210; _xsrf=520265d4db46e8e94bf5a672336660b9; _xsrf=520265d4db46e8e94bf5a672336660b9; display=desktop; GMT=3; _gid=GA1.1.570943472.1560442824; _ym_isad=2; _ym_visorc_156828=w; _ym_visorc_2646964=w; hhul=98c67ed5472e4714fca417487377f2e07d7c51cc2ba53180eb71699682babd96; hhul=98c67ed5472e4714fca417487377f2e07d7c51cc2ba53180eb71699682babd96; __zzat58=MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9DcHowb2odZ31gUXlaCnxXGhl4blZQEBBgb0Z0ei08aE9fSl5SSF4KayELIjBdLRtJUBg5Mzk0ZnBXJ2BMXx9HWVIIKiETd3AfQS91ZQkLOjB2N1dZJn4aXXIVfkRdCxtKXWkIQ1AYL0tfdSs+aR5fTlwRP0deMhcjVUE4WEtxTxx6dl99KkBrHWNLXiZIXU95LBV7J10tG0lQGBIWfV1YiA==; remember=0; lrp=""; lrr=""; hhtoken=xN6llI5djRqueO10qlAEPvBjiGt1; hhrole=anonymous; _gat_main=1; gssc58=a4VxYldtb0i5QSjRL0Lu+MRHuxx12dC4oSIqmWMVcQ2maZ8JLlv6hFqWP1d5Kp0PQPUS//xpSvNiSEBnIHuws/sM878mxHeWA8yCRKV54nWkFly4Cu/fmYvjnyhIVFVglse3wkptQup3n28pPEek0eUtikPFdNsoisjPrEJAAQ==; cfids58=emEOXwKkbkFpr3fkSEuC8GhPuJX1I1kS4MF9KEbnasvtN3g/JkL03NTX4jLJomt5fqlTFf32FqZwt5GZ4hFM+bqWU2QOFuCIaxAmwHDnCkLMouwKaQGJ9sueuEMLWIbNYm6BPso6Si2vqE402qiwoY11Xgke9xKOajkSZM7Y; cfids58=emEOXwKkbkFpr3fkSEuC8GhPuJX1I1kS4MF9KEbnasvtN3g/JkL03NTX4jLJomt5fqlTFf32FqZwt5GZ4hFM+bqWU2QOFuCIaxAmwHDnCkLMouwKaQGJ9sueuEMLWIbNYm6BPso6Si2vqE402qiwoY11Xgke9xKOajkSZM7Y; gssc58=a4VxYldtb0i5QSjRL0Lu+MRHuxx12dC4oSIqmWMVcQ2maZ8JLlv6hFqWP1d5Kp0PQPUS//xpSvNiSEBnIHuws/sM878mxHeWA8yCRKV54nWkFly4Cu/fmYvjnyhIVFVglse3wkptQup3n28pPEek0eUtikPFdNsoisjPrEJAAQ==; fgssc58=e09435da52ea5ce4e41b3f0b970223d8c942789e
raw_headers = '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
content-length: 205
content-type: application/x-www-form-urlencoded
referer: https://spb.hh.ru/
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
'''

headers = {}

data = {
    "backUrl": "https://hh.ru/",
    "failUrl": "/account/login?backurl=%2F",
    "username": "fatsumitsu@gmail.com",
    "password": "a7c1fe7986d0a868",
    "remember": "yes"
}

for i in raw_headers.split("\n"):
    j = i.split(": ", maxsplit=1)
    if len(j) == 2:
        headers[j[0]] = j[1]

for i in headers:
    print(i + ":", headers[i])


class HhGrabber:

    HOME = "http://spb.hh.ru"
    HEADERS = headers

    data = '''
    '''

    def __init__(self, uname, pw):
        print("making request...")
        self.session = requests.session()
        self.session.headers = self.HEADERS
        print(self.session.headers)
        self.auth(uname, pw)

    def auth(self, uname, pw):
        page = self.get_page(self.HOME)
        # print(page)
        xsrf = page.split('name="_xsrf" value="')[1].split('"></form>')[0]
        # print(xsrf)
        data["_xsrf"] = xsrf
        print(self.session.post("https://hh.ru/account/login?backurl=%2F", data=data).text)

    def get_page(self, url):
        print("getting page")
        x =  self.session.get(url).text
        # print(self.session.get(url))
        print("got page")
        return x


hg = HhGrabber("fatsumitsu@gmail.com", "a7c1fe7986d0a868")
