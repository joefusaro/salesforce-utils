import csv
from simple_salesforce import Salesforce


class SalesforceUtility(object):

    def __init__(self, username, password, security_token):
        self.username = username
        self.password = password
        self.security_token = security_token
        self.connection = self.connect()

    def connect(self):
        return Salesforce(
            username=self.username,
            password=self.password,
            security_token=self.security_token
            )

class SalesforceMetadataGenerator(SalesforceUtility):

    def make_csv(self, table_name):
        path = "../" + table_name + ".csv"
        operator = getattr(self.connection, table_name)
        metadata = operator.describe()
        fields = metadata["fields"]

        fieldnames = fields[0].keys()

        with open(path, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in fields:
                _dict = {}
                for k,v in row.iteritems():
                    _dict[k] = v
                writer.writerow(_dict)
