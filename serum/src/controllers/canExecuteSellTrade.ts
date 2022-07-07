import { sellTradeCanFill, computeAskLiquidity, computeBidLiquidity } from '../libs'
import { Connection, PublicKey, Keypair, Account } from '@solana/web3.js'
import { Market, Orderbook, OpenOrders } from '@project-serum/serum'
import { logger } from '../services/logger'
import { TradeCanExecuteRequest, TradeCanExecuteResponse } from '../types'

const canExecuteSellTrade = async (
  connection: Connection,
  tradeCanExecuteRequest: TradeCanExecuteRequest
): Promise<TradeCanExecuteResponse> => {
  const { marketAddress, programId } = tradeCanExecuteRequest

  logger.info(`Loading Serum Market: ${marketAddress}`)
  const marketAddressPublicKey: PublicKey = new PublicKey(marketAddress)
  const programIdPublicKey: PublicKey = new PublicKey(programId)
  const options = { skipPreflight: false }
  const market: Market = await Market.load(
    connection,
    marketAddressPublicKey,
    options,
    programIdPublicKey
  )

  logger.info(`Running Pre-Execution Tests In Serum Market: ${marketAddress}`)
  const asks: Orderbook = await market.loadAsks(connection)
  const bids: Orderbook = await market.loadBids(connection)
  const hasLiquidity: boolean = (computeBidLiquidity(bids) > 1) && (computeAskLiquidity(asks) > 1)
  const canFill: boolean = sellTradeCanFill(tradeCanExecuteRequest, bids)
  const canExecute: boolean = hasLiquidity && canFill
  const tradeCanExecuteResponse: TradeCanExecuteResponse = {
    ok: true,
    message: `canExecute: ${canExecute}. hasLiquidity: ${hasLiquidity}. canFill: ${canFill}. Trades Executed`,
    hasLiquidity: hasLiquidity,
    canFill: canFill,
    canExecute: canExecute
  }
  if (!canExecute) {
    logger.error(`canExecuteSellRequest: canExecute: ${canExecute}. hasLiquidity: ${hasLiquidity}. canFill: ${canFill}. Trades Stopped.`)
  }
  return tradeCanExecuteResponse
}

export default canExecuteSellTrade
