# Salad API Documentation

## `GET` avatars
`GET` the autheticated user's unlocked avatar(s)

URL: https://app-api.salad.io/api/v1/profile

Responses:
```json
[
   {
      "description":" ",
      "id":"6fad3221-d2ab-485d-97cc-50f640e0f8de",
      "imageUrl":"https://assets.salad.com/strapi/assets/carrot_3fad4b85bf.png",
      "name":"Carrot"
   },
   {
      "description":" ",
      "id":"99b80c2a-4805-42d1-a094-4ea9e3e5e2ee",
      "imageUrl":"https://assets.salad.com/strapi/assets/alpha_tester_d3e4f61f53.png",
      "name":"Alpha Tester"
   },
   {
      "description":" ",
      "id":"c4e8df05-1d96-4f6b-94d2-7650465782ab",
      "imageUrl":"https://assets.salad.com/strapi/assets/S2_Toss_12e256ecdc.png",
      "name":"\"Toss\" Avatar"
   },
]
```

> Get the user's unlocked avatars.
* description: Get the avatar's description.
* id: Get the avatar's id.
* imageUrl: Get the avatar's image URL.
* name: Get the avatar's name.

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication