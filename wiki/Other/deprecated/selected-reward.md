# Salad API Documentation

> **Warning** <br>
> Deprecation Notice: This API have been abandoned since Salad remove the Chopping Cart feature. <br>
> 🔧 Recommended: None

## `GET` changelog.
`GET` The current Salad client's changelog. (during Alpha phase)

URL: https://app-api.salad.io/api/v1/profile/selected-reward

Responses:
```json
{
    "rewardId": "f9bd06d6-b3d1-4ec5-9d21-c45f2af83bcd"
}
```

### Explaination
> **Note** <br>
> UPDATED: Get the last reward (that you have selected) from the Salad Store
* rewardId: Reward/item ID

### Response code
HTTP response status codes <br>
200 - OK <br>
401 - Requires authetication