# Some Salesforce Utilities

Utilities for generating CSV files from Salesforce metadata.

```
from code.core import SalesforceMetadataGenerator

smg = SalesforceMetadataGenerator('mysfdc@credentials.com', 'mypassword', 'mysecuritytoken')

smg.make_csv('Lead')
smg.make_csv('Contact')
smg.make_csv('Account')
```
