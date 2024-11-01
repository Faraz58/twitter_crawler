# Twitter Crawler API with FastAPI

This project is a Twitter data crawler built using FastAPI. It allows users to collect data from Twitter based on usernames and keywords, with easy management via API endpoints.

## Features

- **Manage Account**: Configure user authentication information.
- **Set Proxy**: Set proxy or proxy list for the crawler.
- **Search Users**: Collect the latest 10 tweets from a list of usernames.
- **Keyword Search**: Collect the latest 10 tweets based on keywords.

## Endpoints

| Endpoint             | Method | Description                              |
|----------------------|--------|------------------------------------------|
| `/manage_account`    | POST   | User authentication configuration.       |
| `/config_proxy`      | POST   | Set proxies for the crawler.             |
| `/search_users`      | POST   | Retrieve latest tweets for usernames.    |
| `/keywords_search`   | POST   | Retrieve latest tweets based on keywords.|

## Quick Start

### Prerequisites

- Docker should be installed on your system.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/twitter_crawler.git
    cd twitter_crawler
    ```

2. **Build Docker Image**:

    ```bash
    docker build -t twitter_crawler .
    ```

3. **Run Docker Container**:

    ```bash
    docker run -d -p 8000:8000 twitter_crawler
    ```

4. **Access the API**:

   Open your browser or API client and go to [http://localhost:8000/docs](http://localhost:8000/docs) to test the API.

### Example Requests

#### Authentication Example

```bash
curl -X 'POST' \
  'http://localhost:8000/manage_account' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "your_username",
    "password": "your_password",
    "token": "your_token"
  }'
