import requests
import sys

import pprint
pp = pprint.PrettyPrinter()

subdomain_list = open('subdomains.txt').read()
subs = subdomain_list.splitlines()

#pp.pprint(subs)

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_to_check, timeout=1)
    except requests.ConnectionError:
        pass
    except requests.ReadTimeout:
        pass
    else:
        print("Valid domain ", url_to_check)