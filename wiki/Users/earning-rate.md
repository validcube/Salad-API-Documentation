# Salad API Documentation

## `GET` earning rate
`GET` the autheticated user's earning rate (from bonuses, etc)

URL: https://app-api.salad.io/api/v2/bonuses/earning-rate

Responses:
```json
(probably) Soon TM
```

### Explaination
> **Note** <br>
> Get the user's profile information.
Soon TM

### Note
> **Note** <br>
> If the user doesn't currently have an active earning boost (2x from referral are excluded), the API will return `[]` text or 404 instead

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200	- OK <br>
401 - Requires authetication