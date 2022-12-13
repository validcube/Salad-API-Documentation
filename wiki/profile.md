# Salad API Documentation

## `GET` User Balance
`GET` the autheticated user's profile

URL: https://app-api.salad.io/api/v1/profile

Responses:
```json
{
   "email":"Amogus@salad.com",
   "extensions":{
      "minecraftUsername":"RedImpostor"
   },
   "id":"2deb65e6-d6ed-4bdc-8bdf-fb4a155042dd",
   "lastAcceptedTermsOfService":"1.0",
   "lastSeenApplicationVersion":"2021-09-24",
   "pendingTermsVersion":"2022-10-19T00:00:00+00:00",
   "username":"RedImpostor",
   "viewedReferralOnboarding":true
}
```

> Get the user's profile information

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication