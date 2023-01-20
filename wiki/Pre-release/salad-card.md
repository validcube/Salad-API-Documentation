# Salad API Documentation

> **Warning** <br>
> Pre-release API are subjected to changes without prior notice, I can't 100% sure that this will be accurate.

## `GET` Salad Card
`GET` the autheticated user's Salad Card.

URL: https://app-api.salad.io/api/v2/salad-card/cards

Responses:
```json
Soon TM
```

> **Note** <br>
> Get the user's Salad Card.

If the user doesn't have Salad Card, the API will return `[]`

If the user's sAccessToken had expired, the API will return "try refresh token" text instead

HTTP response status codes
200	- OK
401 - Requires authetication