# Salad API Documentation

## `GET` selected avatar
`GET` the autheticated user's selected avatar.

URL: https://app-api.salad.io/api/v2/avatars/selected

Responses:
```json
{
   "description":" ",
   "id":"c5a827bf-01bd-4949-83f3-6c9e367b749f",
   "imageUrl":"https://assets.salad.com/strapi/assets/Recipe_Composition_Animated_23f439bde5.png",
   "name":"\"Dice\" Avatar"
}
```

* description: Get the current description of the selected avatar.
* id: Get the ID of the selected avatar.
* imageUrl: Get the image URL of the selected avatar.
* name: Get the name of the selected avatar.

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication