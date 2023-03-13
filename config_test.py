from tenable_jira.jira import Jira
from tenable_jira.config import base_config
from restfly.utils import dict_merge
import yaml, json

config_file = 'config_paypal.yaml'

config = dict_merge(
    base_config(),
    yaml.load(open(config_file), Loader=yaml.Loader)
)
jira = Jira(
    'https://{}/rest/api/3'.format(config['jira']['address']),
    config['jira']['api_username'],
    config['jira']['api_token']
)

print('Available Issue Types are:')

for a in jira.issue_types.list():
    print('{:>10}: {}'.format(a.get('id'), a.get('name')))