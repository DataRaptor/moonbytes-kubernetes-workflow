import { Orderbook } from '@project-serum/serum'
import { logger } from '../services/logger'
import { TradeCanExecuteRequest } from '../types'

const buyTradeCanFill = (
  tradeCanExecuteRequest: TradeCanExecuteRequest,
  asks: Orderbook
): boolean => {
  const { baseSymbol, quoteSymbol, side, marketAddress, price, quantity } = tradeCanExecuteRequest

  var filledSize = 0
  for (const ask of asks) {
    if (ask.price <= price) {
      filledSize += ask.size
    }
  }
  console.log(
    `[buyTradeCanFill] - ${side}ing ${quantity} ${baseSymbol} for ${
      quantity * price
    } ${quoteSymbol} at price: ${price} ${baseSymbol}/${quoteSymbol}`
  )
  if (filledSize > quantity) {
    console.log(`Buy Trade Can Fill For Market ${marketAddress}`)
    return true
  } 
  console.log(
    `Buy Trade Cannot Fill For Market ${marketAddress}. Stopping Trade.`
  )
  return false
}

const sellTradeCanFill = (
  tradeCanExecuteRequest: TradeCanExecuteRequest,
  bids: Orderbook
): boolean => {
  const { baseSymbol, quoteSymbol, side, marketAddress, price, quantity } = tradeCanExecuteRequest

  var filledSize = 0
  for (const bid of bids) {
    if (bid.price >= price) {
      filledSize += bid.size
    }
  }
  console.log(
    `[buyTradeCanFill] - ${side}ing ${quantity} ${baseSymbol} for ${
      quantity * price
    } ${quoteSymbol} at price: ${price} ${baseSymbol}/${quoteSymbol}`
  )
  if (filledSize > quantity) {
    console.info(`Sell Trade Can Fill For Market ${marketAddress}`)
    return true
  }
  console.log(
    `Sell Trade Cannot Fill For Market ${marketAddress}. Stopping Trade`
  )
  return false
}

export { buyTradeCanFill, sellTradeCanFill }
