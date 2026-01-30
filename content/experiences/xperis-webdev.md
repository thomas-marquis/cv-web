---
title: "Web developer at Xperis (six-month internship)"
description: |
  Internship for my last six-month internship. My mission was to improve a monitoring tool for the Cloverleaf EAI.

weight: 10
skills:
  - name: Java
    details: |
      The entire project backend was written in Java.
  - name: Struts 2
    details: |
      Struts 2 is a Java framework that allows to create web applications.
      The existing code was written using this framework.
  - name: JavaScript
    details: |
      Since Struts 2 is a server-side rendered web framework, the frontend needed some JS for more complex interactions.
      No framework were used for the frontend, just vanilla JS and JQery. 
      (I spent hours on [this website](https://caniuse.com/), does this bring back memories?)
  - name: JQuery
  - name: D3js
    details: |
      I used D3js to create interactive charts and graphs.
      I have bench-marked several libraries and found D3js to be the most suitable for this project because of its flexibility and infinite possibilities.
  - name: CSS
  - name: Cloverleaf EAI
    details: |
      EAI stands for Enterprise Application Integration.
      It is a software architecture that allows different applications to communicate with each other.
      Cloverleaf is an commercial EAI solution provided by an US company specialized for hospitals.
  - name: R
    details: |
      Despite R was not needed for this project, I choose to use it to conduct data analysis on Cloverleaf metrics during the exploratory phase of the project.
  - name: Subversion
    details: |
      Historically, Xperis used SVN for version control.
      Thus, I had to learn how to use SVN in order to contribute to the project.
  - name: Vertx
    details: |
      Vertx is a Java framework that allows to create reactive applications.
      I used it to create a RESTful API for Cloverleaf metrics.
      This API server were hosted on the Cloverleaf server and was responsible to collect metrics and expose them to the main application backend.
  - name: SQLite
    details: |
      SQLite is the default database where Cloverleaf stored the metrics.
      The Vertx API server got connected to this database to retrieve them.
  - name: User interviews
    details: |
      I conducted user interviews with the project's users to understand their needs.
      These interviews helped me to define the project's requirements and backlog.
  - name: Needs analysis
  - name: TDD
    details: |
      The existing code didn't contain any unit tests.
      I had to write unit tests for the new features I was implementing.
      Then, I implemented most of the features using TDD.
  - name: JUnit
    details: |
      I used Junit to write unit tests for the backend.
  - name: Jasmine
    details: |
      I used Jasmine to write unit tests for the frontend.
  - name: Mockito
    details: |
      Mockito is a Java library that helps to write mocks in the unit tests.
      I used it to mock some of the backend's classes for tests.
  - name: Independent work
    details: |
      I was the only developer on this project.
  - name: Technical conception
    details: |
      For this internship, I had to design the technical architecture myself.
      My main constraint was to adapt my technical choices to the project's requirements and constraints.
period:
  from: 2017-03
  to: 2017-09
  format: %Y-%m
location: Bordeaux, France
---
# Web developer at Xperis (six-month internship)

## Context

Xperis is a French company located in Bordeaux, specialized in the healthcare EAI platform Cloverleaf.
An EAI is a software architecture that allows different applications to communicate with each other.
Cloverleaf is developed and maintained by a US company. Xperis is an independent company that distributes Cloverleaf to the hospitals in France.
Alongside, Xperis developed a monitoring platform for Cloverleaf. 
It consists of a simple web application that allows users (hospital IT departments) to monitor messages sent through the system and diagnose issues.

My mission was to add a metric dashboard to this monitoring tool.

## Key achievements

**🖼 Frontend development:**

- Developed a dashboard using D3js and vanilla JavaScript and JQuery.
- Implemented custom and interactive data visualizations using D3js.
- Implemented tests on the frontend using Jasmine.

**⚙️ Backend development:**

- Updated the backend to collect, process and expose Cloverleaf metrics to the frontend.
- Implemented unit tests for the backend using JUnit.

**🎤 User interviews:**

- Conducted interviews with some hospital IT departments managers to understand their needs.
- Defined the project's requirements and built the backlog acordingly.