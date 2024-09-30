from pprint import pprint
from portalsdk import APIContext, APIMethodType, APIRequest
import random
import string


def randomid (size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def main(msisdn, amount):
    tranfcode = randomid()
    refcode = randomid()
    api_context = APIContext()
    api_context.api_key = 'api-key'
    api_context.public_key ='public-key' 
    api_context.ssl = True
    api_context.method_type = APIMethodType.POST
    #api_context.address = 'api.sandbox.vm.co.mz'# Area the teste
    api_context.address = 'api.vm.co.mz'
    api_context.port = 18352
    api_context.path = '/ipg/v1x/c2bPayment/singleStage/'

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_TransactionReference', str(tranfcode))
    api_context.add_parameter('input_CustomerMSISDN', str(msisdn))
    api_context.add_parameter('input_Amount',str(amount))
    api_context.add_parameter('input_ThirdPartyReference', str(refcode))
    api_context.add_parameter('input_ServiceProviderCode','short-code') # Short code Ex: 910845

    api_request = APIRequest(api_context)
    result = api_request.execute()

    pprint(result.status_code)
    pprint(result.headers)
    pprint(result.body)

    return result.status_code