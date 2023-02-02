# Salad API Documentation

> **Warning** <br>
> Deprecation Notice: Salad Seasons is cancelled. <br>
> 🔧 Recommended: None.

## `GET` seasons
`GET` the autheticated user's seasons stats

URL: https://app-api.salad.io/api/v2/seasons/current

Responses:
```json
{
   "currentLevelId":7,
   "endAbsolute":"2022-01-02T06:59:00Z",
   "levels":[
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L1_Avatar_128d2ae969.jpg",
         "earnedAt":"2021-10-15T08:16:47.754963Z",
         "id":1,
         "xpRequired":1
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L2_Giveaway_Entry_0ecfce88fb.jpg",
         "earnedAt":"2021-10-15T09:35:03.4066498Z",
         "id":2,
         "xpRequired":60
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L3_Two_Worlds_II_e0c23e2723.jpg",
         "earnedAt":"2021-10-17T14:25:50.5436986Z",
         "id":3,
         "xpRequired":360
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L4_2_X_0_35_0b3cd25c76.jpg",
         "earnedAt":"2021-10-22T11:27:58.1925027Z",
         "id":4,
         "xpRequired":1440
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L5_Animated_Avatar_35ff826f98.jpg",
         "earnedAt":"2021-11-02T09:56:35.8437914Z",
         "id":5,
         "xpRequired":2880
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L6_0_75_Bonus_f65c8b3089.jpg",
         "earnedAt":"2021-11-24T07:26:45.8615625Z",
         "id":6,
         "xpRequired":4200
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L7_Fly_and_Destroy_993316d0e9.jpg",
         "earnedAt":"2021-12-23T16:02:34.4900501Z",
         "id":7,
         "xpRequired":4800
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S1_L3_2_X_1_9c155f460f.jpg",
         "id":8,
         "xpRequired":5400
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L9_Animated_Avatar_c50e3629fd.jpg",
         "id":9,
         "xpRequired":6000
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L10_1_50_Bonus_0ddceb55dc.jpg",
         "id":10,
         "xpRequired":6000
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L11_Community_Avatar_winner_39332df5d9.png",
         "id":11,
         "xpRequired":6000
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S1_L12_1_75_Bonus_25444578a5.jpg",
         "id":12,
         "xpRequired":6000
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L13_Giveaway_Entry_730548ad08.jpg",
         "id":13,
         "xpRequired":6000
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S1_L14_Team_Trees_b07e9a77a4.jpg",
         "id":14,
         "xpRequired":6000
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L15_Beyond_Earth_8792af0b59.jpg",
         "id":15,
         "xpRequired":7200
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S1_L16_3_50_Bonus_f54654cf5b.jpg",
         "id":16,
         "xpRequired":7800
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S1_L17_2_X_4_00_835ca2165b.jpg",
         "id":17,
         "xpRequired":8700
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S1_L18_Discord_Nitro_5e45766199.jpg",
         "id":18,
         "xpRequired":9900
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S2_L19_Giveaway_Entry_fb67e9b3f0.jpg",
         "id":19,
         "xpRequired":11100
      },
      {
         "bonusImageUrl":"https://assets.salad.com/strapi/assets/S1_L20_Swag_1_ae34398552.jpg",
         "id":20,
         "xpRequired":11700
      }
   ],
   "levelXp":2185,
   "name":"Season 2",
   "nextLevelId":8,
   "startAbsolute":"2021-10-01T18:00:00Z",
   "totalXp":15926
}
```

### Explaination
> **Note** <br>
> Get the user's stats about the season
* currentLevelId: Get the user's current level
* endAbsolute: Get the Seasons end date
* levels: List all the available reward to get
* levelXp: Get the required XP to reach the next level
* name: Name of the Seasons
* nextLevelId: Get the user's next level
* startAbsolute: Get the Seasons start date
* totalXp: Get the XP that the user have earned since the start of Seasons

### Accepted cookies
(required) - sAccessToken

### Response code
HTTP response status codes <br>
200 - OK <br>
401 - Requires authetication