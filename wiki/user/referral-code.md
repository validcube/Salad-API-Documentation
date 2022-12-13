# Salad API Documentation

## `GET` User Balance
`GET` the autheticated user's referral code

URL: https://app-api.salad.io/api/v1/profile/referral-code

Responses:
```json
{
    "code":"P81UWS"
}
```

> Show the user's referral code

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication