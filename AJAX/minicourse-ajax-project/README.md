How can I get a list of all my APIlimits?
$ curl --head https://api.nytimes.com/svc/books/v3/lists/overview.json?api-key=??? | grep -i "X-RateLimit"

How do I use the Times APIs?

Our APIs use a RESTful style and a resource-oriented architecture. Calls are made via HTTP requests (at a minimum, the GET method will be available; specific APIs may implement other methods). Your request URIs should be patterned after the examples in the API documentation, and you should always include your API key in a query string. See the documentation for each API for more details on request parameters and URI structure.
