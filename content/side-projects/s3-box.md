---
title: S3 Box
weight: 30
description: |
  A desktop application for managing S3 buckets. Written in Go.
skills:
  - name: Golang
  - name: S3
  - name: Github Actions
  - name: Test Containers
  - name: Automated Testing
  - name: Gomock
  - name: Fyne
  - name: Design Patterns
    details: |
      - State
  - name: Domain Driven Design
  - name: MVVM Pattern
  - name: Event Driven Architecture
  - name: Clean Architecture
---

# S3-Box

<p align="center">
  <img src="../assets/images/s3-box-logo-tr.png" width="200" alt="s3 box logo">
</p>

S3-Box is a desktop application for managing S3 buckets, written in Go.

## Presentation

I've always been disappointed by S3 client applications. Sometimes, they are too complex or not user friendly.
Some other times, they are web applications and need complex setups to be used. And sometimes, they are not free.

That's why I decided to create my own S3 client application.
Since this project was first motivated by my personal needs, I mostly needs it for my personal project. So, I've decided
to develop it as a personal side project.

## Links

- [GitHub repository](https://github.com/thomas-marquis/s3-box)

## Technical considerations

- **Fyne** - Cross platform GUI framework
  ([fyne](https://fyne.io/)) enable a desktop (bu also mobile) application to be developed in Go.
- **MVVM** - I've implemented the Model-View-ViewModel architecture pattern to separate the business logic from the UI.
  View models are classes that handle the business logic and update the application state. The UI is able to observe
  changes
  in the view models and update itself accordingly.
- **Event Driven Architecture** - The application is event driven.
  When a domain object's method is called, it returns an event. This event is then send through an event bus to all
  interested parts of the application.
- **Clean architecture** - The application is clean architecture compliant.
  The domain layer doesn't depends on any other layer. Here, the ViewModels ats as a user case layer, orchestrating
  domain objects.
- **Domain Driven Design** - I tried to follow the Domain Driven Design principles.
  The domain code is as close as possible to the real-world concepts (here, files, directories, etc.)

## Screenshots

![s3-box explorer view screenshot](../assets/images/s3box-screenshot.png)

![s3-box connection view screenshot](../assets/images/s3box-connection-screenshot.png)

![s3-box conenction form screenshot](../assets/images/s3box-conn-form-screenshot.png)