---
title: "Web and Chatbot Developer at [Cdiscount](https://www.cdiscount.com/)"
description: |
  Development of Google Assistant and Messenger chatbots (using Dialogflow and Spring Boot), 
  and front/back development on the Cdiscount’s website (ReactJS) and mobile app (React Native).

  - Deployed chatbots helping users to find products
  - Developed a new navigation system on the mobile website and app
image: "content/assets/images/java-logo.png"
weight: 20
highlighted: false
skills:
  - name: Java
    details: |
      Versions used: 9, 10, 11, and 12
  - name: Spring Boot
    details: |
      Versions used: 2.0 and 2.1
  - name: ReactJS
    details: |
      - Versions used: 15 and 16
      - Language: JavaScript
      - Others: Hooks, Redux/Saga (for state management and side effects), Axios (HTTP client), later replaced by the Fetch API, Styled Components (CSS-in-JS), Jest, and Enzyme (testing)
  - name: React Native
  - name: Dialogflow (NLP)
    details: |
      Dialogflow is an NLP platform that enables the creation of chatbots.
      This solution allows users to define intents and entities without coding.
      Two approaches are possible to connect a backend:
      - **Webhook**: The backend is called by Dialogflow when a user interacts with the bot.
      - **API**: The backend calls Dialogflow to obtain the intent and entities.

      For technical and architectural reasons, we chose the Webhook approach.
  - name: Kotlin
    details: |
      Kotlin is a modern programming language that combines the best features of Java and Scala.
      It was used in the TOCK project, and I utilized it during experimentation with this platform.
  - name: Vertx
    details: |
      TOCK is written in Kotlin and uses Vertx as its event bus.
  - name: Python
    details: |
      Although Python was not part of the team's technical stack, I used it to develop small scripts for automating tasks, such as:
      - Facilitating Dialogflow setup by extracting examples from spreadsheets and injecting them into Dialogflow.
      - Conducting performance tests to compare two different NLP platforms.
  - name: Couchbase
    details: |
      Couchbase's full-text search feature is a powerful and performant tool for searching text with non-exact matches.
      We used it to index our wine catalog. When a user requested a wine and provided a short description, we converted it into a full-text search query.
  - name: MS SQL Server
    details: |
      As the company's primary database solution, we stored data in MS SQL Server.
  - name: TDD (Test-Driven Development)
    details: |
      I introduced TDD practices for the frontend using ReactJS, Enzyme, and shallow rendering.

      Shallow rendering involves rendering a component without its children, allowing tests to focus only on the component being tested.
      Enzyme also enables interaction with the rendered component, making it possible to test user interaction scenarios at the component level.
  - name: Mesos & Marathon
    details: |
      Mesos and Marathon were the company's initial container orchestrators.
      We later transitioned to Kubernetes.
  - name: Kubernetes
    details: |
      Kubernetes became the primary container orchestrator for all company microservices.
      We migrated all backend components to Kubernetes.
  - name: Git
  - name: CSS
    details: |
      For the frontend, we used [Styled Components](https://styled-components.com/) as a CSS-in-JS solution.
  - name: Technical Design
  - name: Mockito
  - name: Cucumber
    details: |
      Cucumber is a tool for writing acceptance tests in a BDD (Behavior-Driven Development) format.
      Test cases are written in Gherkin, a simple DSL that allows non-technical stakeholders to read and write them.
      The test engine was implemented in Java.

      With Cucumber, we tested complete use cases for microservices.
      Database interactions were mocked using Mockito, and REST API calls were mocked with WireMock.
  - name: JUnit
period:
  from: 2018-02
  to: 2020-03
  format: "%Y-%m"
location: Bordeaux, France
---

# Web and Chatbot Developer at Cdiscount

## Context

Cdiscount is a leading French e-commerce company. In 2018, chatbots were quite different from today, but their
popularity was on the rise.
The company formed a small team, the FT-Chatbot (FT = Feature Team), to develop its first internal chatbot.
I served as a web developer on this team for two years, from its inception to the project's conclusion.

## Key Achievements

**✨ Google Assistant Chatbot Development**

- Configured the Assistant on Google Cloud Platform and set up the NLP system using Dialogflow.
- Developed the backend in Java with Spring Boot. This REST API acted as a webhook called by Dialogflow.
- The backend implemented various use cases and conversational flows using a Responsibility-Chain pattern.

**🌟 Facebook Messenger Chatbot Development**

- Used the same architecture as the Google Assistant, including the backend and Dialogflow configuration.
- The main difference was the assistant setup on Facebook.

**☕️ Pure Backend Java Development**

- For all chatbots, the backend was developed in Java with Spring Boot.
- The backend was deployed on Kubernetes.

**🏗 Full-Stack Java & ReactJS Development**

- Beyond chatbot development, we also implemented features for the mobile website and app.
- At the time, the company used React Native for the mobile app, while the mobile website was built with ReactJS.
- I was responsible for the complete feature development process:
  - Prototyping locally to help the product owner validate design and behavior.
  - Designing the technical architecture and obtaining validation from technical experts.
  - Creating new database tables as needed.
  - Implementing and testing the backend.
  - Developing the frontend using the new or updated backend.

Some features I worked on include:

- Quick and smart filtering buttons to help users filter the catalog by suggesting filters (e.g., product size, color).
- A chatbot widget integrated directly into the search results page for specific categories.

**R&D: The Open Conversational Kit**

- [TOCK (The Open Conversational Kit)](https://doc.tock.ai/tock/master/admin/architecture.html) is an open-source French
  NLP platform for creating chatbots.
  It can be deployed on-premise or in the cloud.
- We evaluated TOCK to determine if it could replace Dialogflow in our chatbot.
- The platform is written in Kotlin, and we explored its capabilities during this period.

## Focus: How Did the Chatbot Work?

In 2018, generative AI did not yet exist. The chatbot operated using two simple techniques:

- **Intent Detection**: This is a text classification problem where an intent represents a category of user interaction.
  For example, our chatbot could advise customers on wine and toys (two distinct topics).
  We set up two main intents, one for each topic.
- **Entity Extraction**: Once an intent was identified, we extracted important information from the user's message.
  For the wine chatbot, this included details like the wine color and the type of taste the user preferred.

Dialogflow, a SaaS platform, allowed us to define intents and entities without coding.
We provided examples for each, and the platform trained the model accordingly.

Team members manually wrote all the bot's responses for each scenario.
For a given scenario, multiple similar responses were possible, and the backend randomly selected one to create the
illusion of a natural conversation.
