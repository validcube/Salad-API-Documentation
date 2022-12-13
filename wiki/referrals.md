# Salad API Documentation

## `GET` User Balance
`GET` the autheticated user's info about referrees

URL: https://app-api.salad.io/api/v1/profile/referrals

Responses:
```json
[
   {
      "code":"P81UWS",
      "dateEntered":"2020-09-19T02:15:25.1351346+00:00",
      "earnedBalance":0.0,
      "refereeId":"db823d86-184f-425a-9cdc-5592f20c6000",
      "referralDefinition":{
         "balanceThreshold":2.0,
         "bonusRate":1.0,
         "referrerBonus":0.5
      },
      "referrerId":"0895951d-ebec-4dba-baff-a9a606cb93d5"
   },
   {
      "code":"P81UWS",
      "dateEntered":"2019-10-26T11:31:53.8130233+00:00",
      "earnedBalance":0.0,
      "refereeId":"fd634147-cc2d-46b8-92a1-256da5b8a99b",
      "referralDefinition":{
         "balanceThreshold":2.0,
         "bonusRate":1.0,
         "referrerBonus":0.5
      },
      "referrerId":"0895951d-ebec-4dba-baff-a9a606cb93d5"
   }
]
```

> List the users who have used your referral code

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication