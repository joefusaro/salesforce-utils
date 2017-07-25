# Some Salesforce Utilities


## SalesforceMetadataGenerator

Simple way of generating a CSV file containing Salesforce metadata for a table.

```
from code.core import SalesforceMetadataGenerator

smg = SalesforceMetadataGenerator('mysfdc@credentials.com', 'mypassword', 'mysecuritytoken')

smg.make_csv('Lead')
smg.make_csv('Contact')
smg.make_csv('Account')
```
