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

### Explaination
> **Note** <br>
> Get the user's profile information
* email: Get the user's email address.
* extensions: Get the user's linked 3rd-party account like minecraft, paypal
* id: Get the user's account identifier or ID.
* lastacceptedTermsOfService: Get the user's last accepted Terms of Service.
* lastSeenApplicationVersion: Get the user's last seen application version. (Use during Alpha phase)
* pendingTermsVersion: (?)
* username: Get the username of the authenticated user.
* viewedReferralOnboarding: Get the user's viewed referral onboarding page. (Use during first sign up phase)

### Response code
HTTP response status codes <br>
200 - OK <br>
401 - Requires authetication