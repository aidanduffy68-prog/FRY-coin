#!/bin/bash
# FRY Smart Contract Deployment Script
# Deploy to Arbitrum Sepolia testnet

set -e

echo "🍟 FRY Smart Contract Deployment"
echo "=================================="
echo ""

# Check if Hardhat is installed
if ! command -v npx &> /dev/null; then
    echo "❌ npx not found. Installing Node.js dependencies..."
    npm install --save-dev hardhat @nomiclabs/hardhat-ethers ethers
fi

# Create Hardhat project structure if needed
if [ ! -f "hardhat.config.js" ]; then
    echo "📦 Initializing Hardhat project..."
    
    cat > hardhat.config.js << 'EOF'
require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    arbitrumSepolia: {
      url: process.env.ARBITRUM_SEPOLIA_RPC || "https://sepolia-rollup.arbitrum.io/rpc",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 421614
    },
    arbitrum: {
      url: process.env.ARBITRUM_RPC || "https://arb1.arbitrum.io/rpc",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 42161
    }
  }
};
EOF
    
    echo "✓ Hardhat config created"
fi

# Create deployment script
mkdir -p scripts

cat > scripts/deploy_fry_system.js << 'EOF'
const hre = require("hardhat");

async function main() {
  console.log("🍟 Deploying FRY System Contracts...\n");
  
  // Get deployer
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying with account:", deployer.address);
  console.log("Account balance:", (await deployer.getBalance()).toString(), "\n");
  
  // 1. Deploy AgentBVerifier
  console.log("1. Deploying AgentBVerifier...");
  const AgentBVerifier = await hre.ethers.getContractFactory("AgentBVerifier");
  const agentBVerifier = await AgentBVerifier.deploy();
  await agentBVerifier.deployed();
  console.log("✓ AgentBVerifier deployed to:", agentBVerifier.address);
  
  // 2. Deploy ConfidentialPositionVerifier
  console.log("\n2. Deploying ConfidentialPositionVerifier...");
  const ConfidentialPositionVerifier = await hre.ethers.getContractFactory("ConfidentialPositionVerifier");
  const positionVerifier = await ConfidentialPositionVerifier.deploy();
  await positionVerifier.deployed();
  console.log("✓ ConfidentialPositionVerifier deployed to:", positionVerifier.address);
  
  // Save deployment addresses
  const deployment = {
    network: hre.network.name,
    chainId: hre.network.config.chainId,
    deployer: deployer.address,
    timestamp: new Date().toISOString(),
    contracts: {
      AgentBVerifier: agentBVerifier.address,
      ConfidentialPositionVerifier: positionVerifier.address
    }
  };
  
  const fs = require('fs');
  fs.writeFileSync(
    'deployment_addresses.json',
    JSON.stringify(deployment, null, 2)
  );
  
  console.log("\n✓ Deployment complete!");
  console.log("Addresses saved to deployment_addresses.json");
  
  console.log("\n🍟 FRY System Deployed Successfully 🍟");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
EOF

echo "✓ Deployment script created"
echo ""

# Check for environment variables
if [ -z "$PRIVATE_KEY" ]; then
    echo "⚠️  PRIVATE_KEY not set"
    echo "   Export your private key: export PRIVATE_KEY=0x..."
    echo ""
fi

if [ -z "$ARBITRUM_SEPOLIA_RPC" ]; then
    echo "ℹ️  Using default Arbitrum Sepolia RPC"
    echo "   Override with: export ARBITRUM_SEPOLIA_RPC=https://..."
    echo ""
fi

echo "📋 Deployment Checklist:"
echo "  [ ] Set PRIVATE_KEY environment variable"
echo "  [ ] Fund deployer address with Sepolia ETH"
echo "  [ ] Review contract code (AgentBVerifier.sol, ConfidentialPositionVerifier.sol)"
echo "  [ ] Run: npm install"
echo "  [ ] Run: npx hardhat compile"
echo "  [ ] Run: npx hardhat run scripts/deploy_fry_system.js --network arbitrumSepolia"
echo ""

echo "🚀 Ready to deploy!"
echo ""
echo "Commands:"
echo "  # Compile contracts"
echo "  npx hardhat compile"
echo ""
echo "  # Deploy to testnet"
echo "  npx hardhat run scripts/deploy_fry_system.js --network arbitrumSepolia"
echo ""
echo "  # Deploy to mainnet (when ready)"
echo "  npx hardhat run scripts/deploy_fry_system.js --network arbitrum"
echo ""
