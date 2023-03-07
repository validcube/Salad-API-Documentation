# Salad API Documentation

> **Warning** <br>
> Pre-release API are subjected to changes without prior notice, I can't 100% sure that this will be accurate.

## `GET` Salad Card
???

URL: Pre-release

Responses:
```json
{
    "total": 123,
    "displayItems": 101
}
```

### Explaination
> **Note** <br>
> ????
* `total`: `[Required] /** The total line item */`
* `displayItems`: `[Optional] /** line items to show to the user */`

### Note
> **Note** <br>
> This discovered on https://github.com/SaladTechnologies/salad-applications/blob/master/packages/web-app/src/modules/salad-pay/models/SaladPaymentRequestOptions.ts