# CLI-Auth

## Overview

CLI-Auth is a demonstration application that showcases Single Sign-On (SSO) integration using OpenID Connect (OIDC) for both web and CLI applications. This project aims to provide a comprehensive example of how to implement SSO in different types of applications.

## Features

- SSO integration using OIDC
- Web application authentication
- CLI application authentication

## Prerequisites

- Node.js
- npm or yarn
- An OIDC provider (e.g., Auth0, Okta)

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/kharkevich/web-cli-oidc-sso
    cd cli-auth
    ```

2. Install dependencies:
    ```sh
    npm install
    # or
    yarn install
    ```

3. Configure OIDC provider:
    - Create an application in your OIDC provider.
    - Note down the client ID, client secret, and issuer URL.

4. Create a `.env` file in the root directory and add the following environment variables:
    ```env
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    ISSUER_URL=your_issuer_url
    ```

## Running the Application

### Web Application

1. Start the web application:
    ```sh
    npm run start:web
    # or
    yarn start:web
    ```

2. Open your browser and navigate to `http://localhost:3000`.

### CLI Application

1. Start the CLI application:
    ```sh
    npm run start:cli
    # or
    yarn start:cli
    ```

2. Follow the prompts to authenticate via the CLI.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements

- [OpenID Connect](https://openid.net/connect/)
