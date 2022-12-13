# Salad API Documentation

## `GET` changelog.
`GET` The current Salad client's changelog. (during Alpha phase)

URL: https://app-api.salad.io/api/v2/changelog

Responses:
```json
{
   "lastUpdated":"2021-09-24",
   "url":"https://salad.com/whats-new"
}
```

* lastUpdated: Get the current datetime of when the changelog was published.
* url: Get the URL to the changelog.

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication