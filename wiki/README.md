# Salad API Documentation
<a href="https://gitmoji.dev">
  <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji">
</a>

> **Note** <br>
> This repository is not officially endorsed by [Salad Technologies©️](https://salad.com/), use it at your own risk!

## User API Documentation

| Documentation | Category | Method | API |
| --- | --- | --- | --- |
| Return user's profile information | Users | `GET` | https://app-api.salad.io/api/v1/profile |
| Return user's current & lifetimebalance | Users | `GET` | https://app-api.salad.io/api/v1/profile/balance |
| Return user's XP | Users | `GET` | https://app-api.salad.io/api/v1/profile/xp |
| Return user's referral code | Users | `GET` | https://app-api.salad.io/api/v1/profile/referral-code |
| Return a list of user that use your code | Users | `GET` | https://app-api.salad.io/api/v1/profile/referrals |
| Return a list of redemptions (reward vault) | Users | `GET` | https://app-api.salad.io/api/v2/redemptions |
| Return earning history for the past 30 days | Users | `GET` | https://app-api.salad.io/api/v2/reports/30-day-earning-history |
| Return a list of unlocked avatars | Users | `GET` | https://app-api.salad.io/api/v2/avatars |
| Return the user's equipped avatar | Users | `GET` | https://app-api.salad.io/api/v2/avatars/selected |
| Return a list of unclaimed bonus(es) | Users | `GET` | https://app-api.salad.io/api/v2/bonuses |
| Return Salad mining ID | Users | `POST` | https://app-api.salad.io/api/v2/machines |
| Refresh sAccessToken | Auth | `POST` | https://app-api.salad.io/auth/session/refresh |
| Verify the OTP code (SuperToken) | Auth | `POST` | https://app-api.salad.io/api/v2/authentication-sessions/verification |
| initialise the authentication process (login process) | Auth | `POST` | https://app-api.salad.io/api/v2/authentication-sessions |
| Return the current Salad API status | Other | `GET` | https://app-api.salad.io/health/ready |
| Return the changelog for Salad | Deprecated (Other) | `GET` | https://app-api.salad.io/api/v2/changelog |
| Return the current seasons | Deprecated (Users) | `GET` | https://app-api.salad.io/api/v2/seasons/current |
| Return the user's Salad card (& also start the creation process) | Pre-release | `GET`, `POST` | https://app-api.salad.io/api/v2/salad-card/cards |
| Return the Salad card balance | Pre-release | `GET` | https://app-api.salad.io/api/v2/salad-card/cards/${this.saladCard?.cardId}/balance |
| Return the Salad card status | Pre-release | `GET` | https://app-api.salad.io/api/v2/salad-card/cards/${this.saladCard?.cardId}/locked |
| Replace (or re-enroll) Salad card | Pre-release | `POST` | https://app-api.salad.io/api/v2/salad-card/cards/${this.saladCard?.cardId}/replace |
| Return the Salad card Info (embed) | Pre-release | `GET` | https://app-api.salad.io/api/v2/salad-card/cards/${this.saladCard?.cardId}/embed |