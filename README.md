# 🍟 USD_FRY - Liquidity Rails for Wreckage Absorption

**Production-ready DeFi infrastructure for native stablecoin DEXes**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Solidity 0.8.19](https://img.shields.io/badge/solidity-0.8.19-blue.svg)](https://soliditylang.org/)
[![Deployed](https://img.shields.io/badge/deployed-Arbitrum%20Sepolia-blue.svg)](https://sepolia.arbiscan.io/address/0xB6Ce342D32cEf47bb316f5d2f7c2b39b00916eE0)

🌐 **[Live Demo](https://aidanduffy68-prog.github.io/USD_FRY/)** | 📄 **[Whitepaper](liquidity-rails/docs/FRY_TECHNICAL_WHITEPAPER.md)** | 📝 **[Mirror Article](liquidity-rails/docs/FRY_MIRROR_ARTICLE.md)**

---

## 🚀 Deployed on Arbitrum Sepolia Testnet

**Live Smart Contracts:**
```
USDFRYToken:                    0xB6Ce342D32cEf47bb316f5d2f7c2b39b00916eE0
AgentBVerifier:                 0x859fe6A2BD2bBF62A0f526F3d11e85C60A617060
ConfidentialPositionVerifier:   0xfdB84Ab8907D8e8d9Bf81BeD078240d72437D697
LiquidityRailsRouter:           0x2C93031141C3284FbccD4b8d1Ac0b8C60a174E23
WreckageMatchingPool:           0xFB3EB4E31f05097145Fb883ddAC14c528Fe13785
```

[View on Arbiscan →](https://sepolia.arbiscan.io/address/0xB6Ce342D32cEf47bb316f5d2f7c2b39b00916eE0)

---

## 📘 [Read the Technical Whitepaper](liquidity-rails/docs/FRY_TECHNICAL_WHITEPAPER.md)

**Start here** - Complete technical specification covering system architecture, routing algorithms, privacy layer, economic model, and deployment guide.

---

## Quick Links

- **[Technical Whitepaper](liquidity-rails/docs/FRY_TECHNICAL_WHITEPAPER.md)** - THE BIBLE
- **[Quick Start](liquidity-rails/docs/QUICK_START.md)** - Get running in 5 minutes
- **[System Summary](liquidity-rails/docs/SYSTEM_SUMMARY.md)** - High-level overview
- **[Deployment Guide](liquidity-rails/docs/DEPLOYMENT_GUIDE.md)** - Production deployment

---

## Overview

USD_FRY converts trading losses (wreckage) into productive assets through optimal routing, peer-to-peer matching, and AI-driven market making. Built specifically for native stablecoin DEXes (Hyperliquid USDH, Aster USDF).

### Key Metrics
- **FRY Minting**: 2.26 per $1 (vs 0.5 base rate)
- **Capital Efficiency**: 7.4x via native token denomination
- **Volatility Reduction**: 61.5% in funding rates
- **ML Enhancement**: +11% hedge optimization
- **System Improvement**: 221% over base rate

### Tech Stack
- **Smart Contracts**: Solidity 0.8.19, OpenZeppelin, Hardhat
- **Backend**: Python, FastAPI, ethers.js
- **ML/Privacy**: PyTorch, EZKL (zkML), Pedersen commitments
- **Deployment**: Arbitrum Sepolia (testnet), ready for mainnet

---

## Project Structure

```
liquidity-rails/
├── core/
│   ├── engines/        # Routing, matching, ML, visualization
│   ├── privacy/        # zkML & confidential positions
│   ├── federated/      # Distributed learning
│   ├── api/            # REST API server
│   ├── contracts/      # Smart contracts
│   └── tests/          # Test suite
├── docs/               # Documentation
├── scripts/            # Deployment scripts
└── examples/           # Usage examples
```

---

## Quick Start

```bash
cd liquidity-rails
pip install -r requirements.txt

# Start API server
python core/api/fry_api.py

# Run tests
python core/tests/test_complete_system.py
```

---

## Architecture

### Three-Tier Routing System

1. **P2P Matching** (1.4 FRY/$1) - Cash-settled funding rate swaps
2. **Liquidity Rails** (1.2-2.2 FRY/$1) - Multi-hop routing with ML optimization
3. **Agent B Market Maker** (0.8-1.0 FRY/$1) - AI-enhanced fallback

### Core Components

- **Liquidity Rails Engine** - Optimal routing across DEXes
- **Wreckage Matching Engine** - P2P funding swaps
- **Agent B** - ML-enhanced market making
- **zkML Privacy Layer** - EZKL proofs + Pedersen commitments
- **Smart Contracts** - On-chain minting and verification

---

## Use Cases

**For DEXes:**
- Reduce LP losses via wreckage recycling
- 7.4x capital efficiency improvement
- Stabilize funding rates (-61.5% volatility)

**For Market Makers:**
- Convert losses into FRY tokens
- Access optimal liquidity routes
- ML-enhanced hedging (+11% performance)

**For Liquidity Providers:**
- Earn FRY from liquidity provision
- Reduced impermanent loss
- Confidential position tracking

---

## Built by Liquidity Engineers 🛤️

**Status**: Production Ready  
**Version**: 1.0.0  
**Code**: 16,313 lines  
**Deployed**: Arbitrum Sepolia Testnet

Built for [Hyperliquid](https://hyperliquid.xyz) and [Aster Protocol](https://aster.xyz)

For questions or partnerships, open an issue.
