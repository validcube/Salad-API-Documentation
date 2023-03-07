# Salad API Documentation

## `GET` Error Definition
???

Responses:
```json
{
    "message": "string",
    "errorCode": 418,
    "errorCategory": "unknown",
    "errorAction": "restart"
}
```

### Explaination
> **Note** <br>
> ????
* message: log message to look for
* errorCode: Error code
* errorCategory: Error Category
* errorAction: Action to take when SaladBowl has experienced an error.

### Note
> **Note** <br>
* `errorCategory` can be `driver`, `antiVirus`, `firewall`, `network`, and also be `silent` or `unknown` if the error can't be categorised.
* `errorAction` can be `ignore`, `restart`, and `stop` depending on the severity.