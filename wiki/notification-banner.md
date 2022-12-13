# Salad API Documentation

## `GET` Notifications banner
`GET` the current banner text

URL: https://app-api.salad.io/api/v1/notification-banner

Responses:
```json
{
   "endDate":"2021-02-23T00:00:00+00:00",
   "startDate":"2020-12-17T00:00:00+00:00",
   "text":"At the moment, newly redeemed reward codes are only available in your email inbox."
}
```

> endDate: Get the expired date for the notification banner.
> startDate: Get the start date for the notification banner.
> text: Get the text for the notification banner.

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication