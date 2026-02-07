---
title: "Genkit Mistral"
description: |
  A Genkit plugin for Mistral AI, enabling seamless integration of Mistral AI models into Genkit workflows.

  Genkit is a powerful SDK for building AI workflows and agents in TypeScript, Go, and Python.
  This plugin extends Genkit's capabilities to support Mistral AI models.
weight: 70
skills:
  - name: Golang
  - name: Genkit
  - name: GitHub Actions
  - name: Mistral AI
  - name: Automated Testing
  - name: Gomock
---

# Genkit Mistral

<p align="center">
  <img src="../assets/images/genkit-mistral-logo-tr.png" width="200" alt="genkit-mistral logo">
</p>

`genkit-mistral` is a **Genkit plugin** written in **Go**, designed to integrate **Mistral AI** models into Genkit
workflows.

---

## Presentation

**Genkit** is a powerful SDK for building AI workflows and agents in **TypeScript, Go, and Python**. While Genkit was
initially designed with a focus on TypeScript, its **Go version** is well-supported and actively maintained.

Genkit is **model-agnostic**, meaning your code can work with various AI models, including **OpenAI, Google AI, and
custom models**. To use a specific model, you need to install the corresponding plugin.

Genkit provides default plugins for some models, such as the **Google AI plugin** for Gemini models. However, there was
no plugin available for **Mistral AI**—until now.

This library is built on top of the [Mistral client](https://thomas-marquis.github.io/mistral-client/#getting-started),
another open-source project I developed.

---

## About the Project

- **[GitHub Repository](https://github.com/thomas-marquis/genkit-mistral/tree/main)**: Source code and project files.
- **[Documentation](https://pkg.go.dev/github.com/thomas-marquis/genkit-mistral)**: Detailed API documentation.
- **[Code Examples](https://github.com/thomas-marquis/genkit-examples/tree/main)**: Practical examples demonstrating how
  to use the plugin.
- **[Genkit Documentation](https://genkit.dev/docs/get-started/?lang=go)**: Official Genkit documentation for Go.

---

## Quick Start

### Installation

Start by installing **Genkit** and the `genkit-mistral` plugin:

```bash
go get github.com/firebase/genkit/go
go get github.com/thomas-marquis/genkit-mistral
```

### Initialization

Initialize Genkit with the Mistral plugin:

```go
package main

import (
  "context"
  "time"
  "github.com/firebase/genkit/go"
  "github.com/thomas-marquis/genkit-mistral"
  mistralclient "github.com/thomas-marquis/mistral-client"
)

func main() {
    ctx := context.Background()
    g := genkit.Init(ctx,
      genkit.WithPlugins(
        mistral.NewPlugin("<your_mistral_api_key>",
          mistral.WithClientOptions(mistralclient.WithClientTimeout(40*time.Second)), // Optional configuration
        ),
      ))
}
```

### Usage

You can now use **Genkit** to generate text, implement agentic workflows, and more with Mistral AI models.

