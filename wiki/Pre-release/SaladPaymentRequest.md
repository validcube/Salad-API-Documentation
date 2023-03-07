# Salad API Documentation

> **Warning** <br>
> Pre-release API are subjected to changes without prior notice, I can't 100% sure that this will be accurate.

## `GET` Salad Card
???

URL: Pre-release

Responses:
```json
{
    "canMakePayment": true,
    "show": "A name that the browser shows the customer in the payment interface.",
    "abort": "",
    "on": ""
}
```

### Explaination
> **Note** <br>
> ????
* `canMakePayment`: `/** Indicates whether the PaymentRequest object can make a payment before calling show(). */`
* `show`: `/** Causes the user agent to begin the user interaction for the payment request. */`
* `abort`: `/** Causes the user agent to end the payment request and to remove any user interface that might be shown. */`
* `on`: `/** Listen for specific payment actions  */`

### Note
> **Note** <br>
> This discovered on https://github.com/SaladTechnologies/salad-applications/blob/master/packages/web-app/src/modules/salad-pay/models/SaladPaymentRequest.ts