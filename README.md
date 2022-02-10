# MSP Vendors Vulnerability Disclosure Programs / Bug Bounty Programs

## Introduction
This serves as a general index of vendors in the MSP space who may or may not have published their Vulnerability Disclosure Program (VDP) and Bug Bounty Programs (BBP) publicly.

Vendors, MSPs or security researchers who wish to have a company included in the list can ping me at [dana@vulscan.com](mailto:dana@vulscan.com) with the information to be added/updated, or provide a pull request for me to approve. 

## Methodology
- Anyone who contacts me with links to a vendor offering products and services to MSPs may be included in the list.
- Every vendor added gets run though an assessment against [RFC8615](https://datatracker.ietf.org/doc/html/rfc8615) (see [https://securitytxt.org/](https://securitytxt.org/)) and DNS Security TXT (see [https://dnssecuritytxt.org/](https://dnssecuritytxt.org/)). This populates the corresponding columns.
- All vendors are then automatically checked against webcrawl data for terms including "Vulnerability Disclosure Program", "VDP", "disclosure", "bug bounty" and "BBP". Any results will be reviewed by a human, and corresponding links added if VDP / BBP data is found.
- Some vendors who I have relationships with may be contacted over LinkedIn or by email.
- Anyone who submits a Git pull request will be manually reviewed for accuracy and then considered approval. All reasonable requests will be accepted as long as the vendor clearly offers services to MSPs.

## Vendors
| Company  | VDP | BBP | Safe Harbor? | security.txt | DNS security TXT |
| --- | :-: | :-: | :-: | :-: | :-: |
| [Acronis](https://www.acronis.com/)  | [Yes](https://hackerone.com/acronis/)  | [Yes](https://hackerone.com/acronis/) | Yes | [Yes](https://www.acronis.com/.well-known/security.txt) | No |
| [Addigy](https://addigy.com/)  | [Yes](https://addigy.com/responsible-disclosure/) | No | No | No | No |
| [Appgate](https://www.appgate.com/)  | No | No | No | No | No |
| [Atera](https://www.atera.com/)  | No | No | No | No | No |
| [Auvik](https://www.auvik.com/)  | [Yes](https://hackerone.com/auvik) | No | Yes  | No | No |
| [Axcient](https://axcient.com/)  | No | No | No | No | No |
| [Barracuda](https://www.barracuda.com/)  | [Yes](https://bugcrowd.com/barracuda) | Yes | Partial | No | No |
| [Bitdefender](https://www.bitdefender.com/)  | [Yes](https://www.bitdefender.com/bitdefender_vulnerability_disclosure_program.html) | [Yes](https://www.bitdefender.com/site/view/bug-bounty.html) | No | No | No |
| [BitTitan](https://www.bittitan.com/) | No | No | No | No | No |
| [Blumira](https://www.blumira.com/) | No | No | No | No | No |
| [ConnectWise](https://www.connectwise.com/)  | [Yes](https://hackerone.com/connectwise-h1r) | No | Yes | No | No |
| [Datto](https://www.datto.com/)  | [Yes](https://www.datto.com/legal/vulnerability-disclosure-program) | No | Yes | [Yes](https://www.datto.com/.well-known/security.txt) | No |
| [Egnyte](https://www.egnyte.com/)  | No | No | No | No | No |
| [Fortinet](https://www.fortinet.com/)  | [Yes](https://www.fortiguard.com/psirt_policy) | No | Yes | [Yes](https://www.fortinet.com/.well-known/security.txt) | No |
| [Gradient MSP](https://www.meetgradient.com/)  | No | No | No | No | No |
| [Huntress](https://www.huntress.com/) | No | No | No | No | No |
| [Kaseya](https://www.kaseya.com/) | [Yes](https://www.kaseya.com/legal/vulnerability-disclosure-policy/) | No | Yes | No | No |
| [Liongard](https://www.liongard.com/)  | No | No | No | No | No |
| [GoTo](https://www.goto.com) (formally LogMeIn)  | No | No | No | No | No |
| [Malwarebytes](https://www.malwarebytes.com/) | [Yes](https://www.malwarebytes.com/secure/guidelines) | [Yes](https://www.malwarebytes.com/secure) | No | No | No |
| [N-Able](https://www.n-able.com/) | No | No | No | No | No |
| [Naverisk](https://naverisk.com/)  | No | No | No | No | No |
| [NinjaOne](https://www.ninjaone.com/) | No | [Yes](https://www.ninjaone.com/bug-bounty/) | No | [Yes](https://www.ninjarmm.com/.well-known/security.txt) | No |
| [nerdio](https://getnerdio.com/) | No | No | No | No | No |
| [OITVOIP](https://oit.co/) | No | No | No | No | No |
| [ServiceNow](https://www.servicenow.com/) | [Yes](https://www.servicenow.com/company/trust/responsible-disclosure.html) | No | No | [Yes](https://www.servicenow.com/.well-known/security.txt) | No |
| [Servosity](https://www.servosity.com/) |  |  |  |  |  |
| [SolarWinds](https://www.solarwinds.com/)  | [Yes](https://www.solarwinds.com/information-security/vulnerability-disclosure-policy) | No | No | [Yes](https://www.solarwinds.com/.well-known/security.txt) | No |
| [Sonicwall](https://www.sonicwall.com/)  |  |  |  |  |  |
| [Sophos](https://www.sophos.com/)  |  |  |  |  |  |
| [Taylor Business Group](https://www.taylorbusinessgroup.com/)  |  |  |  |  |  |
| [ThreatLocker](https://www.threatlocker.com/)  |  |  |  |  |  |
| [TrendMicro](https://www.trendmicro.com/)  |  |  |  |  |  |
| [WebRoot](https://www.webroot.com/)  |  |  |  |  |  |
| [Watchguard](https://www.watchguard.com/)  |  |  |  |  |  |
| [Xero](https://www.xero.com/ca/)  |  |  |  |  |  |
|  |  |  |  |  |  |

## Research Notes
- Any bug bounty programs that are currently private, even if I know of them, will still be marked as "No". Any vendor that wishes to update that to a Yes simply has to provide me with a link to a landing page which offers security researchers a way to apply to the private program.
- Checks against security.txt and DNS Security TXT is done with the python script included in this repo. If a vendor has a non-standard configuration, please contact me with the appropriate URL/DNS record info and it will be updated in the script to validate. (But why aren't you following the standards?)

## Q&A
### I'm not a vendor, why am I on this list?
If you are offering services to other MSPs, and have a web application/portal that you are asking MSPs to log into, then you are responsible for application security (appsec) of that app. That means you are a potential target in the supply chain, and should be thinking about how adversaries may leverage your digital assets to attack MSPs, and ultimately their customers. So where is _YOUR_ VDP? Need help determining if you need one? [I can help](https://learn.vulscan.com/one-on-one-coaching).

### I'm a startup providing software to MSPs, why am I on this list?
Some MSP felt they wanted to know if you have a VDP and asked me to check. It might very well be that your appsec maturity model isn't at the point you are ready for a VDP. You should be honest with your customers about that. Otherwise, if it's very new to you and you need help, [contact me](https://learn.vulscan.com/one-on-one-coaching).

### Your assessment of my company is wrong
Could be. I'd be happy to update the index with proper data. 
