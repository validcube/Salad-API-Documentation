# Salad API Documentation

> **Warning** <br>
> Pre-release API are subjected to changes without prior notice, I can't 100% sure that this will be accurate.

## `GET` Salad Card
`GET` the autheticated user's Salad Card.

URL: https://app-api.salad.io/api/v2/salad-card/cards

Responses:
```json
{
    "cardId": "string",
    "closed": false,
    "locked": true,
    "panMasked": "string",
    "suspended": false
}
```

### Explaination
> **Note** <br>
> Get the user's Salad Card.
* cardId: Get the user's card ID
* closed: Check if the card was `closed`
* locked: Check if the card was `locked`
* panMasked: Salad Card Digits
* suspended: Check if the card was `suspended`

### Note
> **Note** <br>
> If the user doesn't have Salad Card, the API will return `[]`

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200	- OK <br>
401 - Requires authetication