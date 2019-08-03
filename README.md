
# CredAPI
## An API Authentication Library
---

### Description: 

This goal of this library is to simplify api authenticaion and to create a universal wrapper for popular APIs.

### Usage:
Create a mycredentials.py file and make sure to add that to the .gitignore. In this file enter all required credentials. For example:
```
reddit_cred = credential(name="Reddit", username="", password="", client_id="", client_secret="", user_agent="")
```

This library can be used as a submodule. The following commands must be run in the desired repo:
```
git submodule add git@github.com:ybharatu/CredAPI.git
git submodule update --init --recursive
```

### Functions:
    - get_cred_dict: Returns required credentials in dictionary form


### Supported APIs:
    - Reddit

### Dependencies:
    - unittest
    - praw
