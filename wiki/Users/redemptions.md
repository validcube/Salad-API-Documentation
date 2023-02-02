# Salad API Documentation

## `GET` redemptions / reward-vault
`GET` the entire purchase history

URL: 
* https://app-api.salad.io/api/v1/reward-vault
* https://app-api.salad.io/api/v2/redemptions

Responses:
```json
[
   {
      "code":"0Z0AY-3D24J-EV8R8",
      "id":"d305f74c-4bb7-4e9b-8e63-13f84f4fbf47",
      "name":"Angry Golf",
      "price":0.4,
      "status":"complete",
      "timestamp":"2020-09-12T11:26:03.272142+00:00"
   },
   {
      "id":"4d030b02-8a85-4e3a-a53d-f6d332081d51",
      "name":"A Story About My Uncle",
      "price":1.1607142857142856,
      "status":"failed",
      "timestamp":"2020-09-12T11:23:17.7946405+00:00"
   },
   {
      "code":"https://discord.gift/cyH5Pe2j4ptQDJdRhF9r4XUU",
      "id":"f0280072-99e2-442a-adf9-a145706f3dfa",
      "name":"(old) Discord Nitro Classic",
      "price":4.99,
      "status":"complete",
      "timestamp":"2020-08-20T12:45:10.1365675+00:00"
   },
]
```

### Explaination
> **Note** <br>
> Get user's all redeemed items.
* code: Get the redemptions code for the item. (if any)
* id: Get the redemptions id for the item.
* name: Get the redemptions name for the item
* price: Get the redemptions price for the item.
* status: Get the redemptions status for the item.
* timestamp: Get the redemptions timestamp for the item.

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200 - OK <br>
401 - Requires authetication