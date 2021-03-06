#
# This file is generated by jsonrpcstub, DO NOT CHANGE IT MANUALLY!
#

#
# To use this client, jsonrpc_pyclient must be installed:
# pip install jsonrpc_pyclient
#

from jsonrpc_pyclient import client

class jsonrpc_example_client(client.Client):
    def __init__(self, connector, version='2.0'):
        super(jsonrpc_example_client, self).__init__(connector, version)

    def myclass_add(self, a, b):
        parameters = {}
        parameters['a'] = a
        parameters['b'] = b

        result = self.call_method('myclass_add', parameters)
        return result

    def myclass_echo(self, message):
        parameters = {}
        parameters['message'] = message

        result = self.call_method('myclass_echo', parameters)
        return result

    def myclass_get_val(self):
        parameters = None

        result = self.call_method('myclass_get_val', parameters)
        return result

    def myclass_mult(self, a, b):
        parameters = {}
        parameters['a'] = a
        parameters['b'] = b

        result = self.call_method('myclass_mult', parameters)
        return result

    def myclass_set_val(self, value):
        parameters = {}
        parameters['value'] = value

        result = self.call_method('myclass_set_val', parameters)
        return result

    def mytftp_get_ip(self):
        parameters = None

        result = self.call_method('mytftp_get_ip', parameters)
        return result

    def mytftp_set_ip(self, ip):
        parameters = {}
        parameters['ip'] = ip

        result = self.call_method('mytftp_set_ip', parameters)
        return result

    def myaes_config(self, iv, key):
        parameters = {}
        parameters['iv'] = iv
        parameters['key'] = key

        result = self.call_method('myaes_config', parameters)
        return result

    def myaes_encrypt(self, source, target):
        parameters = {}
        parameters['source'] = source
        parameters['target'] = target

        result = self.call_method('myaes_encrypt', parameters)
        return result


