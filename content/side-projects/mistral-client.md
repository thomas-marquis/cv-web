---
title: Mistral Client
weight: 50
description: |
  A Go library for interacting with the Mistral API.
skills:
  - name: Golang
    details: |
      This library is written in Go and is designed for use in any Go project.
      The version used for this project is 1.25, which was the latest stable release at the time of writing.

      Additionally, I learned how to publish a library on GitHub Packages.
  - name: GitHub Actions
    details: |
      Continuous integration, release, and documentation builds are managed using GitHub Actions.
  - name: Mistral AI
    details: |
      Since this library implements the Mistral API interface contract, I referred to the official API documentation to ensure full compatibility.
  - name: Automated Testing
    details: |
      To maintain high quality and prevent regressions, the project includes various types of tests:
      - Standard unit tests for stateless functions, sometimes using mocks
      - A fake HTTP server with `httptest` to test the client's HTTP calls (ensuring proper request body serialization)

      Additional test types, such as fuzz testing, benchmarks, and examples, will be added in the future.
  - name: Gomock
    details: |
      Gomock is a library that generates mock objects for interfaces.
      I used it to mock internal dependencies, enabling isolated testing of specific components.
  - name: MkDocs & MkDocs Material
    details: |
      Documentation is generated with MkDocs Material and published on GitHub Pages.
      You can access it [here](https://thomas-marquis.github.io/mistral-client/).
---

# mistral-client

<p align="center">
  <img src="../assets/images/mistral-client-logo-tr.png" width="200" alt="mistral-client logo">
</p>

`mistral-client` is a Go library designed to interact with the Mistral API.

## Overview

This HTTP client provides access to all core functionalities of the Mistral API:

- Access to main endpoints (chat completion, embeddings, etc.)
- Support for streaming mode in chat completion
- Tool calling capabilities
- Output format constraints
- Model discovery

The client also includes advanced features, such as:

**Caching:**

When enabled, requests and responses are cached locally. Identical requests are served from the cache using a request
hash, reducing redundant API calls.

**MLflow Integration:**

Store your prompts in MLflow instead of hardcoding them. This approach ensures prompts are reusable and
language-agnostic, while leveraging MLflow’s versioning and tagging for better traceability and rollback capabilities.

**Upcoming Features:**

*Fake Models:*

For scenarios where generated text or embeddings are irrelevant (e.g., local app testing or UI validation),
`genkit-mistral` will provide fake models for chat completion and embeddings.

## Learn More

- [GitHub Repository](https://github.com/thomas-marquis/mistral-client)
- [Documentation](https://thomas-marquis.github.io/mistral-client/)
- [Package References](https://pkg.go.dev/github.com/thomas-marquis/mistral-client)
- [Mistral API References](https://docs.mistral.ai/api)

## Installation

```bash
go get github.com/thomas-marquis/mistral-client
```

**Requirements:**

- Go 1.25 or later

## Usage

```go
import "github.com/thomas-marquis/mistral-client/mistral"

apiKey := ""
ctx := context.Background()

client := mistral.New(apiKey,
    mistral.WithClientTimeout(60 * time.Second))

ccReq := mistral.NewChatCompletionRequest("mistral-small-latest",
    []mistral.ChatMessage{
        mistral.NewSystemMessageFromString("You are a helpful assistant."),
        mistral.NewUserMessageFromString("Tell me a joke about cats"),
    })
ccRes, err := client.ChatCompletion(ctx, ccReq)

emReq := mistral.NewEmbeddingRequest("mistral-embed", []string{"some text to embed"})
emRes, err := client.Embeddings(ctx, emReq)
```

## Design Choices and Technical Challenges

**Request Objects as Input:**

Each endpoint method accepts a request object (e.g., `ChatCompletionRequest` for `Client.ChatCompletion`).
Users must create this object before calling the method. Builder functions and options are provided to simplify the
process.

**Why not use a simple list of messages and options as parameters?**

Using request objects directly offers users greater flexibility and customization.
