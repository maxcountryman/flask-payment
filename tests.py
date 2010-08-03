# -*- coding: utf-8 -*-

from __future__ import with_statement

import unittest

from flask import Flask, g
from flaskext.payments import Payments, Transaction, Authorisation, PaymentValidationError

class TestCase(unittest.TestCase):

    TESTING = True
   
    # Perhaps make a PaypalTestCase later
    PAYPAL_API_ENDPOINT = ''
    PAYPAL_URL = ''
    PAYPAL_API_USER = '' # Edit this to your API user name
    PAYPAL_API_PWD = ''# Edit this to your API password
    PAYPAL_API_SIGNATURE = '' # Edit this to your API signature
    PAYPAL_API_VERSION = '53.0' 

    def setUp(self):

        self.app = Flask(__name__)
        self.app.config.from_object(self)
        
        self.payments = Payments(self.app)

        self.ctx = self.app.test_request_context()
        self.ctx.push()

    def tearDown(self):

        self.ctx.pop()

def getValidTransaction():
    trans = Transaction({
        'amt': '9.95',
        'inv': 'inv',
        'custom': 'custom',
        'next': 'http://www.example.com/next/',
        'returnurl': 'http://www.example.com/pay/',
        'cancelurl': 'http://www.example.com/cancel/',
        'firstname': 'Brave',
        'lastname': 'Star',
        'street': '1 Main St',
        'city': u'San Jose',
        'state': 'CA',
        'countrycode': 'US',
        'zip': '95131',
        'expdate': '012019',
        'cvv2': '037',
        'acct': '4797503429879309',
        'creditcardtype': 'visa',
        'ipaddress': '10.0.1.199',
        })
    return trans

class TestTransaction(TestCase):

    def test_initialize(self):
        trans = getValidTransaction() 

        #assert trans.sender == "support@mysite.com"
        #assert msg.recipients == ["to@example.com"]


class TestAuthorisation(TestCase):

    pass

class TestPayments(TestCase):

    def test_process(self):

        # probably need a test object factory
        trans = getValidTransaction()

        authorisation = self.payments.process(trans)

        assert authorisation.status 

class TestConnection(TestCase):
    """ testing of some lower level stuff? """

    pass
