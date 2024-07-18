Write a Django application that doesn’t expose any endpoints. It does data processing on a periodic, scheduled basis.
The frequency of runs should be configurable.
You will need to connect to an external API to download resources.
Use this basic resource to understand the structure of the REST API framework to connect to.
https://api.b2broker.com/docs/api/back-office/v2/index.html#/
This is the endpoint that you will be working with specifically:
https://api.b2broker.com/docs/api/back-office/v2/index.html#/operations/getClientCollection
1- “The Fetch”:
a. Exposing and using the above resources, get a bearer_token that you can use the to query the above endpoint. (If you feel confident add the refresh token logic also). This will mean having to go to Auth endpoints.
b. Get a list of all clients (Use fromUpdateTime and toUpdateTime filters if necessary. No other filters so all clients are fetched!).
c. Leverage Django ORM to save the clients into a database (the database for now should be sqlite, but it should be easy to switch to any other). Create the necessary db schemas so that all fields can be saved
2- Run the above “Fetch” at time intervals specified in the configuration.
Preferences (lack of observing these preferences will not disqualify you, yet, adherence will gain you extra points): use poetry, follow PEP and use typehings.