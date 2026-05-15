# GCP-VertexAI-Multimodal-Agents
Despliegue y pruebas funcionales de agentes de Inteligencia Artificial Generativa y Prompt Engineering Multimodal en entornos cloud.
# Deployment of Multimodal AI Agents with Vertex AI

## Project Description
This repository contains the architecture, development, and cloud deployment of a Multimodal Generative AI Agent utilizing **Google Cloud Platform (GCP)** and **Vertex AI**. The system processes, analyzes, and executes logical operations across multiple data input formats (Text, Image, Video, and Voice) in an automated pipeline.

## Technical Stack
*   **Core Language:** Python 3.10+ (Pandas, NumPy)
*   **Cloud Services:** GCP Vertex AI Studio, Vertex AI Feature Store, Cloud Storage
*   **Data Warehouse:** Google BigQuery & BigQuery ML (BQML)
*   **Infrastructure & Security:** GCP IAM (Custom Roles & Service Accounts), Linux (Bash)
*   **Validation Environment:** Jupyter Lab / Notebooks

##  Core Architecture & Features
1.  **Multimodal Query Processing:** Implements native logic pipelines to interpret and process parallel multi-channel data inputs.
2.  **Production-Ready API Integration:** Deploys functional cloud endpoints to establish secure external connections with the AI agent.
3.  **Principle of Least Privilege Security:** Strict access control structure leveraging delegated service accounts and custom IAM roles to mitigate cloud infrastructure risks.
4.  **In-Database Machine Learning:** Utilizes BQML scripts to run predictive analysis directly on data storage layers without moving massive tables.

##  Installation & Deployment
To mirror this environment locally or execute it inside your GCP Cloud Shell terminal, run the following commands:

```bash
# Clone the repository
git clone https://github.com

# Navigate to the project root directory
cd GCP-VertexAI-Multimodal-Agents

# Install core dependencies
pip install -r requirements.txt
```

## Responsible AI Compliance
This project enforces **Responsible AI Frameworks**, ensuring rigorous bias detection, strict data privacy controls for structured inputs, and transparency logging on all generated agent outputs.
