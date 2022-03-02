import requests, json
import subprocess
get_ip_url = "https://ipv6.icanhazip.com"
sub_domain = "api.anukul.com.np"
email = "beinganukul@gmail.com"
auth_key = "<from dash.cloudflare.com>"
content_type = "application/json"
zone = "<from dash.cloudflare.com"
record_type = "AAAA"

headers_ = {
        "X-Auth-Email" : email,
        "X-Auth-Key" : auth_key,
        "Content-Type" : content_type
}

def get_new_ip():
    return_value = subprocess.getoutput('/home/anukul/project/github-ddns-cf/ipaddr.sh')
    print(return_value)
    return return_value

#def compare_with_cloudflare()

def fetch_old_address_cf():
    recieved_response = requests.get("https://api.cloudflare.com/client/v4/zones/"+ zone +
    "/dns_records?type="+ record_type + "&name="+ sub_domain, headers = headers_).text
    old_cf_ip_addr = json.loads(recieved_response)['result'][0]['content']
    identifier = json.loads(recieved_response)['result'][0]['id']
    return old_cf_ip_addr, identifier

def post_ip_change_req(old_ip, new_ip, identify):
    payload = {
            "type":record_type,
            "name":sub_domain,
            "content":new_ip,
            "ttl":1,
            "priority":10,
            "proxied":False
        }

    put_payload = json.dumps(payload, ensure_ascii = False)
    print(put_payload)
    send_request = requests.put("https://api.cloudflare.com/client/v4/zones/"+ zone +
            "/dns_records/"+ identify, headers = headers_, data = put_payload)
    send_request = json.loads(send_request)
    print(send_request.txt)
    print(send_request)
def main():
    old_ip, identify = fetch_old_address_cf()
    new_ip = get_new_ip()
    if old_ip != new_ip:
       post_ip_change_req(old_ip, new_ip, identify)
    else:
        print("The addresses are not changed yet!!")

if __name__ == "__main__":
    main()
