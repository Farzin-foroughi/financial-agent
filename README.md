# Financial Agent

This project is a LangGraph agent that can provide financial analysis based on the latest prices of gold, USD, and Bitcoin.

## Architecture

The agent is built using LangGraph and is structured as follows:

- **`app.py`**: The main entry point of the application. It builds the graph and invokes it with a sample question.
- **`graph/`**: This directory contains the core logic of the LangGraph agent.
  - **`graph.py`**: Defines the graph structure, connecting all the nodes and edges.
  - **`nodes.py`**: Contains the logic for each node in the graph, including intent detection, data collection, and analysis.
  - **`router.py`**: Implements the routing logic to direct the flow of the graph based on the detected intent.
  - **`state.py`**: Defines the state object that is passed between the nodes in the graph.
- **`tools/`**: This directory contains the tools that the agent can use to collect data.
  - **`gold.py`**: A tool to fetch the latest price of gold.
  - **`usd.py`**: A tool to fetch the latest price of USD.
  - **`btc.py`**: A tool to fetch the latest price of Bitcoin.
- **`api/`**: This directory contains the FastAPI server that exposes the agent as an API.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd financial-agent
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the environment variables:**
   - The agent uses the OpenAI API for analysis. You need to set your OpenAI API key as an environment variable:
     ```bash
     export OPENAI_API_KEY="your-openai-api-key"
     ```
   - The USD tool attempts to fetch the exchange rate from a public API. If the API does not support IRR, you can provide a fallback value using an environment variable:
      ```bash
      export USD_TO_TOMAN="120000"
      ```

## Usage

### Running the Agent

To run the agent directly, you can execute the `app.py` script:

```bash
python app.py
```

This will run the agent with a sample question and print the analysis to the console.

### Running the API Server

To run the API server, you can use `uvicorn`:

```bash
uvicorn api.main:app --reload
```

The API will be available at `http://localhost:8000`. You can send a POST request to the `/analyze` endpoint with a JSON body containing the question:

```json
{
  "question": "یک تحلیل اقتصادی بده"
}
```

The API will return a JSON response containing the analysis.
