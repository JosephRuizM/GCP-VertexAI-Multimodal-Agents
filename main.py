import os
from google.cloud import aiplatform
import vertexai
from vertexai.generative_models import GenerativeModel, Part


def initialize_vertex_ai(project_id: str, location: str):
    """Initializes the official Google Cloud Vertex AI SDK environment."""
    vertexai.init(project=project_id, location=location)
    print(f"[INFO] Vertex AI successfully connected to project: {project_id}")


def execute_multimodal_analysis(bucket_uri: str, user_prompt: str) -> str:
    """Executes requests leveraging standard Gemini 1.5 Flash endpoints."""

    model = GenerativeModel("gemini-1.5-flash")

    video_asset = Part.from_uri(bucket_uri, mime_type="video/mp4")

    print("[INFO] Submitting multimodal payload to Google Cloud servers...")
    response = model.generate_content([video_asset, user_prompt])
    return response.text


if __name__ == "__main__":
    GCP_PROJECT = os.getenv("GCP_PROJECT_ID", "una-academic-project-42")
    GCP_LOCATION = os.getenv("GCP_REGION", "us-central1")
    DATA_PATH = "gs://corporate-inventory-vault/operations_log.mp4"
    QUERY = "Analyze operational data and highlight processing discrepancies."

    initialize_vertex_ai(GCP_PROJECT, GCP_LOCATION)
