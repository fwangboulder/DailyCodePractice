1.  Open index.html

2. Type the address.

3. You will see a background image, the New York Time News and Wikipedia links.

How can I get a list of all my APIlimits?
$ curl --head https://api.nytimes.com/svc/books/v3/lists/overview.json?api-key=??? | grep -i "X-RateLimit"

How do I use the Times APIs?

Our APIs use a RESTful style and a resource-oriented architecture. Calls are made via HTTP requests (at a minimum, the GET method will be available; specific APIs may implement other methods). Your request URIs should be patterned after the examples in the API documentation, and you should always include your API key in a query string. See the documentation for each API for more details on request parameters and URI structure.


synchronous vs Synchronous Requests:
scrolling down in the Newsfeed Asy
loading homepage when not singed in: Sy
posting a message on a friend's timeline: Asy
clicking through a friend's pictures: Asy

AJAX Request Necessities:

Post request has : URL and some Data
Get request has: URL along with call back faction and some optional Database

Planner app: Google streetview, New York times API, Wiki API

how to integrate different APIs together in a single web app.
