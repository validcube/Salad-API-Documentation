# Salad API Documentation

> **Warning** <br>
> Pre-release API are subjected to changes without prior notice, I can't 100% sure that this will be accurate.

## `GET` Salad Card
???

URL: Pre-release

Responses:
```json
{
    "methodName": "salad-pay",
    "details": 101,
    "complete": "success"
}
```

### Explaination
> **Note** <br>
> ????
* `methodName`: This will always be `salad-pay`
* `details`: `/** An object containing the payment details. */`
* `complete`: `/** A Salad provided function. Call this when you have processed the token data provided by SaladPay. */`

### Note
> **Note** <br>
> This discovered on https://github.com/SaladTechnologies/salad-applications/blob/master/packages/web-app/src/modules/salad-pay/models/SaladPaymentResponse.ts
* `complete` can return `fail` on failed task, and `success` on... you guess it.