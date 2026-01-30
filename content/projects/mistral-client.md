---
title: Mistral Client
section: personal
weight: 50
skills:
  - name: Golang
    details: |
      This library is written in Golang and can be used in any Golang project.
      The version used for this project is 1.25, the latest stable one at the time of writing.
      
      On top of this, I had to learn how to publish a library on Github Packages.
  - name: Github Actions
    details: |
      Continuous integration, release and documentation build are performed with Github Actions.
  - name: Mistral AI
    details: |
      As this library implements an interface contract of Mistral API, I had to check the API documentation to ensure compatibility.
  - name: Automated Testing
    details: |
      In order to ensure the quality of the library and prevent regressions, I used diferent kinds of tests inside the project:
      - Regular unit tests for stateless functions, sometimes with mocks
      - Fake HTTP server with httptest to test the client's HTTP calls (ensuring the request body is correctly serialized)
      
      Other kind of tests will be added in the future (e.g. Fuzz, Benchmark, Examples...)
  - name: Gomock
    details: |
      Gomock is a library able to generate mock objects for interfaces.
      I used it to mock some internal dependencies of the library to test some other parts in isolation.
  - name: MKdoc & MKdocs Material
    details: |
      Documentation is generated with MKdoc Material and published on Github Pages.
      It is available [here](https://thomas-marquis.github.io/mistral-client/).
---
# mistral-client

<p align="center">
  <img src="../assets/images/mistral-client-logo-tr.png" width="200" alt="mistral-client logo">
</p>

`mistral-client` is a Golang library for interacting with the Mistral API.

## Presentation

It is an HTTP client that provides all the basic functionality of the Mistral API:

- Calling the main endpoints (chat completion, embedding, etc.)
- Supports streaming mode for chat completion
- Tool calling
- Output format constraint
- Model discovery

This client also provides some advanced features such as:

**Caching**: 

If enabled, the requests and responses are cached locally. Thanks to the request's hash, if the user send the exact same request twice, the API won't be called and the cached response will be returned.

Coming soon:

**Fake models**:

If you don't care about the generated text or embedding (e.g. when you just want to run you app locally, or check the UI is correctly rendered...)
genkit-mistral provides you some fake models (one for chat completion and one for embeddings).

**MLflow integration**:

You can store your prompts on MLflow instead of writing them directly in your code.
That way, prompts become a reusable and language agnostic asset. 
you can also leverage the MLflow prompt registry versioning and tagging capabilities to enhance the traceability and rollback.


## Learn more

* [GitHub repository](https://github.com/thomas-marquis/mistral-client)
* [Documentation](https://thomas-marquis.github.io/mistral-client/)
* [Package references](https://pkg.go.dev/github.com/thomas-marquis/mistral-client)
* [Mistral API references](https://docs.mistral.ai/api)


## Installation

```bash
go get github.com/thomas-marquis/mistral-client
```

Requirements:

- Go >= 1.25

## Usage

```go
import "github.com/thomas-marquis/mistral-client/mistral"

apiKey := ""
ctx := context.Background()

client := mistral.New(apiKey,
                mistral.WithClientTimeout(60 * time.Second))
                
ccReq := mistral.NewChatCompletionRequest("mistral-small-latest",
   []mistral.ChatMessage{
       mistral.NewSystemMessageFromString("you are a helpful assistant."),
       mistral.NewUserMessageFromString("Tell me a joke about cats"),
    })
ccRes, err := client.ChatCompletion(ctx, ccReq)

emReq := mistral.NewEmbeddingRequest("mistral-embed", []string{"some text to embed"})
emRes, err := client.Embeddings(ctx, emReq)
```

## Conception choices and technical challenges

**Request object as input**

Each endpoint method takes a request object as input (e.g. `ChatCompletionRequest` for `Client.ChatCompletion`, etc.)
User must create this object first, before calling the method. 
Builder function and options are available to make this process as smooth as possible.

_Why not just some list of messages and options as parameters?_

From a user perspective, manipulating the request object directly allows more freedom and customization.

