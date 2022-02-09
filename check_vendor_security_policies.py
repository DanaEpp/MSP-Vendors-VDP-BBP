#!/usr/bin/env python3

""" 
    Checks if a vendor is properly following security.txt and DNS Security TXT standards 
    and publishing their security contact and policy information

    See https://securitytxt.org/ and https://dnssecuritytxt.org for more information

    Author: Dana Epp (SilverStr)
"""

import sys
import requests
import dns.resolver

security_txt_uri = ".well-known/security.txt"
dns_security_prefix = "_security"

dns_security_txt = [ 
        'security_contact',
        '"security_contact',
        'security_policy',
        '"security_policy'
]


class VendorSecurityInfo:
    def __init__( self, domain ):
        self.domain = domain
        self.web_security_txt = False
        self.dns_security_txt = False

def load_vendors(filename):
    # Load up vendor list
    vendors = []
    
    try:
        with open( filename, "r") as f:
            for domain in f:
                vendors.append(VendorSecurityInfo(domain.strip()))
    except:
        print( f"Unable to find {filename}. Aborting" )
        sys.exit()

    return vendors

def fetch_url(url):
    exists = False

    try:
        response = requests.get(url)
        if( response.status_code == 200 ):
            # Need to check for at least the "Contact" field, in case
            # the resulting file is a redirect or something
            if "Contact: " in str(response.content):
                exists = True
    except Exception as ex:
        print( f"Unable to reach {url}. Err: {ex}" ) 

    return exists

def security_txt_exists(domain):

    url  = f"https://{domain}/{security_txt_uri}"
    url2 = f"https://www.{domain}/{security_txt_uri}"
    
    # First check at the root of the domain
    if fetch_url(url) or fetch_url(url2):
        exists = True
    else:
        exists = False
        
    return exists

def resolve( resolver, domain ):
    exists = False

    try:
        answers = resolver.query( domain, "TXT" )
        for record in answers:
            if record.to_text().startswith(tuple(dns_security_txt)):
                exists = True
    except dns.resolver.NoAnswer:
        # Gobble up if know TXT records exist
        pass
    except dns.resolver.NXDOMAIN:
        # Gobble up if the domain doesn't exist (ie: _security.domain.com)
        pass
    except Exception as ex:
        print( f"Unable to resolve {domain}. Err: {ex}" )

    return exists

def dns_security_txt_exists(domain):
    resolver = dns.resolver.Resolver()
    resolver.timeout = resolver.lifetime = 5
    resolver.nameservers = ['1.1.1.1', '8.8.8.8']

    if resolve(resolver, domain ) or resolve(resolver, dns_security_prefix+"."+domain) :
        exists = True
    else:
        exists = False

    return exists

vendors = load_vendors("vendors.txt")

for vendor in vendors:
    # First check for security.txt
    if security_txt_exists(vendor.domain):
        print( f"security.txt: {vendor.domain}")

    # Now check for DNS Security TXT
    if dns_security_txt_exists(vendor.domain):
        print( f"DNS Security TXT: {vendor.domain}")
