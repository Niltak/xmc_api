import requests
import xmltodict
from getpass import getpass


class Connection(object):
    def __init__(
        self,
        hostname,
        user,
        pwd=None) -> None:
        '''
        Starts a connection to the XMC server.
        '''
        if not pwd:
            pwd = getpass()
        self.url = f'https://{hostname}:8443/nbi/graphql'
        self.user = user
        self.pwd = pwd

    def requesting(self, query) -> requests:
        '''
        Submits get request to the XMC server.
        Returns response.
        '''
        get_query = {
            'query': query
        }
        return requests.get(self.url, auth=(self.user, self.pwd), params=get_query)


    def requesting_dict(self, query) -> dict:
        '''
        Converts requested response to a dictionary for easier manipulation.
        Returns a filtered response
        '''
        reponse = self.requesting(query)
        return reponse.json()['data']['network']


    def switch_list_create(self, site_code) -> dict:
        '''
        '''
        query = 'query{ network{ devices{ ip nickName nosIdName}}}'
        switch_list = self.requesting_dict(query)['devices']

        non_switch_list = []
        for switch in switch_list[:]:
            if switch['nosIdName'] == 'Ubuntu':
                non_switch_list.append(switch)
                switch_list.remove(switch)
                continue
            switch['hostname'] = switch['nickName']
            switch['host'] = switch['ip']
            switch['groups'] = ['EXAMPLE_PCS_BUSINESS', site_code]
            switch['neighbor'] = []
            switch['data'] = {}
            switch['data']['location'] = 'EXAMPLE_DEPARTMENT'
            switch['data']['role'] = 'EXAMPLE_CSW_DSW_ASW'
            switch['data']['device_type'] = ''
            del switch['ip']
            del switch['nickName']
            del switch['nosIdName']

        return switch_list