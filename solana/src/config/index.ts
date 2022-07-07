import { readFile } from 'mz/fs'
import { logger } from '../services/logger'

const PORT = process.env.PORT || 8080
const SOLANA_RPC_URL =
  process.env.SOLANA_RPC_URL || 'https://solana-api.projectserum.com/'
const PRIVATE_KEY_PATH =
  process.env.PRIVATE_KEY_PATH || './src/config/wallet.json'
const TIME_TILL_TRADE_SETTLE =
  Number(process.env.TIME_TILL_TRADE_SETTLE) || 10000

const getPrivateKey = async () => {
  if (!PRIVATE_KEY_PATH) {
    logger.warn(
      "> No Private Key Path Environment Variable Detected! You're going to need this trust me."
    )
    process.exit(1)
  }
  const privateKeyString = await readFile(PRIVATE_KEY_PATH, {
    encoding: 'utf8',
  })
  const privateKey = Uint8Array.from(JSON.parse(privateKeyString))
  return privateKey
}

export {
  PORT,
  SOLANA_RPC_URL,
  PRIVATE_KEY_PATH,
  TIME_TILL_TRADE_SETTLE,
  getPrivateKey,
}
