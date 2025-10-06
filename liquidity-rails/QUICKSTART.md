# USD_FRY Protocol - Quick Start Guide

## Prerequisites

- Python 3.8+
- pip package manager
- (Optional) Virtual environment

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/aidanduffy68-prog/USD_FRY.git
cd USD_FRY/liquidity-rails
```

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: EZKL (zkML library) requires separate installation:
```bash
pip install ezkl==22.2.1
```

If EZKL installation fails, the system will fall back to simulation mode.

## Running the System

### Start the API Server

```bash
cd core/api
python fry_api.py
```

Or with uvicorn:
```bash
uvicorn fry_api:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

### Run System Tests

```bash
cd core/tests
python test_complete_system.py
```

### Run the Live Demo

```bash
python demo_live_system.py
```

This will simulate 10 wreckage events and show real-time USD_FRY minting.

## API Endpoints

### Submit Wreckage

```bash
curl -X POST http://localhost:8000/wreckage/submit \
  -H "Content-Type: application/json" \
  -d '{
    "dex": "Hyperliquid",
    "wreckage_type": "long_liq",
    "asset": "BTC",
    "amount_usd": 50000,
    "stablecoin": "USDH"
  }'
```

### Get System Health

```bash
curl http://localhost:8000/system/health
```

### Get Liquidity Summary

```bash
curl http://localhost:8000/liquidity/summary
```

### Get Current Minting Rate

```bash
curl http://localhost:8000/fry/minting-rate
```

## Project Structure

```
liquidity-rails/
├── core/
│   ├── api/              # FastAPI server
│   ├── engines/          # Core routing engines
│   │   ├── routing/      # Liquidity rails
│   │   ├── matching/     # P2P matching
│   │   └── ml/           # Machine learning
│   ├── contracts/        # Solidity smart contracts
│   ├── privacy/          # zkML & Pedersen commitments
│   ├── federated/        # Federated learning
│   └── tests/            # Test files
├── docs/                 # Documentation
├── examples/             # Example scripts
└── requirements.txt      # Python dependencies
```

## Key Components

### 1. Liquidity Rails Engine
Routes wreckage through optimal paths across DEX venues.

```python
from core.engines.routing.liquidity_rails_engine import LiquidityRailsEngine

engine = LiquidityRailsEngine()
result = engine.route_wreckage(amount_usd=100000, asset="BTC", max_hops=3)
```

### 2. Wreckage Matching Engine
P2P matching for offsetting funding rate positions.

```python
from core.engines.matching.fry_wreckage_matching_engine import WreckageMatchingEngine

matcher = WreckageMatchingEngine()
match = matcher.submit_wreckage(wreckage_event)
```

### 3. Agent B Market Maker
AI-driven market making with adaptive hedging.

```python
from core.engines.agent_b_core import AgentB

agent = AgentB()
hedge_ratio = agent.calculate_hedge_ratio(position, market_data)
```

## Configuration

### Environment Variables

Create a `.env` file in the `liquidity-rails/` directory:

```bash
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# DEX API Keys (optional for live data)
BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here

# zkML Configuration
EZKL_ENABLED=true
EZKL_PROOF_THRESHOLD=0.05

# Logging
LOG_LEVEL=INFO
```

## Troubleshooting

### Import Errors

If you get import errors, make sure you're in the correct directory:

```bash
cd liquidity-rails
export PYTHONPATH="${PYTHONPATH}:$(pwd)/core"
```

### EZKL Installation Issues

EZKL requires Rust. If installation fails:

1. Install Rust: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
2. Try again: `pip install ezkl==22.2.1`
3. Or run without zkML (simulation mode will be used)

### Port Already in Use

If port 8000 is in use:

```bash
uvicorn fry_api:app --port 8001
```

## Next Steps

1. **Deploy Smart Contracts**: See `core/contracts/README.md`
2. **Run Federated Learning**: See `core/federated/README.md`
3. **Integrate with DEX**: See API documentation
4. **Read the Whitepaper**: See `docs/FRY_TECHNICAL_WHITEPAPER.md`

## Support

- GitHub Issues: https://github.com/aidanduffy68-prog/USD_FRY/issues
- Documentation: `docs/`
- API Docs: http://localhost:8000/docs (when server is running)

## License

MIT License - See LICENSE file for details

---

**Built for Native Stablecoin DEXes | Powered by Wreckage Absorption**
