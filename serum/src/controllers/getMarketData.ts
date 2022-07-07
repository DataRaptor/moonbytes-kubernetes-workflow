import { Connection, PublicKey, Keypair, Account } from '@solana/web3.js'
import { Market, Orderbook, OpenOrders } from '@project-serum/serum'
import { logger } from '../services/logger'
import {
  computePriceMidPoint,
  computeBestAsk,
  computeBestBid,
  computeAskLiquidity,
  computeBidLiquidity,
  computeBidAskSpread,
  computeBidAskPctSpread,
  parseBids,
  parseAsks,
} from '../libs'
import {
  GetMarketDataRequest,
  GetMarketDataResponse,
  OrderbookSlice,
} from '../types'

const getMarketData = async (
  connection: Connection,
  getMarketDataRequest: GetMarketDataRequest
): Promise<GetMarketDataResponse> => {

  const { marketAddress, programId } = getMarketDataRequest

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
  const asks: Orderbook = await market.loadAsks(connection)
  const bids: Orderbook = await market.loadBids(connection)

  const midpointPrice: number = computePriceMidPoint(asks, bids)
  const bestBidPrice: number = computeBestBid(bids)
  const bestAskPrice: number = computeBestAsk(asks)
  const bidAskPctSpread: number = computeBidAskPctSpread(bestAskPrice, bestBidPrice)
  const bidAskSpread: number = computeBidAskSpread(bestAskPrice, bestBidPrice)
  const parsedAsks: OrderbookSlice[] = parseAsks(asks)
  const parsedBids: OrderbookSlice[] = parseBids(bids)
  const bidLiquidity: number = computeBidLiquidity(bids)
  const askLiquidity: number = computeAskLiquidity(bids)
  const getMarketDataResponse: GetMarketDataResponse = {
    ok: true,
    message: 'Success',
    midpointPrice: midpointPrice,
    bestBidPrice: bestBidPrice,
    bestAskPrice: bestAskPrice,
    bidAskSpread: bidAskSpread,
    bidAskPctSpread: bidAskPctSpread,
    asks: parsedAsks,
    bids: parsedBids,
    bidLiquidity: bidLiquidity,
    askLiquidity: askLiquidity,
  }
  return getMarketDataResponse
}

export default getMarketData
