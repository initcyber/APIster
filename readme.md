# API_Fuzzz
This python program (currently being developed) will be utilized to "scrape" a website to determine what API endpoints exists and what information can be obtained
from the API endpoint.

## Notes/To-Do
(Somehow) integrate developer mode from Mozilla or Chrome to intercept HTTP Requests
Then hit the endpoint API with requests() module and see what we get

Use a proxy of sorts? mitmproxy.org?


Ports - use scanner.py to scan through the ports of a website... then integrate with selenium-fuzz.py in order to scan a website, against those open ports, to figure out what api's exist.

or

Try common ports in a list?

1/17/24 - Close: 
Able to import port_scanner.py, cant integratee into api_scanner.py. api_scanner_bk.py works as intended.
