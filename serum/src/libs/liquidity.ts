import { Orderbook } from '@project-serum/serum'

const computeBidLiquidity = (bids: Orderbook): number => {
  var liquidity = 0
  for (const bid of bids) {
    liquidity += bid.size * bid.price
  }
  return liquidity
}

const computeAskLiquidity = (asks: Orderbook): number => {
  var liquidity = 0
  for (const ask of asks) {
    liquidity += ask.size * ask.price
  }
  return liquidity
}

export { computeBidLiquidity, computeAskLiquidity }
