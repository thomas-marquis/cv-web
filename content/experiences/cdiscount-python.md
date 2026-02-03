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
      Python was one of the company's primary languages, extensively used for Data and Data Science projects, as well as internal tools.
      During this experience, the majority of my work involved Python development.

      **Responsibilities:**
      - Managed the Python version lifecycle for the company:
        - Ensured libraries and Docker images were available and tested for the latest versions
        - Deprecated older versions and assisted teams in migrating to newer ones
      - Versions used: 3.7 to 3.10

  - name: Python Data Science Libraries
    details: |
      Worked extensively with Data Science libraries and frameworks, including:
      - pandas, numpy, scikit-learn, matplotlib, plotly, xgboost, lightgbm, spacy, pytorch, and tensorflow

      These libraries were widely used by Data Scientists for their projects.
      My role included refactoring, optimizing, and occasionally developing projects using these libraries.

  - name: Docker
    details: |
      **Developed and maintained** the company's official Docker images for Python.
      - Built a CI/CD pipeline to automatically rebuild images on a weekly basis
      - Deployed images to the company's Docker registry

  - name: Kubernetes
    details: |
      Utilized a variety of Kubernetes resources:
      - **Pods**: Core Kubernetes objects for running applications
      - **Deployments, ReplicaSets, and Services**: For managing APIs
      - **Jobs and CronJobs**: For batch jobs, particularly Data Science inference tasks
      - **Secrets and ConfigMaps**: For configuration and secrets management (later transitioned to Vault)
      - **Persistent Volume Claims and StorageClasses**: For persistent data storage (e.g., Jupyter notebooks for JupyterHub)
      - **Ingress and IngressControllers**: For external access to applications
      - **CRDs (Custom Resource Definitions)**: For custom resources like Argo Workflows

  - name: Helm
    details: |
      While the CI/CD pipeline provided a standard Helm chart for most use cases, I developed custom Helm charts for specific applications and environments.
      - Example: Deploying Snowflake credentials on Kubernetes Secrets before the introduction of Vault

  - name: Hexagonal Architecture
    details: |
      Promoted and implemented hexagonal architecture, which adheres to Clean Architecture principles.
      - Used **Dependency Injector** for dependency injection
      - Used **Pydantic** for data validation and type annotations
      - Used **FastAPI** for REST APIs

      This architecture was applied to both API/streaming applications and batch applications (e.g., Jobs).

  - name: Pair & Mob Programming
    details: |
      Practiced pair and mob programming:
      - With team members for developing libraries and internal tools
      - With Data Scientists to guide them on coding best practices and unit testing

  - name: Argo Workflows
    details: |
      **Argo Workflows** is a Kubernetes-native workflow engine for orchestrating Kubernetes resources.
      - Deployed Argo Workflows on the company's Kubernetes cluster
      - Implemented CI/CD pipelines for deploying Argo applications

      The main objective was to enable Data Scientists to split their workflows into smaller steps, orchestrated via a simple configuration file.
      Each job could be scheduled before or after another, forming an execution graph.

  - name: FastAPI
    details: |
      Migrated all APIs from Flask to FastAPI early in my tenure.
      - FastAPI offers better performance and supports writing clean, maintainable code
      - Combined with Dependency Injector, FastAPI enabled the development of production-grade APIs with robust architecture

  - name: Snowflake
    details: |
      Snowflake served as the company's main data warehouse.
      - Began using Snowflake in 2021, migrating from an on-premise Hadoop Cluster
      - Played a key role in the migration process, helping to refactor and optimize existing Python projects

  - name: OIDC & OAuth2
    details: |
      Developed a Python library for **OpenID Connect (OIDC)** and **OAuth2** protocols.
      - Split the library into smaller modules and managed a monorepo using **Pants**
      - Implemented multiple use cases, both synchronous and asynchronous:
        - **Human-to-machine**: OIDC for human authentication from a frontend (public and private flows)
        - **Machine-to-machine**: Authentication between technical components (e.g., Python Jobs, microservices)

  - name: Code Performance Optimization
    details: |
      Addressed performance bottlenecks in Data Science jobs, some of which took over 20 hours to run.
      - Applied a structured methodology for optimization:
        - Better batching: Split large datasets into smaller batches to reduce memory usage and speed up processing
        - Removed unused data or columns
        - Utilized faster libraries and algorithms, and ensured the latest versions of Python and libraries were used
        - Offloaded relational-algebra operations to Snowflake instead of pandas

  - name: Linux & Bash
    details: |
      Worked extensively with Linux and Bash for automation, system administration, and deployment tasks.
      - All components were deployed on Debian containers within Kubernetes

  - name: Git

  - name: Prometheus PromQL & Grafana
    details: |
      Created custom Grafana dashboards using Prometheus PromQL to monitor applications and infrastructure.
      - Set up alerts with Zabbix, triggered from PromQL queries

  - name: Azure DevOps YAML Pipelines
    details: |
      Developed CI/CD pipelines using Azure DevOps YAML to automate build, test, and deployment processes.
      - Ensured continuous integration and delivery for Python applications and libraries

  - name: Technical Design
    details: |
      Prepared technical design documents for new projects, reviewed by an architectural committee.
      - Presented new projects to the committee multiple times

  - name: User Interviews
    details: |
      Conducted user interviews with Data Scientists at the beginning of the mission.
      - Aimed to understand their workflows, needs, and goals

  - name: Behave
    details: |
      Used **Behave** for behavior-driven development (BDD).
      - Wrote tests in **Gherkin**, a human-readable format

  - name: Clean Architecture
    details: |
      Applied Clean Architecture principles:
      - Split application code into multiple layers, organized from inner (business domain) to outer (infrastructure)
      - Ensured inner layers did not depend on outer layers

      Hexagonal architecture was one approach to applying these principles.

  - name: TDD (Test-Driven Development)
    details: |
      Practiced Test-Driven Development (TDD) for critical parts of projects.
      - Ensured business rules were correctly implemented and the code was robust
      - Example: Implementing an authentication library in Python to ensure correct OIDC protocol implementation

period:
  from: 2020-03
  to: 2022-07
  format: "%Y-%m"
location: Bordeaux, France
---
# Python Expert for Data Science

## Context

After leaving the Chatbot Team, I joined a team focused on **industrializing Data Science projects** at [Peaksys](https://www.linkedin.com/company/peaksys/posts/?feedView=all) (the Cdiscount's IT subsidiary). 
My role was to bridge the gap between Data Scientists and production environments, ensuring their work was scalable, maintainable, and efficient. 
I developed Python libraries, frameworks, and tools to streamline workflows, improve security, and optimize performance.

During this mission, I was employed by [SII](https://sii-group.com/en-FR) and worked at Peaksys as a full-time consultant.

## Achievements

**🛠 Python Libraries Development**
- Developed Python libraries to simplify interactions with the company's information system (databases, observability, file storage, etc.).
- Focused on creating reusable, modular, and well-documented code to empower Data Scientists.

**🧰 Framework Development**
- Designed and developed a **custom framework** based on Luigi to help Data Scientists write Python workflows efficiently.
- The framework improved organization, reproducibility, and scalability of data science projects.
- Provided generic components to avoid code duplication and accelerate development.

**🧩 Argo Workflows**
- Deployed **Argo Workflows** on Kubernetes, enabling Data Science teams to split large workflows into smaller, manageable steps.
- Facilitated scheduling and parallel execution of workflows across multiple Kubernetes pods, enhancing efficiency and resource utilization.

**🔑 Security and Authentication**
- Developed a **security library** implementing **OpenID Connect (OIDC)** and **OAuth2** protocols.
- Ensured secure access to internal tools and resources, aligning with company-wide security standards.
- Managed complexity by splitting the library into smaller modules and using **Pants** for monorepo management.

**❄️ Snowflake Migration**
- Assisted in migrating all **Data Science Python algorithms** to **Snowflake**.
- Leveraged the migration to refactor and optimize existing Python projects, improving performance and maintainability.

**🪐 JupyterHub Deployment**
- Deployed a **JupyterHub server** on Kubernetes, providing Data Scientists with secure access to their notebook sessions.
- Each user session ran in a dedicated Kubernetes pod with custom resource allocation.
- Implemented a **Keycloak-based authentication system** to prevent unauthorized access.

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
