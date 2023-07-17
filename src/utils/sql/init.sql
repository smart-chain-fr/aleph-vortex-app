-- Indexer
DROP TABLE IF EXISTS indexer;
CREATE TABLE IF NOT EXISTS indexer (
    id SERIAL NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE,
    level BIGINT,
    totalSupply BIGINT,
    circulatingSupply BIGINT,
    totalBootstrapped BIGINT,
    totalCommitments BIGINT,
    totalActivated BIGINT,
    totalCreated BIGINT,
    totalBurned BIGINT,
    totalBanished BIGINT,
    totalFrozen BIGINT,
    totalRollupBonds BIGINT,
    totalSmartRollupBonds BIGINT,
    totalVested BIGINT,
    CONSTRAINT indexer_pkey PRIMARY KEY (id)
);

-- CONTRACT : DEX
DROP TABLE IF EXISTS contract_dex_storage;
CREATE TABLE IF NOT EXISTS contract_dex_storage
(
    id SERIAL NOT NULL,
    history BIGINT,
    manager TEXT,
    reserve TEXT,
    xtzpool TEXT,
    lqttotal TEXT,
    tokenpool TEXT,
    lqtaddress TEXT,
    freezebaker BOOLEAN,
    tokenaddress TEXT,
    user_investments BIGINT,
    selfisupdatingtokenpool BOOLEAN,
    CONSTRAINT contract_dex_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_dex_operations;
CREATE TABLE IF NOT EXISTS contract_dex_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_dex_operations_pkey PRIMARY KEY (id)
);

-- CONTRACT : TOKEN SMAK
DROP TABLE IF EXISTS contract_token_smak_storage;
CREATE TABLE IF NOT EXISTS contract_token_smak_storage
(
    id SERIAL NOT NULL,
    freezer TEXT,
    balances TEXT,
    metadata TEXT,
    totalSupply TEXT,
    administrator TEXT,
    token_metadata TEXT,
    frozen_accounts TEXT,
    CONSTRAINT contract_token_smak_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_token_smak_operations;
CREATE TABLE IF NOT EXISTS contract_token_smak_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_token_smak_operations_pkey PRIMARY KEY (id)
);

-- CONTRACT : TOKEN ANTI
DROP TABLE IF EXISTS contract_token_anti_storage;
CREATE TABLE IF NOT EXISTS contract_token_anti_storage
(
    id SERIAL NOT NULL,
    admin TEXT,
    ledger TEXT,
    reserve TEXT,
    metadata TEXT,
    allowances TEXT,
    burn_address TEXT,
    total_supply TEXT,
    burned_supply TEXT,
    initial_supply TEXT,
    token_metadata TEXT,
    CONSTRAINT contract_token_anti_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_token_anti_operations;
CREATE TABLE IF NOT EXISTS contract_token_anti_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_token_anti_operations_pkey PRIMARY KEY (id)
);

-- CONTRACT : VORTEX_FACTORY_FA12
DROP TABLE IF EXISTS contract_factory_fa12_storage;
CREATE TABLE IF NOT EXISTS contract_factory_fa12_storage
(
    id SERIAL NOT NULL,
    swaps BIGINT,
    counter BIGINT,
    empty_tokens BIGINT,
    empty_history BIGINT,
    token_to_swaps BIGINT,
    default_reserve TEXT,
    default_metadata BIGINT,
    empty_allowances BIGINT,
    default_token_metadata BIGINT,
    empty_user_investments BIGINT,    
    CONSTRAINT contract_factory_fa12_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_factory_fa12_operations;
CREATE TABLE IF NOT EXISTS contract_factory_fa12_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_factory_fa12_operations_pkey PRIMARY KEY (id)
);

-- CONTRACT : VORTEX_FACTORY_FA2
DROP TABLE IF EXISTS contract_factory_fa2_storage;
CREATE TABLE IF NOT EXISTS contract_factory_fa2_storage
(
    id SERIAL NOT NULL,
    swaps BIGINT,
    counter BIGINT,
    empty_tokens BIGINT,
    empty_history BIGINT,
    token_to_swaps BIGINT,
    default_reserve TEXT,
    default_metadata BIGINT,
    empty_allowances BIGINT,
    default_token_metadata BIGINT,
    empty_user_investments BIGINT,    
    CONSTRAINT contract_factory_fa2_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_factory_fa2_operations;
CREATE TABLE IF NOT EXISTS contract_factory_fa2_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_factory_fa2_operations_pkey PRIMARY KEY (id)
);

-- CONTRACT : VORTEX_FACTORY_DOGA
DROP TABLE IF EXISTS contract_factory_doga_storage;
CREATE TABLE IF NOT EXISTS contract_factory_doga_storage
(
    id SERIAL NOT NULL,
    swaps BIGINT,
    counter BIGINT,
    empty_tokens BIGINT,
    empty_history BIGINT,
    token_to_swaps BIGINT,
    default_reserve TEXT,
    default_metadata BIGINT,
    empty_allowances BIGINT,
    default_token_metadata BIGINT,
    empty_user_investments BIGINT,    
    CONSTRAINT contract_factory_doga_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_factory_doga_operations;
CREATE TABLE IF NOT EXISTS contract_factory_doga_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_factory_doga_operations_pkey PRIMARY KEY (id)
);

-- CONTRACT : VORTEX_STAKING_SMAK
DROP TABLE IF EXISTS contract_staking_smak_storage;
CREATE TABLE IF NOT EXISTS contract_staking_smak_storage (
    id SERIAL NOT NULL,
    admin TEXT,
    reserve TEXT,
    metadata BIGINT,
    addressId BIGINT,
    maxValuesNb TEXT,
    stakingHistory BIGINT,
    votingContract TEXT,
    can_set_storage BOOLEAN,
    numberOfStakers TEXT,
    redeemedRewards BIGINT,
    stakeFlexLength TEXT,
    FA12TokenContract TEXT,
    userStakeFlexPack BIGINT,
    userStakeLockPack BIGINT,
    totalRedeemedRewards TEXT,
    CONSTRAINT contract_staking_smak_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_staking_smak_operations;
CREATE TABLE IF NOT EXISTS contract_staking_smak_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_staking_smak_operations_pkey PRIMARY KEY (id)
);

-- CONTRACT : VORTEX_FARMS_V1
DROP TABLE IF EXISTS contract_farms_v1_storage;
CREATE TABLE IF NOT EXISTS contract_farms_v1_storage (
    id SERIAL NOT NULL,
    admin TEXT,
    inverse_farms BIGINT,
    all_farms_data BIGINT,
    CONSTRAINT contract_farms_v1_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_farms_v1_operations;
CREATE TABLE IF NOT EXISTS contract_farms_v1_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_farms_v1_pkey PRIMARY KEY (id)
);

-- CONTRACT : VORTEX_FARMS_V2
DROP TABLE IF EXISTS contract_farms_v2_storage;
CREATE TABLE IF NOT EXISTS contract_farms_v2_storage (
    id SERIAL NOT NULL,
    admin TEXT,
    inverse_farms BIGINT,
    all_farms_data BIGINT,
    CONSTRAINT contract_farms_v2_storage_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_farms_v2_operations;
CREATE TABLE IF NOT EXISTS contract_farms_v2_operations (
    id SERIAL NOT NULL,
    type TEXT,
    level BIGINT,
    timestamp TIMESTAMP,
    block TEXT,
    hash TEXT,
    counter BIGINT,
    sender TEXT,
    gasLimit BIGINT,
    gasUsed BIGINT,
    storageLimit BIGINT,
    storageUsed BIGINT,
    bakerFee BIGINT,
    storageFee BIGINT,
    allocationFee BIGINT,
    target TEXT,
    amount BIGINT,
    status TEXT,
    hasInternals BOOLEAN,
    initiator TEXT DEFAULT '',
    nonce BIGINT DEFAULT 0,
    parameter TEXT DEFAULT '',
    senderCodeHash BIGINT DEFAULT 0,
    targetCodeHash BIGINT DEFAULT 0,
    tokenTransfersCount BIGINT DEFAULT 0,
    errors TEXT DEFAULT '',
    eventsCount BIGINT DEFAULT 0,
    CONSTRAINT contract_farms_v2_pkey PRIMARY KEY (id)
);
DROP TABLE IF EXISTS contract_farms_v2_allfarms;
CREATE TABLE IF NOT EXISTS contract_farms_v2_allfarms (
    id SERIAL NOT NULL,
    factory INT,
    address TEXT,
    CONSTRAINT contract_farms_v2_allfarms_pkey PRIMARY KEY (id),
    CONSTRAINT contract_farms_v2_allfarms_factory_key FOREIGN KEY (factory) REFERENCES contract_farms_v2_storage (id)
);