# Salad API Documentation

## `GET` balance
`GET` the autheticated user's balance

URL: https://app-api.salad.io/api/v1/profile/balance

Responses:
```json
{
    "currentBalance":0.0336467461259585,
    "lifetimeBalance":80.68771421600665
}
```

### Explaination
> **Note** <br>
> Get the user's current & lifetime balance.
* currentBalance: Get the current balance of the user's account
* lifetimeBalance: Get the lifetime or total balance of the user's account

### Response code
HTTP response status codes <br>
200	- OK <br>
401 - Requires authetication