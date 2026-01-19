import requests

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

headers = {
    "Content-Type": "application/soap+xml; charset=utf-8"
}

soap_body = """
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Body>
    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>IN</sCountryISOCode>
    </CountryCurrency>
  </soap:Body>
</soap:Envelope>
"""

response = requests.post(url, data=soap_body, headers=headers)

print("Status Code:", response.text)
# print("Response Body:")
# print(response.text)
#
# import xml.etree.ElementTree as ET
#
# root = ET.fromstring(response.text)
#
# namespaces = {
#     "soap12": "http://www.w3.org/2003/05/soap-envelope",
#     "ns": "https://www.w3schools.com/xml/"
# }
#
# c_to_f = root.find(".//ns:CelsiusToFahrenheitResult", namespaces)
# print("c_to_f:", c_to_f.text)