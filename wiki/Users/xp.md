# Salad API Documentation

## `GET` xp
`GET` the autheticated user's experiences (or, points!)

URL: https://app-api.salad.io/api/v1/profile/xp

Responses:
```json
{
    "lifetimeXp":85876
}
```

### Explaination
> **Note** <br>
> Get user's lifetime XP.
* lifetimeXp: Get the lifetime or total Xp of the user's account

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200	- OK <br>
401 - Requires authetication