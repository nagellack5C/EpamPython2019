PKB_GET_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozila/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

HEADERS_LOGIN = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-length": "408",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://pikabu.ru",
    "referer": "https://pikabu.ru/",
    "cookie": "PHPSESS=rtltjpnvpblits7fk56knccsoi1r9vh9; is_scrollmode=1; pcid=zcKjXiQA0v2; rheftjdd=rheftjddVal; bs=G0; _ym_uid=1561840461882815179; _ym_d=1561840461; _ym_visorc_174977=w; _ym_isad=2; _ga=GA1.2.1204291216.1561840462; _gid=GA1.2.663245661.1561840462; _gat_gtag_UA_28292940_1=1; vn=eJwzNTc2NDAxBQAFtAFq; _ym_visorc_56459=w; fps=d05eeb13ea6aa22c712e60cb58fbdee2fd",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    # "x-csrf-token": "eb7du6u39k4hj0e63ko32on8e8vpkdp4",
    "x-requested-with": "XMLHttpRequest"
}

LOGIN_PAYLOAD = {
    "mode": "login",
    "username": "dasgeschaft",
    "password": "test@1992",
    "g-recaptcha-response": "03AOLTBLSS-eHoLGvIgnYKZxXX-MG23YFvc7gK5ZUS-uzAEhKgAdOwG3z-z3Xq1TPmWd5ZPtdJLFZojwtHRVPY99ZRnIfE__bBnoTYv49cMu-7UDyxoWoXPiLHt9TtKt4UxyZD4RrfqbRkLxZLsLolmdaE_hXZVTjqyN45Fyw70VYwMP0sJpE3D53AmW9UjXpcN63U7X0G7dOW8OypUa7rk-_Zu2MKCdll4D6mXR4_zDwKD5Wf_RmT-UfFyvkqF61THlUTx4xTk-ecX2r2kgAP9wEF43tqMHMOz9uujMleRWXF9OpjLx-3eNa9xg_xkyQLhUxXFsF_hqmjsWs5Amj2_6rEqRMbV0i2td4GrOibdzp4X43haMoeoS_hCKSK2WCw5oItqtoyhRmNDrR3DGdg9lbwKVc3tj3p_cz6FIqDNfbbTUBKkurCkZXoQE-Hp33z3nxYudG0bVOr0C6CMaRdiGKh1A9lePdig55gEXKuZkH0ldngAqawuN48K_2Fabvfe67ZVhynYKzgnbnYYTs9KmKVFM4bu9ODkEqsUHabnb61cLHWaWCahllmFE8paIcCJG5YD-bds2tInkTU2ukrV2bSObR39WqVNOqDDDt43Av4LpFZaG72epgrH7NuWTQVSrtOg5H3fTHDYKaN6JCcbX7C4nsl0qICRRPlHMtqShD1VSRxvvX2XgUWfjuvthdUOV2jI0g1nokgx2PLtaw0LbcOxQ8dKi2I5ASJOZNA10zJlot-KliDnKYrqi0XHRZpJnWAPkqhjbCBUm8E9qVeaa_6EuzHWOyjc5L2EHGbP2gzj0nRen9zvOrx6OX9lRWBj6NNpOcjWumS25QKjCGWDsOydliNXXfCCYRdnaunq1N2wAx1f6ge04nPhNzmhnVY56yasWCeWuu9Ued_qln1W70d4YiZ1RORJEjo94q-n_xgdv0yHZfDrt0505EO_uO8vX1I9rTwB6BI6G5IohHK2nFqMwfHxSn29F31ukQBV95vOfWSYdlM0Jh2T7jgMGSyjdluciW5Yx0NLe19ncOnZ6ST3T62YdSyL2en9MgsL-BFVG2DZP9qTC7OcOjC37DSl6AGp6dvuk9I7oiOV_UyVf0gtLNig8GHvYnirDq0wNZ_xk-EnBQwfIIqQw1WP-w718xWyjAPRoUVKo2C7bzdkMhlNP6DDMNM8TkyJW6HicJCig7sVVmSchI772-vVJ_VrSL6reOzEHhbiM1hIuPAmj12pzWsD_YUuEpBUq97ECGXNIYge_B2klCfOt4T16CFP0oh9yY5lSxONX6nxuZZEJMnWh-yUkz0yj1ZvfG5tWW1X5w8iYS3jvC3vvbqepapac653oQsaNzxMkfpBwDHvK-rZ-cG6L4VpJs7OmtZrvztHzaIx7ujl44M9s65xKupOWBXXZiedhhLkI8W8Njv94W0WIvQaP88k7dWWGs9Ch7NoySFujZa7VygxAYHdzsfYUF8Fv4-FUS7VJBttpgLfSFvg-Da-BEAUCM7pqZ0pDBGnEa2gcb-Z4q_WbNFqE9-VLoGXty298MRXIvC7VV7xaIIYTlc3l7KVb5ExO0lmnJwAG8qGcpuWLrYtyaBzGvZEAmhXkoDmgSx8Z6C-x5kM0YBsPcggDcuGxaYKl-zRJNDrh5oDvYJ_KXPdtnzqUCCgnUhiStt_xtjc2ocA7TytoKbybOFpOmjGh_odZJjz6zff4wK4_PG3bo96hPxs7RozrqX3rYxAthf_eoYKtVnyGQZsHiBr9DhTbzwo3ObalfzJ0uzD-QOvjtov9j7V6BDK9K_AoS6rY7vtRZiiH3EKCSaV9dXdthGHRMyEhDDQNgKYxLYJmhZIeCxfJvTU-Qabi8aj4X3HEKJ7qWmh3H7Bq_Zhp-C0UZpbl0nG0N5lwWhOtzXeC1RmiE"
}

HEADERS_LOGIN_2 = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-length": "408",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    # 'Content-Type': 'multipart/form-data',
    "cookie": "pkb_modern=11; _ym_uid=15618334081036135802; _ym_d=1561833408; bs=H0; _ym_visorc_174977=w; _ga=GA1.2.464527830.1561833408; _gid=GA1.2.2119849258.1561833408; _ym_isad=2; vn=eJwzM7cwNDIyBQAF1gFw; _ym_visorc_56459=w; fps=d05eeb13ea6aa22c712e60cb58fbdee2fd; ulfs=1561833430;",
    "origin": "https://pikabu.ru",
    "referer": "https://pikabu.ru/",

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    # "x-csrf-token": "eb7du6u39k4hj0e63ko32on8e8vpkdp4",
    "x-requested-with": "XMLHttpRequest"
}

x = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-encoding: gzip, deflate, br
accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
cache-control: max-age=0
cookie: pcid=eSMiVZcShv2; _ym_uid=1523384729655819281; __utma=43320484.1797769938.1523384729.1536525433.1536598817.11; _ga=GA1.2.1797769938.1523384729; _ym_d=1553608898; is_scrollmode=1; pkb_modern=11; _ym_isad=1; _gid=GA1.2.763531824.1561820052; ycm=2; autohide_news=0; nps7s=618804; ufp=101; rheftjdd=rheftjddVal; __utma=43320484.1797769938.1523384729.1536525433.1536598817.11; ufp=101; _ym_visorc_174977=w; _ym_visorc_56459=w; set_autohide_news=-1; ulfs=1561832886; PHPSESS=okqkfc18blcmshlh98f3cp2j61pa7ia6; _ym_uid=15618334081036135802; _ym_d=1561833408; _ga=GA1.2.464527830.1561833408; _gid=GA1.2.2119849258.1561833408; _ym_isad=2; vn=eJwzM7cwNDIyBQAF1gFw; fps=d05eeb13ea6aa22c712e60cb58fbdee2fd; ulfs=1561833430; ; la=1; _ym_visorc_174977=w; _ym_visorc_56459=w; bs=J0; _gat_gtag_UA_28292940_1=1; phpDug2=a%3A4%3A%7Bs%3A3%3A%22uid%22%3Bs%3A6%3A%22618359%22%3Bs%3A8%3A%22username%22%3Bs%3A11%3A%22dasgeschaft%22%3Bs%3A3%3A%22rem%22%3Bs%3A32%3A%220c8a820bb1f1aeaef6e4637811530e1d%22%3Bs%3A5%3A%22tries%22%3Bi%3A0%3B%7D
referer: https://pikabu.ru/@dasgeschaft
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'''

if __name__ == "__main__":
    x = x.split("\n")
    x = [y.split(": ", 1) for y in x]
    print("{")
    for i in x:
        print(f'    "{i[0]}": "{i[1]}",')
    print("}")