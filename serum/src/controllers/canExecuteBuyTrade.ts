import { buyTradeCanFill, computeBidLiquidity, computeAskLiquidity } from '../libs'
import { logger } from '../services/logger'
import { Market, Orderbook } from '@project-serum/serum'
import { Connection, PublicKey } from '@solana/web3.js'
import { TradeCanExecuteRequest, TradeCanExecuteResponse } from '../types'

const canExecuteBuyTrade = async (
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

  logger.info(`Simulating Order In Serum Market: ${marketAddress}`)
  const asks: Orderbook = await market.loadAsks(connection)
  const bids: Orderbook = await market.loadBids(connection)
  const hasLiquidity: boolean = (computeBidLiquidity(bids) > 1) && (computeAskLiquidity(asks) > 1)
  const canFill: boolean = buyTradeCanFill(tradeCanExecuteRequest, asks)
  const canExecute: boolean = hasLiquidity && canFill
  const tradeCanExecuteResponse: TradeCanExecuteResponse = {
    ok: true,
    message: `canExecute: ${canExecute}. hasLiquidity: ${hasLiquidity}. canFill: ${canFill}`,
    hasLiquidity: hasLiquidity,
    canFill: canFill,
    canExecute: canExecute
  }
  if (!canExecute) {
    logger.error(`canExecuteBuyRequest: canExecute: ${canExecute}. hasLiquidity: ${hasLiquidity}. canFill: ${canFill}. Trades Stopped.`)
  }
  return tradeCanExecuteResponse
}

export default canExecuteBuyTrade
