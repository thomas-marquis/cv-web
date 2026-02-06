---
title: Tech Lead MLOps at [Peaksys](https://www.linkedin.com/company/peaksys/posts/?feedView=all)
description: |
  Deploying the MLOps approach, designing and building a scalable AI/ML platform,
  hiring and mentoring Python developers, conducting code reviews, and making technical decisions.
  Engaging in R&D to explore innovative solutions.

  - Deployed MLflow as a model registry, developed a Python client, and built CI/CD pipelines
  - Deployed LLMs and embedding models on Azure and on-premise (using TGI and Triton Inference Server)
  - Developed a RAG application with FastAPI, Langchain, and PgVector
  - Prototyped AI multi-agent architecture with Langchain, Langgraph, a2a-sdk, and MCP
image: "content/assets/images/python-logo.png"
weight: 40
highlighted: true
skills:
  - name: Python
  - name: Python Data Science Libraries
    details: |
      Most of our data science projects relied on libraries such as pandas, numpy, scikit-learn, and others.
      Toward the end of my mission, I also tested polars as an alternative to pandas.
      Polars is faster, uses less memory, and is easier to use compared to pandas.
  - name: Docker
  - name: Azure AI Foundry
    details: |
      Azure AI Foundry (formerly Azure OpenAI) is a service for deploying and managing LLM model endpoints.
      Most of the models we used on this platform were OpenAI models.

      Manually managing model deployments was time-consuming and prone to errors.
      To address this, we developed an APIOps pipeline to automate the deployment process.

      We also used Azure API Management (APIM) to enhance user experience and manage access to our models.
  - name: Golang
    details: |
      I used Golang to build automation tools, such as:
      - A scanner to audit all Jobs and CronJobs deployed on our Kubernetes cluster (over 100 jobs)
      - An MCP server for VS Code and Cursor, capable of interacting with our Confluence knowledge base
  - name: Kubernetes
    details: |
      Kubernetes is the backbone of the company's IT infrastructure.
      Everything, from .NET microservices to ML inference jobs, runs on Kubernetes.

      A dedicated DevOps team was responsible for maintaining the Kubernetes cluster.
      However, I often had to troubleshoot issues or handle complex and custom deployments.
  - name: Helm
    details: |
      Helm became an essential tool for deploying complex applications.
      Some examples of its use include:
      - Deploying on-premise LLM endpoints with Text Generation Inference (Hugging Face's open-source solution) with GPU acceleration
      - Deploying an embedding model using Triton Inference Server, a NVIDIA project for model serving
  - name: Hexagonal Architecture
  - name: Clean Architecture
  - name: Pair & Mob Programming
  - name: Argo Workflows
  - name: FastAPI
    details: |
      All the microservices we developed were based on FastAPI, including:
      - Chatbots
      - An LLM evaluation API (based on LlamaIndex)
      - A prototype of a multi-agent architecture with Deep Agents
  - name: Snowflake
    details: |
      Snowflake is the company's main data lake solution.
      A DataOps team was responsible for maintaining our data warehouse.

      As the AI team, we used Snowflake for:
      - Maintaining Python assets used company-wide to connect with Snowflake (Python libraries, authentication APIs, etc.)
      - Building a Python library to help developers and data scientists use Snowflake as a vector database
  - name: NVIDIA GPUs
  - name: OIDC & OAuth2
    details: |
      At Peaksys, even simple internal applications required OIDC security.
      A dedicated team managed a Keycloak instance, but we were responsible for developing platform-specific components to connect to Keycloak.

      We developed:
      - An OIDC plugin for MLflow
      - A prototype to connect the MCP server with OIDC
  - name: Code Performance Optimization
  - name: Linux & Bash
  - name: Git
  - name: JupyterHub
  - name: Azure APIM (API Management)
    details: |
      Configured and deployed an APIM instance for our Azure AI Foundry LLM endpoints.
  - name: Prometheus PromQL & Grafana
    details: |
      Created custom Grafana dashboards to monitor our platform and deployed models.
  - name: Azure DevOps YAML Pipelines
    details: |
      Developed custom CI/CD pipelines for both the team's needs and the Data Science team's requirements.
      Examples include:
      - CI/CD pipelines for TGI and Triton Inference Server deployments
      - A CI/CD pipeline to assist data scientists with deep learning model training on our GPU infrastructure
      - Deploying Helm charts for platform credential management
  - name: Technical Design
  - name: Machine Learning
    details: |
      Although I didn't train ML models daily, I needed a solid understanding of the field.
      I completed a [training course](https://www.linkedin.com/in/thomas-marquis-contact/details/certifications/) provided by DataScientest about ML.
      I also engaged in self-learning over the years, driven by my passion for machine learning and AI.
  - name: MLflow
    details: |
      Deployed a MLflow server for saving and versioning ML models.
      Developed an OIDC authentication plugin.
      Then, developed a Python client to interact with the MLflow server (on top of the mlflow library).
  - name: Behave
  - name: Streamlit
    details: |
      Our team frequently used Streamlit to quickly develop prototypes or internal tools.
      Some of my personal use cases included:
      - A chatbot interface for a RAG application (prototype to showcase the project and aid local development)
      - A user interface secured with OIDC and deployed on Kubernetes, allowing users to manage their personal secret keys for Snowflake

      This website you're currently reading is also developed with Streamlit!
  - name: Langchain / Langgraph / Deep Agents
    details: |
      There's a lot to say about these topics!
      Here are some examples of how I used this powerful stack:
      - Developing a RAG chatbot for FAQs
      - Prototyping a multi-agent architecture with Deep Agents and a2a-sdk, featuring OIDC authentication
      - Leading coding dojos to help machine learning engineers become familiar with these libraries
  - name: TDD (Test-Driven Development)
period:
  from: 2022-07
  to: 2025-12
  format: "%Y-%m"
location: Bordeaux, France
---

# Tech Lead MLOps at Peaksys

## Context

MLOps focuses on managing and automating the lifecycle of machine learning models, including:

- **Training**
- **Model artifact storage, traceability, and versioning**
- **Deployment and inference**
- **Monitoring and alerting** (e.g., drift detection)
- **Retraining**

By "ML model," we refer to:

- "Classical" machine learning models (e.g., Scikit-Learn-based models, XGBoost)
- Deep learning models (e.g., PyTorch, TensorFlow)
- LLM and embedding models (e.g., Hugging Face Transformers, open-weight models)

## About the Team and My Responsibilities

The AI team (aka "CT-IA") was a platform team. Our mission was to build a scalable AI/ML platform to support other teams
within the company in developing their AI/ML products. Our "clients" included:

- **Data Scientists**, providing tools for training, deploying, and managing models
- **Machine Learning Engineers**, Python developers collaborating with data scientists to industrialize their code
- **IT Teams**, offering production-ready LLM endpoints (both on-premise and in the cloud)

The team consisted of:

- A manager
- A Platform Owner (equivalent to a Product Owner)
- 3 MLOps engineers
- A Platform Tech Lead (myself)

As Platform Tech Lead, my responsibilities included:

- Making technical decisions about platform architecture
- Contributing to platform development and operations
- Ensuring the quality of our assets
- Conducting R&D projects and technical monitoring
- Collaborating with the Platform Owner to build the platform roadmap
- Mentoring team members and Machine Learning Engineers (MLEs)
- Participating in the MLE hiring process and onboarding

## Key Achievements

**✨ On-Premise LLMs**

- Deployed on-premise models on Kubernetes with limited GPU resources.
  Models were deployed using Text Generation Inference (for LLMs) or Triton Inference Server (for other models, such as
  CLIP).
  Deployment was managed with a custom Helm chart.
  To provide unified access to all models, I deployed a Traefik proxy as an AI Gateway.

**🧩 MLflow**

- Deployed an MLflow server on our Kubernetes cluster.
  Developed an OIDC authentication plugin to secure the MLflow instance with our internal Keycloak.

**⛓ CI/CD Pipelines**

- Built CI/CD pipelines for ML model training and rapid experimentation.

**☁️ Azure AI Foundry**

- Managed Azure OpenAI (now Azure AI Foundry) models, initially manually and later through an APIOps pipeline.
  These deployments were used company-wide for various AI projects.

**💬 Chatbot**

- Developed a RAG chatbot using Langchain.

**🔬 R&D**

- Conducted R&D on MCP and multi-agent architecture in Python (a2a-sdk).

**📢 Mentoring and Sharing**

- Led coding dojos on Langchain and Langgraph.

**🪄 AI Workflow Development**

- Developed an AI workflow to enhance the quality of product titles and descriptions.

## Other Responsibilities

- Assisted with Machine Learning Engineer recruitment (conducting interviews) and onboarding.
- Reported to management, translating technical concepts for non-technical stakeholders.

## About Peaksys

Peaksys is the IT subsidiary of the Cnova Group, which also owns:

- **Cdiscount**, a prominent e-commerce platform in France
- **C-Logistics**, providing shipment and logistics solutions
- **Octopia**, offering a Marketplace-as-a-Service solution

Peaksys's customers are the other subsidiaries of the Cnova Group.

![Cnova structure](../assets/images/cnova-graph.png)
