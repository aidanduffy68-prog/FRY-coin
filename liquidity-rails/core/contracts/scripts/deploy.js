const hre = require("hardhat");

async function main() {
  console.log("\n🍟 FRY Protocol Deployment Starting...\n");
  
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with account:", deployer.address);
  console.log("Account balance:", (await deployer.getBalance()).toString());
  console.log("Network:", hre.network.name);
  console.log("\n" + "=".repeat(70) + "\n");
  
  // 1. Deploy USD_FRY Token
  console.log("📝 Deploying USDFRYToken...");
  const USDFRYToken = await hre.ethers.getContractFactory("USDFRYToken");
  const usdFryToken = await USDFRYToken.deploy();
  await usdFryToken.deployed();
  console.log("✅ USDFRYToken deployed to:", usdFryToken.address);
  
  // 2. Deploy AgentBVerifier
  console.log("\n📝 Deploying AgentBVerifier...");
  const AgentBVerifier = await hre.ethers.getContractFactory("AgentBVerifier");
  const agentBVerifier = await AgentBVerifier.deploy();
  await agentBVerifier.deployed();
  console.log("✅ AgentBVerifier deployed to:", agentBVerifier.address);
  
  // 3. Deploy ConfidentialPositionVerifier
  console.log("\n📝 Deploying ConfidentialPositionVerifier...");
  const ConfidentialPositionVerifier = await hre.ethers.getContractFactory("ConfidentialPositionVerifier");
  const positionVerifier = await ConfidentialPositionVerifier.deploy();
  await positionVerifier.deployed();
  console.log("✅ ConfidentialPositionVerifier deployed to:", positionVerifier.address);
  
  // 4. Deploy LiquidityRailsRouter
  console.log("\n📝 Deploying LiquidityRailsRouter...");
  const LiquidityRailsRouter = await hre.ethers.getContractFactory("LiquidityRailsRouter");
  const router = await LiquidityRailsRouter.deploy(usdFryToken.address);
  await router.deployed();
  console.log("✅ LiquidityRailsRouter deployed to:", router.address);
  
  // 5. Deploy WreckageMatchingPool
  console.log("\n📝 Deploying WreckageMatchingPool...");
  const WreckageMatchingPool = await hre.ethers.getContractFactory("WreckageMatchingPool");
  const matchingPool = await WreckageMatchingPool.deploy(usdFryToken.address);
  await matchingPool.deployed();
  console.log("✅ WreckageMatchingPool deployed to:", matchingPool.address);
  
  // 6. Grant roles
  console.log("\n📝 Setting up roles...");
  
  const MINTER_ROLE = await usdFryToken.MINTER_ROLE();
  
  // Grant MINTER_ROLE to router
  await usdFryToken.grantRole(MINTER_ROLE, router.address);
  console.log("✅ Granted MINTER_ROLE to LiquidityRailsRouter");
  
  // Grant MINTER_ROLE to matching pool
  await usdFryToken.grantRole(MINTER_ROLE, matchingPool.address);
  console.log("✅ Granted MINTER_ROLE to WreckageMatchingPool");
  
  // Summary
  console.log("\n" + "=".repeat(70));
  console.log("\n🎉 Deployment Complete!\n");
  console.log("Contract Addresses:");
  console.log("-------------------");
  console.log("USDFRYToken:                   ", usdFryToken.address);
  console.log("AgentBVerifier:                ", agentBVerifier.address);
  console.log("ConfidentialPositionVerifier:  ", positionVerifier.address);
  console.log("LiquidityRailsRouter:          ", router.address);
  console.log("WreckageMatchingPool:          ", matchingPool.address);
  console.log("\n" + "=".repeat(70) + "\n");
  
  // Save deployment info
  const deploymentInfo = {
    network: hre.network.name,
    deployer: deployer.address,
    timestamp: new Date().toISOString(),
    contracts: {
      USDFRYToken: usdFryToken.address,
      AgentBVerifier: agentBVerifier.address,
      ConfidentialPositionVerifier: positionVerifier.address,
      LiquidityRailsRouter: router.address,
      WreckageMatchingPool: matchingPool.address
    }
  };
  
  const fs = require('fs');
  fs.writeFileSync(
    'deployment.json',
    JSON.stringify(deploymentInfo, null, 2)
  );
  console.log("💾 Deployment info saved to deployment.json\n");
  
  // Verification instructions
  if (hre.network.name !== "hardhat") {
    console.log("📋 To verify contracts on Arbiscan, run:");
    console.log(`npx hardhat verify --network ${hre.network.name} ${usdFryToken.address}`);
    console.log(`npx hardhat verify --network ${hre.network.name} ${agentBVerifier.address}`);
    console.log(`npx hardhat verify --network ${hre.network.name} ${positionVerifier.address}`);
    console.log(`npx hardhat verify --network ${hre.network.name} ${router.address} ${usdFryToken.address}`);
    console.log(`npx hardhat verify --network ${hre.network.name} ${matchingPool.address} ${usdFryToken.address}`);
    console.log("\n");
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
