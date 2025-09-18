import urllib.request
import re
import sys

if len(sys.argv) < 2:
    print("Usage: python3 extract_emails.py <url>")
    sys.exit(1)

tarurl = sys.argv[1]


try:
    with urllib.request.urlopen(tarurl) as response:
        html = response.read().decode('utf-8', errors='ignore')
except Exception as e:
    print("Error fetching URL:", e)
    sys.exit(1)

regex = re.compile(
    r"([a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*(@|\sat\s)"
    r"(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(?:\.|\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)",
    re.IGNORECASE
)

emails = re.findall(regex, html)

print("<MaltegoMessage>")
print("  <MaltegoTransformResponseMessage>")
print("    <Entities>")

for email in emails:
    print("      <Entity Type=\"maltego.EmailAddress\">")
    print("        <Value>{}</Value>".format(email[0]))
    print("      </Entity>")

print("    </Entities>")
print("  </MaltegoTransformResponseMessage>")
print("</MaltegoMessage>")
