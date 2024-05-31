# API Documentation

## Feedback

### Create Feedback

**POST** `/api/feedback/feedback/`

Create a new feedback.

- **Operation ID:** `feedback_feedback_create`
- **Tags:** feedback

**Request Body:**

- **Content Types:**
  - `application/json`
  - `application/x-www-form-urlencoded`
  - `multipart/form-data`

**Security:**

- `cookieAuth`
- `basicAuth`

**Responses:**

- **201:** 
  - **Content Type:** `application/json`
  - **Schema:** [Feedback](#feedback)

## Schema

### Retrieve Schema

**GET** `/api/schema/`

OpenApi3 schema for this API. Format can be selected via content negotiation.

- **Operation ID:** `schema_retrieve`
- **Tags:** schema

**Parameters:**

- **Query Parameters:**
  - `format`: string (enum: `json`, `yaml`)
  - `lang`: string (enum: `<various language codes>`)

**Security:**

- `cookieAuth`
- `basicAuth`

**Responses:**

- **200:**
  - **Content Types:** `application/vnd.oai.openapi`, `application/yaml`, `application/vnd.oai.openapi+json`, `application/json`
  - **Schema:** object

## Subscriptions

### Retrieve Subscription

**GET** `/api/subscriptions/subscription/`

Retrieve the authenticated user's subscription.

- **Operation ID:** `subscriptions_subscription_retrieve`
- **Tags:** subscriptions

**Security:**

- `tokenAuth`

**Responses:**

- **200:**
  - **Content Type:** `application/json`
  - **Schema:** [Subscription](#subscription)

### Update Subscription

**PUT** `/api/subscriptions/subscription/`

Update the authenticated user's subscription.

- **Operation ID:** `subscriptions_subscription_update`
- **Tags:** subscriptions

**Request Body:**

- **Content Types:**
  - `application/json`
  - `application/x-www-form-urlencoded`
  - `multipart/form-data`

**Security:**

- `tokenAuth`

**Responses:**

- **200:**
  - **Content Type:** `application/json`
  - **Schema:** [Subscription](#subscription)

## User

### Create User

**POST** `/api/user/create/`

Create a new user in the system.

- **Operation ID:** `user_create_create`
- **Tags:** user

**Request Body:**

- **Content Types:**
  - `application/json`
  - `application/x-www-form-urlencoded`
  - `multipart/form-data`

**Security:**

- `cookieAuth`
- `basicAuth`

**Responses:**

- **201:**
  - **Content Type:** `application/json`
  - **Schema:** [User](#user)

### Create Google User

**POST** `/api/user/googlecreate/`

Create a new user in the system.

- **Operation ID:** `user_googlecreate_create`
- **Tags:** user

**Request Body:**

- **Content Types:**
  - `application/json`
  - `application/x-www-form-urlencoded`
  - `multipart/form-data`

**Security:**

- `cookieAuth`
- `basicAuth`

**Responses:**

- **201:**
  - **Content Type:** `application/json`
  - **Schema:** [GoogleUser](#googleuser)

### Create Google Auth Token

**POST** `/api/user/googletoken/`

Create a new auth token for user.

- **Operation ID:** `user_googletoken_create`
- **Tags:** user

**Request Body:**

- **Content Types:**
  - `application/json`
  - `application/x-www-form-urlencoded`
  - `multipart/form-data`

**Security:**

- `cookieAuth`
- `basicAuth`

**Responses:**

- **200:**
  - **Content Type:** `application/json`
  - **Schema:** [GoogleAuthToken](#googleauthtoken)

### Retrieve Authenticated User

**GET** `/api/user/me/`

Manage the authenticated user.

- **Operation ID:** `user_me_retrieve`
- **Tags:** user

**Security:**

- `tokenAuth`

**Responses:**

- **200:**
  - **Content Type:** `application/json`
  - **Schema:** [User](#user)

### Update Authenticated User

**PUT** `/api/user/me/`

Manage the authenticated user.

- **Operation ID:** `user_me_update`
- **Tags:** user

**Request Body:**

- **Content Types:**
  - `multipart/form-data`
  - `application/x-www-form-urlencoded`

**Security:**

- `tokenAuth`

**Responses:**

- **200:**
  - **Content Type:** `application/json`
  - **Schema:** [User](#user)

### Partially Update Authenticated User

**PATCH** `/api/user/me/`

Manage the authenticated user.

- **Operation ID:** `user_me_partial_update`
- **Tags:** user

**Request Body:**

- **Content Types:**
  - `multipart/form-data`
  - `application/x-www-form-urlencoded`

**Security:**

- `tokenAuth`

**Responses:**

- **200:**
  - **Content Type:** `application/json`
  - **Schema:** [User](#user)

### Create Auth Token

**POST** `/api/user/token/`

Create a new auth token for user.

- **Operation ID:** `user_token_create`
- **Tags:** user

**Request Body:**

- **Content Types:**
  - `application/json`
  - `application/x-www-form-urlencoded`
  - `multipart/form-data`

**Security:**

- `cookieAuth`
- `basicAuth`

**Responses:**

- **200:**
  - **Content Type:** `application/json`
  - **Schema:** [AuthToken](#authtoken)

## Components

### Schemas

#### AuthToken

**Type:** object

**Description:** Serializer for the user auth token.

**Properties:**

- `email`: string, format: email
- `password`: string

**Required:**

- `email`
- `password`

#### AuthTokenRequest

**Type:** object

**Description:** Serializer for the user auth token.

**Properties:**

- `email`: string, format: email, minLength: 1
- `password`: string, minLength: 1

**Required:**

- `email`
- `password`

#### Feedback

**Type:** object

**Description:** Serializer for the feedback object.

**Properties:**

- `id`: integer, readOnly: true
- `name`: string, maxLength: 255
- `email`: string, format: email, maxLength: 255
- `issue`: string

**Required:**

- `email`
- `id`
- `issue`
- `name`

#### FeedbackRequest

**Type:** object

**Description:** Serializer for the feedback object.

**Properties:**

- `name`: string, minLength: 1, maxLength: 255
- `email`: string, format: email, minLength: 1, maxLength: 255
- `issue`: string, minLength: 1

**Required:**

- `email`
- `issue`
- `name`

#### GoogleAuthToken

**Type:** object

**Description:** Serializer for the user auth token.

**Properties:**

- `email`: string, format: email
- `name`: string

**Required:**

- `email`
- `name`

#### GoogleAuthTokenRequest

**Type:** object

**Description:** Serializer for the user auth token.

**Properties:**

- `email`: string, format: email, minLength: 1
- `name`: string, minLength: 1

**Required:**

- `email`
- `name`

#### GoogleUser

**Type:** object

**Description:** Serializer for the google user object.

**Properties:**

- `email`: string, format: email, maxLength: 255
- `name`: string, maxLength: 255
- `picture`: string, format: uri

**Required:**

- `email`
- `name`

#### GoogleUserRequest

**Type:** object

**Description:** Serializer for the google user object.

**Properties:**

- `email`: string, format: email, minLength: 1, maxLength: 255
- `name`: string, minLength: 1, maxLength: 255
- `picture`: string, format: binary
- `picture_url`: string, format: uri, writeOnly: true, minLength: 1

**Required:**

- `email`
- `name`

#### PatchedUserRequest

**Type:** object

**Description:** Serializer for the user object.

**Properties:**

- `email`: string, format: email, minLength: 1, maxLength: 255
- `password`: string, writeOnly: true, minLength: 5, maxLength: 128
- `name`: string, minLength: 1, maxLength: 255
- `country`: integer
- `picture`: string, format: binary

#### Subscription

**Type:** object

**Description:** Serializer for the subscription object.

**Properties:**

- `user`: integer, readOnly: true
- `subscription_plan`: [SubscriptionPlanEnum](#subscriptionplanenum)
- `valid_until`: string, format: date-time
- `app_key`: string, readOnly: true, nullable: true

**Required:**

- `app_key`
- `subscription_plan`
- `user`
- `valid_until`

#### SubscriptionPlanEnum

**Type:** string

**Description:** 

- `Free` - Free
- `Paid` - Paid
- `Expired` - Expired

#### SubscriptionRequest

**Type:** object

**Description:** Serializer for the subscription object.

**Properties:**

- `subscription_plan`: [SubscriptionPlanEnum](#subscriptionplanenum)
- `valid_until`: string, format: date-time

**Required:**

- `subscription_plan`
- `valid_until`

#### User

**Type:** object

**Description:** Serializer for the user object.

**Properties:**

- `email`: string, format: email, maxLength: 255
- `name`: string, maxLength: 255
- `country`: integer
- `picture`: string, format: uri

**Required:**

- `email`
- `name`

#### UserRequest

**Type:** object

**Description:** Serializer for the user object.

**Properties:**

- `email`: string, format: email, minLength: 1, maxLength: 255
- `password`: string, writeOnly: true, minLength: 5, maxLength: 128
- `name`: string, minLength: 1, maxLength: 255
- `country`: integer
- `picture`: string, format: binary

**Required:**

- `email`
- `name`
- `password`

### Security Schemes

- **basicAuth:** HTTP Basic Authentication
- **cookieAuth:** API Key Authentication (cookie: `sessionid`)
- **tokenAuth:** API Key Authentication (header: `Authorization`, prefix: "Token")
