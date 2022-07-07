import { OrderbookSlice } from '../types'
import { Orderbook } from '@project-serum/serum'

const computePriceMidPoint = (asks: Orderbook, bids: Orderbook): number => {
  var highestBid = 0
  var lowestAsk = Infinity
  for (const ask of asks) {
    if (ask.price <= lowestAsk) {
      lowestAsk = ask.price
    }
  }
  for (const bid of bids) {
    if (bid.price >= highestBid) {
      highestBid = bid.price
    }
  }
  return (lowestAsk + highestBid) / 2
}

const computeBestAsk = (asks: Orderbook): number => {
  var bestAsk = Infinity
  for (const ask of asks) {
    if (ask.price <= bestAsk) {
      bestAsk = ask.price
    }
  }
  return bestAsk
}

const computeBestBid = (bids: Orderbook): number => {
  var bestBid = 0
  for (const bid of bids) {
    if (bid.price >= bestBid) {
      bestBid = bid.price
    }
  }
  return bestBid
}

const parseBids = (bids: Orderbook): OrderbookSlice[] => {
  var parsedBids: OrderbookSlice[] = []
  for (const bid of bids) {
    parsedBids.push({
      price: bid.price,
      size: bid.size,
    })
  }
  return parsedBids
}

const parseAsks = (asks: Orderbook): OrderbookSlice[] => {
  var parsedAsks: OrderbookSlice[] = []
  for (const ask of asks) {
    parsedAsks.push({
      price: ask.price,
      size: ask.size,
    })
  }
  return parsedAsks
}

const computeBidAskPctSpread = (askPrice: number, bidPrice: number): number => {
  return (askPrice - bidPrice) / bidPrice
}

const computeBidAskSpread = (askPrice: number, bidPrice: number): number => {
  return askPrice - bidPrice
}

export {
  computePriceMidPoint,
  computeBestAsk,
  computeBestBid,
  computeBidAskSpread,
  computeBidAskPctSpread,
  parseBids,
  parseAsks,
}
