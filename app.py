from requests import get
import socket

def run():
    dns_ip = get_current_default_ip_for_domain('chinrubber.com')
    ip = get_current_ip()

    print('DNS IP is %s' % dns_ip)
    print('PUB IP is %s' % ip)
    
def get_current_default_ip_for_domain(domain):
    return socket.gethostbyname(domain)

def get_current_ip():
    return get('https://api.ipify.org').text

if __name__ == "__main__":
    run()