type TradeExecutionRequest = {
  baseSymbol: string
  quoteSymbol: string
  marketAddress: string
  programId: string
  baseMint: string
  quoteMint: string
  side: string
  price: number
  quantity: number
}

type TradeCanExecuteRequest = {
  baseSymbol: string
  quoteSymbol: string
  marketAddress: string
  programId: string
  side: string
  price: number
  quantity: number
}

type GetMarketDataRequest = {
  baseSymbol: string
  quoteSymbol: string
  marketAddress: string
  programId: string
}

type TradeCanExecuteResponse = {
  ok: boolean
  message: string
  hasLiquidity: boolean
  canFill: boolean
  canExecute: boolean
}

type TradeExecutionResponse = {
  ok: boolean
  message: string
  price: number
  quantity: number
}

type GetMarketDataResponse = {
  ok: boolean
  message: string
  midpointPrice: number
  bestBidPrice: number
  bestAskPrice: number
  bidAskSpread: number
  bidAskPctSpread: number 
  asks: OrderbookSlice[]
  bids: OrderbookSlice[]
  bidLiquidity: number
  askLiquidity: number
}

type OrderbookSlice = {
  price: number
  size: number
}


export {
  TradeExecutionRequest,
  TradeExecutionResponse,
  TradeCanExecuteRequest,
  TradeCanExecuteResponse,
  GetMarketDataRequest,
  GetMarketDataResponse,
  OrderbookSlice
}
