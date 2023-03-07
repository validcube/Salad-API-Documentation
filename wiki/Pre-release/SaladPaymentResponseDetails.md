# Salad API Documentation

> **Warning** <br>
> Pre-release API are subjected to changes without prior notice, I can't 100% sure that this will be accurate.

## `GET` Salad Card
???

URL: Pre-release

Responses:
```json
{
    "transactionToken": "salad-pay"
}
```

### Explaination
> **Note** <br>
> ????
* `transactionToken`: The unique token to verify the transactions on Salad's server.

### Note
> **Note** <br>
> This discovered on https://github.com/SaladTechnologies/salad-applications/blob/master/packages/web-app/src/modules/salad-pay/models/SaladPaymentResponseDetails.ts
* `complete` can return `fail` on failed task, and `success` on... you guess it.