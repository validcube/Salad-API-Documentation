# Salad API Documentation

## `GET` referrals
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

### Explaination
> **Note** <br>
> List the users who have used your referral code
* code: Get the code of your referral code
* dateEntered: Get the date that the referral code was entered
* earnedBalance: Get the amount of Salad balance that was 
* refereeId: Get the referee ID (probably user ID)
* referralDefinition
 - balanceThreshold: Get the cap limit of the referee
 - bonusRate: Get the bonus rate of that referee
 - referrerBonus: Get the bonus of your code
* referrerID: Get the ID of the referrer (the user that own the code)

### Response code
HTTP response status codes <br>
200 - OK <br>
401 - Requires authetication