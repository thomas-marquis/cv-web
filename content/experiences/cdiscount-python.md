---
title: "Python Developer at [Peaksys](https://www.linkedin.com/company/peaksys/posts/?feedView=all)"
description: |
  Industrializing Data Science projects, developing Python libraries and tools for Data Scientists,
  and mentoring them on our technical stack and best practices (clean and hexagonal architecture, TDD, BDD).

  - Designed and developed a Python framework for building data science workflows
  - Developed, optimized, and/or refactored Python ML inference jobs
  - Developed a security Python library implementing the OpenID Connect protocol
weight: 30
image: "content/assets/images/python-logo.png"
skills:
  - name: Python
    details: |
      Python is one of the company's main languages. It is used extensively for Data and Data Science projects or for internal tools.
      During this experience, I spent most of my time working with this language.
      
      I was responsible for maintaining the python-versions lifecycle for the company:
      - Assuring the libraries and docker images were available and tested for the latest versions
      - Deprecated older versions and helping teams to migrate to newer ones
      
      Versions used during this experience: from 3.7 to 3.10
  - name: Python Data Science Libraries
    details: |
      I had to get familiar with Data Science libraries and frameworks, such as:
      
      - pandas
      - numpy
      - scikit-learn
      - matplotlib
      - plotly
      - xgboost
      - lightgbm
      - spacy
      - pytorch
      - tensorflow
      
      Those libraries were used extensively by Data Scientists for their projects.
      I had to refactor, optimize and sometimes develop such project myself.
  - name: Docker
    details: |
      Developed and maintained the company's official Docker images for Python.
      I build a CICD pipeline that automatically rebuilds images on a weekly basis and deploys the images to our Docker registry.
  - name: Kubernetes
    details: |
      Resources used:
      
      - Pod, the core Kubernetes object
      - Deployment, ReplicaSet and Services for APIs
      - Job and CronJob for batch jobs (most of the Data Science inferences were done with those)
      - Secrets and ConfigMaps for configuration and secrets management. Toward the end of the missions, Secrets were abandoned in favor of Vault.
      - Persistent Volume Claims and StorageClasses for persistent data storage (e.g. persisting Jupyter notebooks for Jupyterhub)
      - Ingress and IngressControllers for external access to applications
      - CRD (Custom Resource Definitions) for custom resources such as Argo Workflows
  - name: Helm
    details: |
      Even though the CICD provides a standard Helm chart, that can be used for most of the use cases, 
      I had to develop custom Helm charts for specific applications and environments.
      E.g. Deploying Snowflake credentials on Kubernetes Secrets (before Vault was introduced).
  - name: Hexagonal Architecture
    details: |
      Hexagonal architecture implements the Clean Architecture principle.
      I deeply promoted this architecture in my team and across Data Science teams and helped them to adopt it.
      
      I implemented it in python with the following stack:
      
      - Dependency Injector, a powerful library for dependency injection
      - Pydantic for data validation and type annotations
      - FastAPI for REST APIs
      
      This kind of architecture is works with both API or streaming application and batch application (e.g. Jobs)
  - name: Pair & Mob Programming
    details: |
      I've been using pair and mob programming with:
      - Other team members, for developping libraries and internal tools
      - Data Scientists, to help them with coding best practices and unit testing
  - name: Argo Workflows
    details: |
      Argo Workflows is a Kubernetes-native workflow engine for orchestrating pods (or any other Kubernetes resources).
      We deploye the solution on our Kubernetes cluster and implemted the CICD pipelines to deploy Argo applications.
      
      The main objective was to allows Data Scientists to split their workflows into smaller steps.
      We provided a simple way to orchestrate existing or new python Jobs with a simple configuration file.
      Each job can be scheduled before or after another ones into an execution graph. 
  - name: FastAPI
    details: |
      Quickly after I began in  the team, we migrate all our APIs from Flask to FastAPI.
      This library provide better performance and helps to write clean and maintainable code.
      
      Combined to Dependency Injector, FastAPI allows to write production-grade APIs with a strong architecture.
      Matching the robustness of other languages.
  - name: Snowflake
    details: |
      Snowflake is ou main data warehouse. We started to use it in 2021 and we had to migrate to it from our old fashioned on-premise Hadoop Cluster.
      I (neither my team) didn't have to maintain this platform, a DataOps team were dedicated to it.
      Howerver, I was deeply involved in the migration process and helped to refactor and optimize existing python projects.
  - name: OIDC & OAuth2
    details: |
      Implementing a python library for OpenID Connect (OIDC) and OAuth2 protocols was a challenge.
      I had to split the library into multiple smaller ones and manage a mono-repository with Pants.
      This library implemented multiple use cases both synchronously and asynchronously:
      - **Human-to-machine**: OIDC for human authentication from a frontend.
        - Public: when the frontend (here, a python CLI) executes the authentication flow. In such a case, it's not possible to store secret information on it.
        - Private: when the authentication flow is assured by the backend. in this case, the backend can store the Client's secret
      - **Machine-to-machine**: Authenticate on technical components (e.g. a python Job, a microservice, etc.) with another (usually, a microservice)
        In this case, the first component ca invoke our library to fetch an access token from Keycloak and the use it to communicate with the second component.
  - name: Code Performance Optimization
    details: |
      Sometimes, Data Sciences Jobs take too long to run (sometimes more than 20 hours!).
      In such a case, We were missioned to identify bottlenecks and implement improvements.
      
      A classical methodology was:
      - Better batching: split large datasets into smaller batches to reduce the memory footprint, processing them concurrently to speed up the process
      - Removing unused data or columns
      - Faster libraries and algorithms and use latest versions of Python and libraries
      - Execute relational-algebra operations on Snowflake instead of pandas
  - name: Linux & Bash
    details: |
      As a big Linux fan, I've chose to work with a Linux computer.
      Furthermore, all our component were deployed on Debian containers on Kubernetes.
  - name: Git
  - name: Prometheus PromQL & Grafana
    details: |
      Created custom Grafana dashboards using Prometheus PromQL to monitor applications and infrastructure.
      Set up alerts with Zabbix (triggerd from PromQL queries)
  - name: Azure DevOps YAML Pipelines
    details: |
      Developed CI/CD pipelines using Azure DevOps YAML to automate build, test, and deployment processes.
      Ensured continuous integration and delivery for Python applications and libraries.

  - name: Technical Design
    details: |
      Each new project required a strong technical design document. This document was evaluated by an architercural comitee.
      I had to present new project to such a committee multiple times.
  - name: User Interviews
    details: |
      At the begining of the mission, I've interviewd one Data Scientist per team to understand their work process, needs and goals.
  - name: Behave
    details: |
      Used Behave for behavior-driven development (BDD), writing tests in Gherkin, a human-readable format.
  - name: Clean Architecture
    details: |
      Clean architecture principles are very simple:
      - Split the application code into multiple layers
      - The layers are organized from the inner (business domain) to the outer (infrastructure)
      - A inner layer should not depend on an outer layer
      
      Hexagonal architecture is one way to apply clean architecture principles.
      
      I used this ap
  - name: TDD (Test-Driven Development)
    details: |
      Practiced test-driven development to implement critical part of our assets.
      This practice ensures the business rules are correctly implemented and the code is robust.
      
      One example where TDD was especially useful:
      
      Implementing an authentication library in python. Ensuring the OIDC protocol was correctly implemented.
      
period:
  from: 2020-03
  to: 2022-07
  format: "%Y-%m"
location: Bordeaux, France
---
# Python Expert for Data Science

## Context

After leaving the Chatbot Team, I joined a team focused on **industrializing Data Science projects**. 
My role was to bridge the gap between Data Scientists and production environments, ensuring that their work was scalable, maintainable, and efficient. 
I developed Python libraries, frameworks, and tools to streamline workflows, improve security, and optimize performance.

During this mission, as well as the previous ones, I was employed by [SII](https://sii-group.com/en-FR) and worked at Peaksys as a full-time consultant.

## Achievements

**🛠 Python Libraries Development**
- Developed Python libraries to simplify interactions with our information system (databases, observability, file storage, etc.).
- Focused on creating reusable, modular, and well-documented code to empower Data Scientists.

**🧰 Framework Development**
- Designed and developed a **custom framework** based on Luigi to help Data Scientists write Python workflows efficiently.
- The framework enabled better organization, reproducibility, and scalability of data science projects.
- It also provided generic components to avoid code duplication and accelerate development.

**🧩 Argo Workflows**
- Deployed **Argo Workflows** on Kubernetes, allowing Data Science teams to split large workflows into smaller, manageable steps.
- Enabled scheduling and parallel execution of workflows across multiple Kubernetes pods, improving efficiency and resource utilization.

**🔑 Security and Authentication**
- Developed a **security library** implementing the **OpenID Connect (OIDC)** protocol for human-to-machine communication and **OAuth2** for machine-to-machine interactions.
- Ensured secure access to internal tools and resources, aligning with company-wide security standards.
- To tackle the complexity of this library, I split it into multiple smaller ones and managed a mono-repository with [Pants](https://www.pantsbuild.org/stable/docs/introduction/welcome-to-pants)

**❄️ Snowflake Migration**
- Assisted in migrating all **Data Science Python algorithms** to **Snowflake**.
- Used this opportunity to refactor and optimize existing Python projects, improving performance and maintainability.

**🪐 JupyterHub Deployment**
- Deployed a **JupyterHub server** on Kubernetes, providing Data Scientists with secure access to their notebook sessions.
- Each user session ran in a dedicated Kubernetes pod with custom resource allocation.
- Implemented a robust **Keycloak-based authentication system** to prevent unauthorized access.

**👩‍🏫 CI/CD Training**
- Created and led **training sessions** for Data Scientists on **CI/CD best practices**.
- Focused on automating testing, deployment, and monitoring to ensure smooth and reliable workflows.

**📏 Metrics Exporter**
- Developed an **ephemeral-storage metric exporter** for Kubernetes, enabling better monitoring and resource management.

**🧶 Performance Optimizations**
- Optimized the performance of Python batch jobs by identifying bottlenecks and implementing improvements:
  - Better batching strategies
  - Faster libraries and algorithms
  - Efficient resource utilization

**📦 Docker Images**
- Developed **standard internal Docker images** for all Python versions used in the company.
- Managed the **version lifecycle** and built automated pipelines to regularly rebuild and update images.
