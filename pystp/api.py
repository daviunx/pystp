import os
import pycurl

class API(object):
	""" SolidTrustPay API """

	def __init__(self,merchant_account,sci_name,
			subscription,iten_id,amount,currency = "USD",
			logo=None,notify_url=None,confirm_url=None,
			return_url=None,return_method=None,
			cancel_url=None,testmode="OFF",extra_params=None):

		self.merchant_account = merchant_account
