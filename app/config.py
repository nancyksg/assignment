from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration settings.
    Values can be overridden using environment variables.
    """

    APP_NAME: str = "Geo Services API"
    VERSION: str = "0.1.0"

    # Database configuration (conceptual for this assignment)
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/geodb"

    # Azure OpenAI configuration
    AZURE_OPENAI_ENDPOINT: str = "https://your-openai-resource.openai.azure.com/"
    AZURE_OPENAI_API_KEY: str = "your-api-key"
    AZURE_OPENAI_MODEL: str = "gpt-4o"

    # Agent configuration
    AGENT_MAX_TOKENS: int = 1000
    AGENT_TEMPERATURE: float = 0.2

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
