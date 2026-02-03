---
title: Tech Lead MLops at [Peaksys](https://www.linkedin.com/company/peaksys/posts/?feedView=all)
description: |
  Deploying the MLOps approach, designing and building a scalable AI/ML platform, 
  hiring and mentoring python developers, making code reviews and technical choices, R&D.
  
  - Deployed MLflow as a model registry, developed a python client and CICD pipelines
  - Deployed LLMs and embedding models both on Azure and on-premise (with TGI and Triton Inference Server)
  - Developed a RAG application with FastAPI/Langchain/PgVector
  - Prototyping AI multi-agent architecture with Langchain, Langgraph, a2a-sdk and mcp
image: "content/assets/images/python-logo.png"
weight: 40
skills:
  - name: Python
  - name: Python Data Science libraries
    details: |
      Most of our Data Science jobs are based on pandas, numpy, scikit-learn, and other libraries.
      At the end of my mission, I also tested polars as an alternative to pandas.
      This library is faster than pandas, uses less memory and is easier to use.
  - name: Docker
  - name: Azure AI Foundry
    details: |
      Azure AI Foundry (previously AzureOpenAI) is a service that allows you to deploy and manage LLM models endpoint.
      Most of the model we used on this platform was OpenAI models.
      
      Managing model deployments manually was time-consuming and error-prone. 
      That's why we developed an APIOps pipeline to automate the deployment process.
      
      We also used Azure API Management (APIM) to provide a better user experience and to manage the access to our models.
  - name: Golang
    details: |
      I used Golang to build some automation tools, for instance:
      
      - A scanner to audit all the Jobs and CronJob deployed on our Kubernetes cluster (more than 100 jobs).
      - A MCP server for VS code and Cursor able to interact with our Confluence knowledge base.
  - name: Kubernetes
    details: |
      Kubernetes is the backbone of the company's IT infrastructure.
      Everything, from all dot net microservices to ML inference jobs, runs there.
      
      A dedicated devops team was responsible for the maintainance of the Kubernetes cluster.
      However, I've often had to dive into the cluster to troubleshoot issues or tackle complex and custom deployments.
  - name: Helm
    details: |
      At some moments, Helm became both my main work tool and my best friend.
      Deploying a complex application without Helm is a nightmare.
      
      Some examples:
      
      - Deploying on-premise LLM endpoints with Text Generation Inference (A HuggingFace's open source solution) with GPU acceleration
      - Deploying an embedding model using Triton Inference Server, a Nvidia's project for model serving.
  - name: Hexagonal Architecture
  - name: Clean architecture
  - name: Pair & Mob Programming
  - name: Argo Workflows
  - name: FastAPI
    details: |
      All the microservices we developed were based on FastAPI:
      
      - Chatbots
      - A LLM evaluation API (based on Lamaindex)
      - Prototype of a multi-agent architecture with Deep Agents
  - name: Snowflake
    details: |
      Snowflake is the company's main Datalake solution.
      A DataOps team is responsible for the maintenance of our data warehouse.
      
      As AI team, we used Snowflake for:
      
      - maintaining the Python assets the entier company use to connect with Snowflake (python library, authentication APIs...)
      - building a python library that helps Python Developers and Data Scientists to use Snowflake as a vector database
  - name: Nvidia GPUs
  - name: OIDC & Oauth2
    details: |
      At Peaksys, even a simple internal application must be secured with OIDC.
      A dedicated team was responsible for deploying and maintaining a Keycloak instance.
      However, this team wasn't responsible for developping the plateforms-specific components to connect to Keycloak.
      
      Thus, we had to develop:
      
      - An OIDC plugin for MLflow
      - Prototype to connect MCP server with OIDC
  - name: Code performance optimization
  - name: Linux & Bash
  - name: Git
  - name: Prometheus PromQL & Grafana
    details: |
      Create custom Grafana dashboards to monitor our platform and our deployed models.
  - name: Azure DevOps YAML pipelines
    details: |
      Developing custom CICD pipelines for both the team's needs and the Data Science team's needs.
      For instance:
      
      - Developing custom CI/CD pipelines for TGI and Triton Inference Server deployments.
      - Building a CI/CD pipeline to help Data Scientist with Deep Learning model training on our GPU infrastructure
      - Deploying Helm chart for our platform's credential management.
  - name: Technical conception
  - name: Machine Learning
    details: |
      Even though I didn't have to train ML models in my daily job, I needed to have a good understanding of the ML field.
      I [completed a training course](https://www.linkedin.com/in/thomas-marquis-contact/details/certifications/) provided by DataScientest about ML.
      I also learnt from myself for years. Machine Learning and AI are subjects I'm very passionate about.
  - name: MLflow
    
  - name: Behave
  - name: Streamlit
    details: |
      All the team members were familiar with Streamlit to quickly develop prototypes or internal tools.
      
      Some of the use case I've personally developed with Streamlit in the AI team:
      - A chatbot interface for a RAG application (as a prototype to showcase the project and helps with local development)
      - A user interface secured with OIDC and deployed on Kubernets that allows user to manage their personal secret key for Snwoflake.
      
      And, you've probably noticed it already, this website you're currently reading is also developed with Streamlit!
  - name: Langchain / Langgraph / Deep Agents
    details: |
      There's a lot of to write about this topics!
      
      Let's just give some examples where I used this awsome stack:
      
      - Developing a RAG chatbot for FAQ
      - Prototyping of a multi-agent architecture with Deep Agents and a2a-sdk, with OIDC authentication
      - Animating coding dojos to help MLE getting familiar with these libraries
  - name: TDD (Test-Driven Development)
period:
  from: 2022-07
  to: 2025-12
  format: "%Y-%m"
location: Bordeaux, France
---
# Tech Lead MLops at Peaksys

## Context

MLops is about managing and automating the ML model lifecycle:
- training
- model artifact storage, traceability, and versioning
- deployment and inference
- monitoring and alerting (e.g. drift detection)
- retraining

By ML model, we mean:
- "classical" machine learning models (e.g. Scikit-Learn-based models, XGBoost, etc.)
- Deep learning models (e.g. PyTorch, TensorFlow, etc.)
- LLM and embedding models (e.g. lib transformers, Hugging Face open-weight models, etc.)

## About the team and my responsibilities

The AI team (aka "CT-IA") was a platform team. Our mission was to build a scalable AI/ML platform that helps all other company's teams to build their own AI/ML products.
Our "clients" were:
- the **Data Scientists** teams, providing them with tools to train, deploy, and manage their models
- the **Machine Learning Engineers**: python developers who work with Data Scientists to industrialize their python code.
- the **IT teams**, providing them with production-ready LLM endpoints (both on-premise and in the cloud)

This team was composed of:
- A manager
- A Platform Owner (PO); Which is the equivalent of a Product Owner
- 3 MLops Engineers
- A Platform Tech Lead

As Platform tech lead, I was responsible for:
- Making technical decisions about the architecture of our platform
- Contributing to the development and the run of our platform
- Ensuring the quality of our assets
- Conducting R&D projects and technical monitoring
- In collaboration with the PO, building the roadmap of the platform
- Mentoring the other team members as well as the Machine Learning Engineers (MLE)
- Contributing to the MLE hiring process and their onboarding

## Key achievements

**✨ On-premise LLMS**

- Deployed on premise models on Kubernetes with constrained resources (few GPUs).
  The models were deployed with Text Generation Inference (for LLM) or Triton Inference Server (for other models, like CLIP).
  Deployment was managed with a custom Helm chart.
  To give access to all our models with a unique endpoint and a simple routing system, I deployed a Traefik proxy in front of them.
  This proxy acted as an AI Gateway.

**🧩 MLflow**
- Deployed an MLflow server on our Kubernetes cluster. 
  Then, developed an OIDC authentication plugin to secure the MLflow instance with our internal Keycloak.

**⛓ CICD pipelines**
- Built a CI/CD pipelines for ML models training and fast experimentation.

**☁️ Azure AI Foundry**
- Managed Azure OpenAI (now known as Azure AI Foundry) models. 
  Those deployments were used by the whole company for miscellaneous AI projects (both internal and external).
  At the beginning, manually, then with an APIOps pipeline.

**💬 Chatbot**
- Developed a RAG chatbot with Langchain

**🔬 R&D**
- Conducted R&D over MCP and multi-agnt architecture in python (a2a-sdk).

**📢 Mentoring and sharing**
- Animated coding dojos about Langchain and Langraph

**🪄 AI workflow development**
- Developing an AI workflow to improve the quality of our product titles and descriptions.


## Other responsibilities

- Helping with Machine Learning Engineer recruitment (conduction interviews) and onboarding.
- Reporting and presentations to the management. Breaking down technical concepts and explaining them to non-technical people.

## About Peaksys

Peaksys is the IT subsidiary of the Cnova Group. This group also owns Cdisocunt, a famous e-commerce platform in France, as well as tow other specialized companies:

- C-Logistics, that ensures shipments and logistics solutions
- Octopia, that provides a Marketplace-as-a-service solution

The Peaksys's customers are the other subsidiaries of Cnova Group.

![Cnova structure](../assets/images/cnova-graph.png)

