# APIster - Introduction
This python program (currently being developed) will be utilized to "scrape" a website or IP Address to determine what API endpoints exists and what information can be obtained from the API endpoint. This is a very simple tool that will test all open ports for an open API endpoint, assuming that the API endpoint uses "API" in the url. 

<br />
<br />



<div align='center'>

![APIster](https://github.com/initcyber/APIster/blob/main/logo.png)

<a href='https://github.com/initcyber/APIster/releases'>
  
<img src='https://img.shields.io/github/v/release/initcyber/APIster?color=%23FDD835&label=version&style=for-the-badge'>
  
</a>
  
<a href='https://github.com/initcyber/APIster/blob/main/LICENSE'>
  
<img src='https://img.shields.io/github/license/initcyber/APIster?style=for-the-badge'>

</a>

<a href="https://github.com/initcyber/APIster/pulls">

<img src="https://img.shields.io/badge/PRs-welcome-red?style=for-the-badge">

</a>
  

  
</div>

<br />

---

### The APIster script is available for testing! 🥳 🚀

In order to use the APIster:
- clone this repository
- install dependencies (Ubuntu)
  - sudo apt install chromium-chromedriver
- Install requirements.txt (pip install -r requirements.txt)
- I may be missing some requirements/dependencies for this github repository... If you see anything please open an [issue](https://github.com/initcyber/APIster/issues) on github

This has been tested using Ubuntu 22.04/WSL2. I have not tested this using any other linux platforms.
---

<br />

<div align="center">

# Table of Contents

[BUILT WITH](https://github.com/initcyber/APIster#-built-with) • 
[CONTRIBUTING](https://github.com/initcyber/APIster#%EF%B8%8F-contributing) • 
[SPREAD THE WORD](https://github.com/initcyber/APIster#-spread-the-word) • 
[DISCLAIMER](https://github.com/initcyber/APIster#-disclaimer) •
[Notes/To-Do](https://github.com/initcyber/APIster#-notes)
[LICENSE](https://github.com/initcyber/APIster#%EF%B8%8F-license)
[Change Log](https://github.com/initcyber/APIster#-changelog)**

</div>

<br />


# 👨‍💻 built with
(Whats in this?)

Here's a brief high-level overview of what this app is built with:

- This project uses Python, and in the future may use Django. 
- This project relies on the Selenium Webdriver python library 

# ✍️ Contributing

Interested in contributing to this project? Any help is greatly appreciated.

If you have a contribution in mind, please check out our [Contribution Guide](https://github.com/initcyber/APIster/wiki/Contribution-Guide) for information on how to do so. Also, make sure you read our [Code of Conduct](https://github.com/initcyber/APIster/wiki/Code-of-Conduct) to foster an encouraging sense of community.

# ⚠️ License

This app (APIster) is free and open-source software licensed under the GNU General Public License v3.0.

<br />

## Notes/To-Do
In order for this project to function better (pentesting purposes so to speak, with PERMISSION obviously), it would probably be best to incorporate a proxy (mitmproxy?) in order to "mask" your IP Address so it doesn't get blocked by any sort of IDS/IPS which may be implemented.

- Incorporate a proxy
- (Possibly) find a common list of "API" endpoints (such as "http://yourdomain.com/xyz" where "xyz" is another common API endpoint)
- Refactor Code
- Implement a web front end (Django)
- Dockerize
- Export list obtained from port_scanner.py and api_scanner.py into a csv for further investigation.

---

<br />

## DISCLAIMER:

This software is provided 'as is', without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

This tool is intended to be used for legal purposes only, and the user assumes all responsibility for its use. You must ensure that your use of this tool complies with all local, state, and federal laws and regulations. Any use of this tool for unauthorized activities is strictly prohibited.

---

<br />

## Changelog

January 2024 - Initial release (0.1), changed name from API_Fuzzz to APIster.
