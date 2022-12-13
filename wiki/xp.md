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

> lifetimeXp: Get the lifetime or total Xp of the user's account

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication