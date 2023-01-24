# Salad API Documentation

## `GET` User XP
`GET` the autheticated user's experiences (or, points!)

URL: https://app-api.salad.io/api/v1/profile/xp

Responses:
```json
{
    "lifetimeXp":85876
}
```

> **Note** <br>
> Get user's lifetime XP.
* lifetimeXp: Get the lifetime or total Xp of the user's account

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes <br>
200	- OK <br>
401 - Requires authetication