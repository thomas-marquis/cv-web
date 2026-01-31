---
title: "Web Developer at Xperis (Six-Month Internship)"
description: |
  This internship marked the final six months of my studies. 
  My mission was to enhance a monitoring tool for the Cloverleaf EAI platform by developing a metric dashboard.
weight: 10
image: "content/assets/images/java-logo.png"
skills:
  - name: Java
    details: |
      The entire project backend was developed in Java.
  - name: Struts 2
    details: |
      Struts 2 is a Java framework designed for creating web applications. 
      The existing codebase was built using this framework.
  - name: JavaScript
    details: |
      As Struts 2 is a server-side rendered framework, JavaScript was essential for implementing complex frontend interactions. 
      No frontend frameworks were used. Only vanilla JavaScript and jQuery.
      (I spent hours on [this website](https://caniuse.com/), does this bring back memories?)
  - name: jQuery
  - name: D3.js
    details: |
      I used D3.js to create dynamic and interactive charts and graphs. 
      After benchmarking several libraries, D3.js was selected for its flexibility and extensive customization options.
  - name: CSS
  - name: Cloverleaf EAI
    details: |
      EAI (Enterprise Application Integration) is a software architecture that facilitates communication between different applications. 
      Cloverleaf is a commercial EAI solution developed by a US company, specifically tailored for healthcare environments.
  - name: R
    details: |
      Although R was not a requirement for the project, I used it during the exploratory phase to analyze Cloverleaf metrics and gain insights.
  - name: Subversion (SVN)
    details: |
      Xperis historically used SVN for version control. I learned and utilized SVN to contribute effectively to the project.
  - name: Vert.x
    details: |
      Vert.x is a Java framework for building reactive applications. 
      I used it to develop a RESTful API for collecting and exposing Cloverleaf metrics. 
      This API was hosted on the Cloverleaf server.
  - name: SQLite
    details: |
      SQLite served as the default database for storing Cloverleaf metrics. The Vert.x API connected to this database to retrieve the necessary data.
  - name: User Interviews
    details: |
      I conducted interviews with hospital IT department managers to understand their needs and pain points. 
      These interviews were instrumental in defining the project requirements and shaping the backlog.
  - name: Needs Analysis
  - name: TDD (Test-Driven Development)
    details: |
      The existing codebase lacked unit tests. 
      I introduced unit testing for new features and adopted TDD for most of the development process.
  - name: JUnit
    details: |
      JUnit was used to write unit tests for the backend components.
  - name: Jasmine
    details: |
      Jasmine was employed to write unit tests for the frontend logic.
  - name: Mockito
    details: |
      Mockito, a Java library for creating mock objects, was used to simulate dependencies in backend unit tests.
  - name: Independent Work
    details: |
      I was the sole developer on this project, responsible for all aspects of design, development, and testing.
  - name: Technical Design
    details: |
      I designed the technical architecture for the project, ensuring that all choices aligned with the requirements and constraints of the platform.
period:
  from: 2017-03
  to: 2017-09
  format: "%Y-%m"
location: Bordeaux, France
---
# Web Developer at Xperis (Six-Month Internship)

## Context

Xperis is a French company based in Bordeaux, specializing in the **Cloverleaf EAI platform** for healthcare. 
**EAI (Enterprise Application Integration)** enables seamless communication between different software applications. 
Cloverleaf, developed and maintained by a US company, is distributed in France by Xperis. Alongside this, 
Xperis developed a **monitoring platform** for Cloverleaf—a web application designed to help hospital 
IT departments monitor system messages and diagnose issues.

My mission was to **enhance this monitoring tool by adding a metric dashboard**.

## Key Achievements

### 🖼 Frontend Development
- Developed a **dashboard** using **D3.js**, vanilla JavaScript, and jQuery.
- Created **custom, interactive data visualizations** with D3.js.
- Implemented **frontend tests** using Jasmine.

### ⚙️ Backend Development
- Updated the backend to **collect, process, and expose Cloverleaf metrics** to the frontend.
- Introduced **unit testing** for the backend using JUnit.

### 🎤 User-Centric Approach
- Conducted **interviews with hospital IT managers** to identify their needs.
- Defined **project requirements** and built the backlog based on user feedback.
