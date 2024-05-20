import requests
import argparse
from time import sleep
from urllib.parse import urlparse

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list",help="List of URLs", required=True)
    # to be implemented
    parser.add_argument("-r", "--rate",help="rate request/second", required=False)
    parser.add_argument("-H", "--header",help="add request header", required=False)
    parser.add_argument("-o", "--output",help="results output", required=False)
    #////////////
    args = parser.parse_args()
    url =args.list
    with open(args.list) as f:
        for line in f: 
            line = line.strip() 
            try:
                print(OKCYAN+"[+] Checking "+line+ENDC)
                request=requests.get(line,headers={'Origin':'http://'+urlparse(line).netloc+'.example.com'})
                if(request.headers.get('Access-Control-Allow-Origin')):
                    if('example.com' in request.headers['Access-Control-Allow-Origin'] or "*" in request.headers['Access-Control-Allow-Origin']):
                        print(OKGREEN+"[+] Might be vulnerable to CORS misconfiguration "+line+ENDC + " "+OKCYAN+"[+] Access-Control-Allow-Origin: "+request.headers['Access-Control-Allow-Origin']+ENDC)
                    else:
                        print(FAIL+"[-] Not vulnerable to CORS misconfiguration "+line+ENDC + " "+FAIL+"[-] Access-Control-Allow-Origin: "+request.headers['Access-Control-Allow-Origin']+ENDC)
                else:
                        print(FAIL+"[-] Using default CORS "+line+ENDC + " "+FAIL)
            except:
                print(FAIL+"connection Error"+ENDC)
                pass    