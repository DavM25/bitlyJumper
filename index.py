import requests; from time import sleep

def main():
    url = str( input('[-] Enter a valid URL: ') )

    if  url.lower().find('bitly/') == -1 and url.lower().find('bit.ly/') == -1 and url.lower().find("bitly\ ".strip()) == -1 and url.lower().find('bit.ly\ '.strip()) == -1 :
        print('[!] This is not a Bitly URL...')
    else:
        if not url.startswith("https://") and not url.startswith("http://"):
            url = "http://" + url

        if url.startswith("http://"):
            print("\n[!] HTTP is not supported by BitLy. \n[+] Converting the URL to HTTPS...")
            url = url[7:]; url = "https://" + url

        url += "+"
        print('\n[+] Making the request to ' + url)

        try: 
            res = requests.get(url)
            print("[+] Request done! \n[+] Obtaining the real URL...")
        except:
            exit("[!] An error has ocurred during the request... ")

        realurl = res.text.rsplit(f'"long_url": "')[1].rsplit('"')[0]

        if realurl.startswith('http'):
            sleep(1)
            exit("[+] The real URL is: " + realurl)
        else:
            print('[!] An error has ocurred while trying to get the real URL...')

if __name__ == "__main__":
    main()
