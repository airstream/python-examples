import requests
r = requests.get('https://salt.domain.com/api/v2/hosts', auth=('user', 'password'), verify='/etc/puppetlabs/puppet/ssl/certs/ca.pem')
print("Status code:", r.status_code)
response_dict = r.json()
print(response_dict.keys())

repo_dicts = response_dict['results']
for repo_dict in repo_dicts:
        ap = repo_dict['name']
        print("Hostname: " + str(repo_dict['name']))

        status = requests.get('https://salt.domain.com/api/v2/hosts/{}/status'.format(ap),
                                auth=('user', 'password'),
                                verify='/etc/puppetlabs/puppet/ssl/certs/ca.pem')
        response_dict_status = status.json()
        print(response_dict_status['status'])


repo_dicts = response_dict['results']
for repo_dict in repo_dicts:
        ap = repo_dict['name']
        print("Hostname: " + str(repo_dict['name']))

        status = requests.get('https://salt.domain.com/api/v2/hosts/',
                                auth=('user', 'password'),
                                verify='/etc/puppetlabs/puppet/ssl/certs/ca.pem')
        response_dict_status = status.json()
        print(response_dict_status.keys())


opsys = response_dict['results']
for opsys in repo_dicts:
        if "Windows" in str(repo_dict['operatingsystem_name']) or "MacOS" in str(repo_dict['operatingsystem_name']):
          print("WINDOWS / MAC")
        else:
          print("LINUX")
          print("Hostname " + str(repo_dict['name']) + " OS: " + str(repo_dict['operatingsystem_name']))

# STATUS OF HOST
# OK / ERROR
status_dicts = response_dict['results']
for status_dict in status_dicts:
        ap = repo_dict['name']
        print("Hostname: " + str(status_dict['name']))

        if "OK" in str(status_dict['global_status_label']):
          print("OK")
        else:
          print("ERROR")
          # ZABBIX_SEND_ERROR
		  
		  
### OUTPUT ###
# python3 salt-api.py
# Status code: 200
# dict_keys(['per_page', 'subtotal', 'search', 'total', 'sort', 'page', 'results'])
# Hostname: salt.domain.com
# Error
# Hostname: hostname1.domain.com
# No reports
# Hostname: salt.domain.com
# dict_keys(['per_page', 'subtotal', 'search', 'total', 'sort', 'page', 'results'])
# Hostname: hostname2.ci.kit
# dict_keys(['per_page', 'subtotal', 'search', 'total', 'sort', 'page', 'results'])
# LINUX
# Hostname vassilm-test.ci.kit OS: Ubuntu 16.04.3 LTS
# LINUX
# Hostname vassilm-test.ci.kit OS: Ubuntu 16.04.3 LTS
# Hostname: hostname2.ci.kit
# ERROR
# Hostname: hostname2.ci.kit
# ERROR