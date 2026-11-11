
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    app_name: str = "Production-Grade Agentic RAG System"
    app_env: str = "development"

    # OpenRouter configuration
    openrouter_api_key: str = ""
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_model: str = "openai/gpt-4o-mini"

    tavily_api_key: str = ""
    pinecone_api_key: str = ""

    pinecone_index_name: str = "production-it-support-rag"
    pinecone_namespace: str = "company-it-kb"

    embedding_model: str = "text-embedding-3-small"

    top_k: int = 4
    max_retries: int = 1

    admin_api_key: str = "change-me"

    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    upload_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
