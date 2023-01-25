# Salad API Documentation

> **Warning** <br>
> Deprecation Notice: Update for this API has stopped since Salad 0.5.6, the last build for macOS. <br>
> 🔧 Recommended: Migrate to GitHub `SaladTechnologies/salad-applications`'s release API.

## `GET` Application Version
`GET` the current application version for Salad client application.

URL: https://app-api.salad.io/api/v1/desktop-app/version

Responses:
```json
{
   "path":"Salad-0.5.6.exe",
   "releaseDate":"2021-09-01T13:35:00.791+00:00",
   "version":"0.5.6"
}
```

### Explaination
> **Note** <br>
> Get the application's version.
* path: Get the path to download the application.
* releaseDate: Get the release date of the application.
* version: Get the version of the application.

### Response code
HTTP response status codes <br>
200 - OK <br>
401 - Requires authetication