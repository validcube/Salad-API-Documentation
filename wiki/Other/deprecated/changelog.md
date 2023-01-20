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

> **Note** <br>
> Get the application last updated changelog.
* lastUpdated: Get the current datetime of when the changelog was published.
* url: Get the URL to the changelog.

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication