# Salad API Documentation

## `GET` User Balance
`GET` the autheticated user's earning rate (from bonuses, etc)

URL: https://app-api.salad.io/api/v2/bonuses/earning-rate

Responses:
```json
(probably) Soon TM
```

> Get the user's profile information.

If the user didn't have any bonus apply, the API will return 
```json
{
    "type":"https://tools.ietf.org/html/rfc7231#section-6.5.4",
    "title":"Not Found",
    "status":404,
    "traceId":""
}
```
> The API usually returns HTTP status 404, but this is most likely caused by misconfiguration.

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication
404 - Not Found