# Salad API Documentation

## `GET` 30-day-earning-history
`GET` the autheticated user's earning history (1 month)

URL: https://app-api.salad.io/api/v2/reports/30-day-earning-history

Responses:
```json
{
  "2021-08-25T14:00:00Z": 0.0018341376,
  "2021-08-25T13:00:00Z": 0.000916864128
}
```

### Explaination
> **Note** <br>
> Get the user's last 30-days earning.
* `timestamp`: Show the user's earning

If the user didn't mine after a month, the API will return `{}` or nothing instead

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200	- OK <br>
401 - Requires authetication