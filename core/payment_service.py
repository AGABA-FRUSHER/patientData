import base64
import json
import os
import requests
from dotenv import load_dotenv
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes as crypto_hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography import x509
from dotenv import load_dotenv
import xml.etree.ElementTree as ET

# Load env variables
load_dotenv('test.env')

# Constants
username = os.getenv('EAFYA')
password = os.getenv('EAFYAPWD')
ura_certificate_path = os.getenv('URA_CERTIFICATE_PATH', '/home/frusher/Desktop/patientRegistry/patientData/Registry/ura.cer')
private_key_path = os.getenv('PRIVATE_KEY_PATH', '/home/frusher/Desktop/patientRegistry/patientData/core/eafya.privkey.pem')
private_key_password = os.getenv('PRIVATE_KEY_PASSWORD', 'EAFYAPWD')

concatenated_credentials = f'{username}{password}'

def encryption(concatenated_creds, public_key_path='/home/frusher/Desktop/patientRegistry/patientData/core/eafya.pubkey.pem'):
    '''
    Function to encrypt concatenated (username + password) with URA public Key
    '''
    with open(public_key_path, 'rb') as cert_file:
        cert_data = cert_file.read()
        cert = x509.load_pem_x509_certificate(cert_data, default_backend())
        public_key = cert.public_key()
    
    encrypted = public_key.encrypt(
        concatenated_creds.encode('utf-8'),
        padding.PKCS1v15()
    )

    return base64.b64encode(encrypted)

def signature(encrypted, key_path, key_password):
    '''
    Function to sign encrypted data with MDA private key and private key password
    '''
    with open(key_path, 'rb') as private_key_file:
        try:
            # Attempt to load the private key with the provided password
            private_key = serialization.load_pem_private_key(
                private_key_file.read(),
                password=key_password.encode('utf-8'),
                backend=default_backend()
            )
        except ValueError:
            print("Error: Incorrect password or private key is not encrypted.")
            return None
    
    signed = private_key.sign(
        encrypted,
        padding.PKCS1v15(),
        crypto_hashes.SHA1()
    )

    signed_credentials = base64.b64encode(signed).decode('utf-8')

    return signed_credentials


def get_access_token():
    token_url = "https://helpdesk.health.go.ug/token"
    
    token_headers = {
        "Authorization": "Basic VmFOTVNYSjBZQ1VZOWg1cVJ0SFFoRG5JaVJvYTptUG41WUZ4VHBabFZEeFZIYzBkQXVTU2RxWVVh",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    token_data = {
        "grant_type": "client_credentials"
    }
    
    response = requests.post(token_url, headers=token_headers, data=token_data)
    print('='*10, response.text)
    
    if response.status_code == 200:
        token_response = response.json()
        return token_response['access_token']
    else:
        raise Exception(f"Failed to get access token: {response.status_code} {response.text}")


def send_request(encrypted_credentials, signed_credentials):
    '''
    Function to send the request with encrypted and signed credentials
    '''
    # endpoint_url = "https://testpayments.ura.go.ug/MDAService/PaymentServices.svc"
    endpoint_url = "https://helpdesk.health.go.ug/checkprn"
    # endpoint_url = "https://helpdesk.health.go.ug/getprn"

    payload = {
        "CheckPRNStatus": {
        "strPRN": "2240000798961",
        "concatenatedUsernamePasswordSignature": signed_credentials,
        "encryptedConcatenatedUsernamePassword": encrypted_credentials,
        "userName": "EAFYA"
        }
    }

    # payload = {
    #             "PRNRequest":{
    #             "AdditionalFees":"0",
    #             "Amount":"160000",
    #             "AssessmentDate":"2024-04-04T12:16:15.534",
    #             "BuildingName":None,
    #             "ContactNo":None,
    #             "County":None,
    #             "District":None,
    #             "Email":"franktest@health.go.ug",
    #             "ExpiryDays":"21",
    #             "ForeignCurrencyCode":None,
    #             "GrossAmount":"0",
    #             "LocalCouncil":None,
    #             "MobileNo":"256779825056",
    #             "NoOfForms":"1",
    #             "Parish":None,
    #             "PaymentBankCode":"DTB",
    #             "PaymentMode":"CASH",
    #             "PaymentType":"DT",
    #             "PlotNo":None,
    #             "ReferenceNo":"0001069329",
    #             "SRCSystem":"eCitie",
    #             "Street":None,
    #             "SubCounty":None,
    #             "TIN":"1000035867",
    #             "TaxHead":"KCCA524",
    #             "TaxPayerBankCode":"DTB",
    #             "TaxPayerName":"ALIFAT INVESTMENTS LTD",
    #             "TaxSubHead":None,
    #             "TraceCentre":None,
    #             "Village":None, 
    #             },
    #             "concatenatedUsernamePasswordSignature": signed_credentials,
    #             "encryptedConcatenatedUsernamePassword": encrypted_credentials,
    #             "userName": "EAFYA"
    #         }

    access_token = get_access_token()

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "scope": "default",
        "token_type": "Bearer",
        "Authorization": f"Bearer {access_token}"

    }

    payload_jsn_str = json.dumps(payload)    
    response = requests.post(endpoint_url, data=payload_jsn_str, headers=headers)
    

    print(response.status_code)
    print(response.text)
    # try:
    #     json_response = response.json()
    #     print(json_response)
    # except json.decoder.JSONDecodeError:
    #     # print("Non-JSON response:", response.text)
    #     root = ET.fromstring(response.text)

    #     # Find the PRN element in the XML structure
    #     prn_element = root.find('.//{http://schemas.datacontract.org/2004/07/URAPaymentGateway.DataContracts}PRN')

    #     if prn_element is not None:
    #         generated_prn = prn_element.text
    #         print("Generated PRN:", generated_prn)
    #     else:
    #         print("PRN not found in the response.")


if __name__ == "__main__":

    encrypted_data = encryption(concatenated_credentials, ura_certificate_path)
    encrypted_credentials = encrypted_data.decode('utf-8')
    print('\n------encryptedConcatenatedUsernamePassword-------\n' + encrypted_credentials + '\n------End Encryption-----\n')

    signed_credentials = signature(encrypted_data, private_key_path, private_key_password)
    print('\n------concatenatedUsernamePasswordSignature-------\n' + signed_credentials + '\n------End Signature-----\n')

    send_request(encrypted_credentials, signed_credentials)
