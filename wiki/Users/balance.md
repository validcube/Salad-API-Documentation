# Salad API Documentation

## `GET` User Balance
`GET` the autheticated user's balance

URL: https://app-api.salad.io/api/v1/profile/balance

Responses:
```json
{
    "currentBalance":0.0336467461259585,
    "lifetimeBalance":80.68771421600665
}
```

> Get the user's current & lifetime balance.
* currentBalance: Get the current balance of the user's account
* lifetimeBalance: Get the lifetime or total balance of the user's account

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication