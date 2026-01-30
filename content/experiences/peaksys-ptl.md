---
title: Tech Lead MLops at Peaksys
description: July 2022 -> December 2025. Platform Tech lead for the AI team at Peaksys.
---
# Tech Lead MLops at Peaksys

MLops is about managing and automating the ML model lifecycle.
As Platform tech lead, I mentored other team members and built ML pipelines, was responsible for technical decisions, and ensured the quality of our assets.

## Key achievements

- Deployed on premise models on Kubernetes with constrained resources (few GPUs).
  The models were deployed with Text Generation Inference (for LLM) or Triton Inference Server (for other models, like CLIP).
  Deployment was managed with a custom Helm chart.
  To give access to all our models with a unique endpoint and a simple routing system, I deployed a Traefik proxy in front of them.
  This proxy acted as an AI Gateway.
- Deployed an MLflow server on our Kubernetes cluster. 
  Then, developed an OIDC authentication plugin to secure the MLflow instance with our internal Keycloak.
- Built a CI/CD pipelines for ML models training and fast experimentation.
- Managed Azure OpenAI (now known as Azure AI Foundry) models. 
  Those deployments were used by the whole company for miscellaneous AI projects (both internal and external).
  At the beginning, manually, then with an APIOps pipeline.
- Developed a RAG chatbot with Langchain
- Conducted R&D over MCP and multi-agnt architecture in python (a2a-sdk).
- Animated coding dojos about Langchain and Langraph
- Developing an AI workflow to improve the quality of our product titles and descriptions.


## Other responsibilities

- Helping with Machine Learning Engineer recruitment (conduction interviews) and onboarding.
- Reporting and presentations to the management. Breaking down technical concepts and explaining them to non-technical people.

