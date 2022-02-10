# MSP Vendors Vulnerability DIsclosure Programs / Bug Bounty Programs

This serves as a general index of vendors in the MSP space who may or may not have published their Vulnerability Disclosure Program (VDP) and Bug Bounty Programs (BBP) publicly.

Vendors, MSPs or security researchers who wish to have a company included in the list can ping me at [dana@vulscan.com](mailto:dana@vulscan.com) with the information to be added/updated, or provide a pull request for me to approve. 

## Vendors
| Company  | VDP | BPP | Safe Harbor? | security.txt | DNS security TXT |
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
| [Huntress](https://www.huntress.com/)  |  |  |  |  |  |
| [Kaseya](https://www.kaseya.com/)  |  |  |  |  |  |
| [Liongard](https://www.liongard.com/)  |  |  |  |  |  |
| [GoTo](https://www.goto.com) (formally LogMeIn)  |  |  |  |  |  |
| [Malwarebytes](https://www.malwarebytes.com/)  |  |  |  |  |  |
| [N-Able](https://www.n-able.com/)  |  |  |  |  |  |
| [Naverisk](https://naverisk.com/)  |  |  |  |  |  |
| [NinjaOne](https://www.ninjaone.com/)  |  |  |  |  |  |
| [nerdio](https://getnerdio.com/)  |  |  |  |  |  |
| [OITVOIP](https://oit.co/)  |  |  |  |  |  |
| [ServiceNow](https://www.servicenow.com/)  | [Yes](https://www.servicenow.com/company/trust/responsible-disclosure.html) | No | No | [Yes](https://www.servicenow.com/.well-known/security.txt) | No |
| [Servosity](https://www.servosity.com/)  |  |  |  |  |  |
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
