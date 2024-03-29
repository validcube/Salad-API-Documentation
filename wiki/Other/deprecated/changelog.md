# Salad API Documentation

> **Warning** <br>
> Deprecation Notice: Update for this API has stopped since September 24th 2021. <br>
> 🔧 Recommended: Migrate to GitHub `SaladTechnologies/salad-applications`'s release API

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

### Explaination
> **Note** <br>
> Get the application last updated changelog.
* lastUpdated: Get the current datetime of when the changelog was published.
* url: Get the URL to the changelog.

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200 - OK <br>
401 - Requires authetication