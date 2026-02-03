---
title: "Genkit Mistral"
description: |
  Genkit plugin for Mistral AI.

  Genkit is a powerful SDK for building AI workflows and agents in TypeScript, Go and Python.
weight: 70
skills:
  - name: Golang
  - name: Genkit
  - name: Github Actions
  - name: Mistral AI
  - name: Automated Testing
  - name: Gomock
---

# Genkit Mistral

<p align="center">
  <img src="../assets/images/genkit-mistral-logo-tr.png" width="200" alt="genkit-mistral logo">
</p>


`gekit-mistral` is a Genkit plugin written in Go.

## Presentation

Genkit is a powerful SDK for building AI workflows and agents in TypeScript, Go and Python.
Even though Genkit was primarily designed for TypeScript, the Golang version is well supported and actively maintained.

Genkit is model-agnostic: your code can either work for OpenAI's model as well as for your own custom models.
You need to install a plugin for each model you want to use.

Some plugins are available by default, for instance, the Google AI plugin that enables the Gemini AI models.

Unfortunately, no plugin exists for Mistral AI yet. That's why I created this project.

This library is built on top of this
non-official [Mistral client](https://thomas-marquis.github.io/mistral-client/#getting-started) library, another of my
side projects.

## About the project

- [GitHub repository](https://github.com/thomas-marquis/genkit-mistral/tree/main)
- [Documentation](https://pkg.go.dev/github.com/thomas-marquis/genkit-mistral)
- [Code examples](https://github.com/thomas-marquis/genkit-examples/tree/main)
- [Genkit's documentation](https://genkit.dev/docs/get-started/?lang=go)

## Quick start

Start by installing Genkit and the plugin:

```bash
go get github.com/firebase/genkit/go
go get github.com/thomas-marquis/genkit-mistral
```

Then, initialise Genkit:

```go
package main

import (
  "github.com/firebase/genkit/go"
  "github.com/thomas-marquis/genkit-mistral"
  mistralclient "github.com/thomas-marquis/mistral-client"
)

func main() {
    ctx := context.Background()
    g := genkit.Init(ctx,
      genkit.WithPlugins(
        mistral.NewPlugin("<your_mistral_api_key>",
          mistral.WithClientOptions(mistralclient.WithClientTimeout(40*time.Second)), // Optional options
        ),
      ))
}
```

You can now use Genkit to generate text, implement agentic flows, etc.
