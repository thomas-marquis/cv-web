---
title: Tech Lead MLops at Peaksys
description: July 2022 -> December 2025. Platform Tech lead for the AI team at Peaksys.
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
  - name: Golang
  - name: Kubernetes
  - name: Helm
  - name: Hexagonal Architecture
  - name: Pair & Mob Programming
  - name: Argo Workflows
  - name: FastAPI
  - name: Snowflake
  - name: Nvidia GPUs
  - name: OIDC & Oauth2
  - name: Code performance optimization
  - name: Linux & Bash
  - name: Git
  - name: Prometheus PromQL & Grafana
  - name: Azure DevOps YAML pipelines
  - name: Technical conception
  - name: Machine Learning
  - name: MLflow
  - name: Clean architecture
  - name: Behave
  - name: Streamlit
  - name: Langchain / Langgraph / Deep Agents
period:
  from: 2022-07
  to: 2025-12
  format: %Y-%m
location: Bordeaux, France
---
# Tech Lead MLops at Peaksys

MLops is about managing and automating the ML model lifecycle.
As Platform tech lead, I mentored other team members and built ML pipelines, was responsible for technical decisions, and ensured the quality of our assets.

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

## Focus

