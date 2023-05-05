import string
import re

def is_valid_email_address(email):
    email = email.lower()
    parts = email.split('@')
    if len(parts) != 2:
      # Not exactly one at-sign
      return False
    
    allowed = set(string.ascii_lowercase + string.digits + '.-_+')
    for part in parts:
        if not set(part) <= allowed:
          # Characters other than the allowed ones are found
          return False

    # Must contain a top level domain (tld)
    tldsRegex = '/[.com]|[.co.uk]|[.org]/'
    if re.search(tldsRegex, parts[1]) == None:
       return False
    return True
