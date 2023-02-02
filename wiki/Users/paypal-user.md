# Salad API Documentation

## `GET` paypal/users
`GET` the PayPal account of the authenticated user.

URL: https://app-api.salad.io/api/v2/paypal/users

Responses:
```json
Soon TM
```

### Explaination
> **Note** <br>
> Returns the authenticated user's PayPal account
Soon TM

### Note
> **Note** <br>
> In case if the user don't have a PayPal account or have link their PayPal account to Salad, the API will return `No connected PayPal Account was found.`

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200	- OK <br>
401 - Requires authetication