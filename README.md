# 🍟 USD_FRY Protocol

**Decentralized liquidity rails for processing trading wreckage**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Solidity 0.8.19](https://img.shields.io/badge/solidity-0.8.19-blue.svg)](https://soliditylang.org/)
[![Deployed](https://img.shields.io/badge/deployed-Arbitrum%20Mainnet-green.svg)](https://arbiscan.io/address/0x492397d5912C016F49768fBc942d894687c5fe33)

🌐 **[Live Demo](https://aidanduffy68-prog.github.io/USD_FRY/)** | 📊 **[Contracts](https://arbiscan.io/address/0x492397d5912C016F49768fBc942d894687c5fe33)**

---

## 🚀 Live on Arbitrum Mainnet

**Deployed October 11, 2025**

```
USD_FRY Token:               0x492397d5912C016F49768fBc942d894687c5fe33
WreckageProcessorWithOracle: 0xf97E890aDf8968256225060e8744a797954C33CF
FRYPredictionMarket:         0xdF0B798E51d5149fE97D57fbBc8D6A8A0756204e
```

**Chainlink Oracles:**
- BTC/USD: `0x6ce185860a4963106506C203335A2910413708e9`
- ETH/USD: `0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612`

[View on Arbiscan →](https://arbiscan.io/address/0x492397d5912C016F49768fBc942d894687c5fe33)

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

USD_FRY processes trading losses into FRY tokens through Chainlink-verified prices and decentralized liquidity rails. Launched October 9, 2024 - one day before the $19B liquidation event that validated the thesis.

### What It Does
- **Process Wreckage**: Convert trading losses → FRY tokens (2.26x rate)
- **Chainlink Oracles**: Verifiable, tamper-proof price feeds
- **Prediction Markets**: Auto-resolving markets with Chainlink data
- **Decentralized**: No single point of failure (unlike centralized exchanges)

### October 10, 2024
- **$19B liquidations** (largest in history)
- **1.6M traders** affected
- **Centralized systems failed** (Binance/Wintermute rumors)
- **FRY's thesis validated**: Need for decentralized liquidity alternatives

### Tech Stack
- **Smart Contracts**: Solidity 0.8.19, OpenZeppelin, Hardhat
- **Oracles**: Chainlink Price Feeds (BTC/USD, ETH/USD)
- **Network**: Arbitrum Mainnet (low fees, high performance)
- **Frontend**: Interactive demo with Web3 integration

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

### Use the Protocol
1. Visit [Live Demo](https://aidanduffy68-prog.github.io/USD_FRY/)
2. Connect wallet (Arbitrum mainnet)
3. Process wreckage or bet on prediction markets

### Deploy Contracts
```bash
cd liquidity-rails/core/contracts
npm install
npm run deploy:mainnet
```

---

## Architecture

### Core Components

1. **WreckageProcessorWithOracle** - Processes losses with Chainlink-verified prices
2. **FRYPredictionMarket** - Auto-resolving prediction markets
3. **USD_FRY Token** - ERC20 token minted from processed wreckage

### How It Works

```
Trading Loss → Chainlink Price Verification → FRY Minting (2.26x) → Tradeable Token
```

### Prediction Markets
- Create markets about crypto prices, events, etc.
- Bet with USDC
- Auto-resolve using Chainlink oracles
- Losers receive FRY tokens (2.26x their loss)
- Winners receive 70% of losing pool

---

## Use Cases

**For Traders Who Lost Money:**
- Process your Oct 10 losses into FRY tokens
- Get 2.26x rate on verified losses
- Join community of 1.6M affected traders

**For Prediction Market Users:**
- Bet on crypto price movements
- Auto-resolution via Chainlink (no disputes)
- Even if you lose, get FRY tokens

**For DeFi Builders:**
- Integrate FRY as liquidation insurance
- Use Chainlink-verified wreckage processing
- Build on decentralized liquidity infrastructure

---

## Status

**Network**: Arbitrum Mainnet  
**Launched**: October 11, 2025  
**Contracts**: Verified on Arbiscan (pending)  
**Demo**: [Live](https://aidanduffy68-prog.github.io/USD_FRY/)

### Next Steps
- [ ] Verify contracts on Arbiscan
- [ ] Update demo with mainnet addresses
- [ ] User acquisition campaign
- [ ] Integration with zkLighter

Built for traders who lose money. Because centralized systems fail.

For questions or partnerships, open an issue. 🍟
