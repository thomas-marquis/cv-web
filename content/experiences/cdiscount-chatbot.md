---
title: "Web and Chatbot Developer at Cdiscount"
weight: 20
skills:
  - name: Java
    details: |
      Version used: 9, 10, 11 and 12
  - name: Spring Boot
    details: |
      Version used: 2.0 and 2.1
  - name: ReactJS
    details: |
      - Version used: 15 and 16
      - Language: JavaScript
      - Others: hooks, Redux/Saga (for state management and side effects), Axios (HTTP client) then fetch API, Styled Components (CSS in JS), Jest and Ezyme (testing)
  - name: React Native
  - name: Dialogflow (NLP)
    details: |
      Dialogflow is a NLP platform that allows to create chatbots.
      This solution allows to define intents and entities without coding.
      Two different approaches are possible to connect a backend:
      - Webhook: the backend is called by Dialogflow when a user interacts with the bot.
      - API: the backend calls Dialogflow and then obtains the intent and entities.
      
      For some technical and architectural reasons, we decided to use the Webhook approach.
  - name: Kotlin
    details: |
      Kotlin is a modern programming language that combines the best of Java and Scala.
      It's used in the TOCK project and I used it during the experimentation around this platform.
  - name: Vertx
    details: |
      TOCK is written in Kotlin and uses Vertx as its event bus.
  - name: Python
    details: |
      Although Python wasn't part of the team's technical stack, I used it to develop a small script to automate some tasks, for instance: 
      - Facilitating Dialogflow setup, extracting examples from a Spreadsheet and injected them into Dialogflow.
      - Performance tests comparing two different NLP platforms.
  - name: Couchbase
    details: |
      The Couchbase's full text search feature is a very powerful and performant tool to search some text with non-exact match.
      We needed it to index our wine catalogue. 
      When a user ask for a wine and give a short description of what he wants, we converted it into a full-text search request.
  - name: MS SQL Server
    details: |
      As the company's main database solution, we stored on
  - name: TDD (Test-Driven Development)
    details: |
      I've introduced somme TDD practices for the front end part, with ReactJS and enzyme and shallow rendering.
      
      Shallow rendering consists in rendering a component without its children.
      This way, the tests render only the part of the component that we want to test.
      Enzime also allows to interact with the rendered component, making possible to test user interaction scenario at the component level.
  - name: Mesos & Marathon
    details: |
      Mesos and Marathon was the main company-level container orchestrator at the begining of the project.
      We soon moved to Kubernetes.
  - name: Kubernetes
    details: |
      Kubernetes became the main container orchestrator for all the company's microservices.
      We migrated all our backend components to Kubernetes.
  - name: Git
  - name: CSS
    details: |
      In the front end, we used to use [Styled Components](https://styled-components.com/) as a CSS-in-JS solution.
  - name: Technical conception
  - name: Mockito
  - name: Cucumber
    details: |
      Cucumber is a tool to write acceptance tests in a BDD (behavior-driven-development) way.
      The test cases are written in Gherkin language, a simple DSL that allows non-technical people to write and read them.
      The tests engine were then written in Java.
      
      With Cucumber, we were able to test a complete use case for a given microservice.
      Interactions with the database were mocked with Mockito, as well as the REST API calls were mocked with WireMock.
  - name: JUnit
period:
  from: 2018-02
  to: 2020-03
  format: "%Y-%m"
location: Bordeaux, France
---
# Web and Chatbot Developer at Cdiscount

## Context

Cdiscount is a French e-commerce company. In 2018, chatbots were very diferent from nowdays, but their popularity started to grow.
The company decided to create a small team - the FT-Chatbot (FT = Feature Team) - to create the first chatbot internally.
I was a web developer in this team during two years, from its very begining to the end of the project.

## Key achievements

**✨ Google Assistant Chatbot Development**

- Configured the Asistant on Google Cloud Platform and the NLP system with DialogFlow.
- Developed the backend in Java Spring Boot. This REST API acts as a hook called by Dialogflow
- The backend implemented the different use cases and conversational flows with a Responsibility-Chain pattern.

**🌟 Facebook Messenger Chatbot Development**

- Same architecture as the Google Assistant, the same backend and DialogFlow configuration were used.
- The difference lied in the assistant setup on Facebook.

**☕️ Pure backend Java Development**

- For all chatbots, the backend was written in Java with Spring Boot.
- The backend was deployed on Kubernetes.

**🏗 Full stack Java & ReactJS Development**

- On top of our chatbot development activities, we also had to implement some of the mobile website and app features.
- At this time, the company still used React Native for the mobile app.
  On its part, the mobile version of the website was implemented with ReactJS.
- I was autonomous for the complete feature development:
  - prototyping locally to help the product owner to validate the design and behavior
  - making the technical conception of the features and got validations from the technical experts
  - when needed, creating new tables on the database,
  - backend implementation and testing
  - then, frontend implementation using the new or updated backend

Some of the features I've worked on:
- Quick and smart filtering buttons to help the user to filter the catalogue with suggesting filters (product size, color, etc.)
- Chatbot widget directly integrated into the search results page for some specific categories

**R&D: The Open Conversational Kit**

- [TOCK (The Open Conversational Kit)](https://doc.tock.ai/tock/master/admin/architecture.html) is a French and open source NLP platform that allows to create chatbots.
  This solution can be deployed on-premise or in the cloud.
- We decided to test it and see if we could replace Dialogflow in our chatbot.
- The solution is written in Kotlin, and at this time, we needed to 

## Focus: how did a chatbot work?

In 2018, generative AI did not exist yet. The chatbot worked with the combination of two simple techniques:
- **Intent detection**: it is a text classification problem, an intent is simply a category of user interaction. 
  For instant, one of our chatbots where able to advise customer about wine and toys (2 different topics)
  We set up two different main intents, one for each.
- **Entity extraction**: given an intent, we now want to extract important information from the user message.
  For instance, for ou wine chatbot, the color of the wine, the kind of taste the user wants, etc.
  These pieces of information are called entities.

DialogFlow was a SAAS that allowed users to define intent and entities without coding.
We just had to add examples for each, then the platform trained the model accordingly.

The team members handwrote all the bot's replies for each possible scenario.
For a given scenario, multiple similar replies were possible, and our backend chose one of them randomly. 
It created the illusion of a "natural" conversation.


