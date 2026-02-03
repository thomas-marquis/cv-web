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
  - name: Python Data Science Libraries
    details: |
      Most of our Data Science projects relied on libraries such as pandas, numpy, scikit-learn, and others.
  - name: Docker
  - name: Kubernetes
  - name: Helm
  - name: Hexagonal Architecture
  - name: Pair & Mob Programming
  - name: Argo Workflows
  - name: FastAPI
  - name: Snowflake
  - name: OIDC & OAuth2
  - name: Code Performance Optimization
  - name: Linux & Bash
  - name: Git
  - name: Prometheus PromQL & Grafana
  - name: Azure DevOps YAML Pipelines
  - name: Technical Design
  - name: User Interviews
  - name: Behave
  - name: Clean Architecture
  - name: TDD (Test-Driven Development)
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
