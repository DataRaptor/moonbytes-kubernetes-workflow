import http from 'http'
import express from 'express'
import bodyParser = require('body-parser')
import { Connection } from '@solana/web3.js'
import {
  canExecuteBuyTrade,
  canExecuteSellTrade,
  getMarketData,
} from './controllers'
import { SOLANA_RPC_URL, PORT } from './config'
import { logger } from './services/logger'
import {
  TradeCanExecuteRequest,
  TradeCanExecuteResponse,
  GetMarketDataRequest,
  GetMarketDataResponse,
} from './types'

const connection: Connection = new Connection(SOLANA_RPC_URL, 'singleGossip')
const app: express.Express = express()
const server = http.createServer(app)

app.use(
  bodyParser.urlencoded({
    extended: true,
  })
)
app.use(bodyParser.json())


app.post(
  '/trade_can_execute',
  async (req: express.Request, res: express.Response) => {
    const tradeCanExecuteRequest: TradeCanExecuteRequest = req.body
    const { baseSymbol, quoteSymbol, side, price, quantity } =
      tradeCanExecuteRequest
    try {
      if (side == 'buy') {
        const tradeCanExecuteResponse: TradeCanExecuteResponse =
          await canExecuteBuyTrade(connection, tradeCanExecuteRequest)
        res.status(200).json(tradeCanExecuteResponse)
      } else if (side == 'sell') {
        const tradeCanExecuteResponse: TradeCanExecuteResponse =
          await canExecuteSellTrade(connection, tradeCanExecuteRequest)
        res.status(200).json(tradeCanExecuteResponse)
      } else {
        process.exit(1)
      }
    } catch (error) {
      const message = `💀 Could Not Sell ${quantity} ${baseSymbol} for ${
        quantity * price
      } ${quoteSymbol}  ${
        error.message
      } at price ${price} ${baseSymbol}/${quoteSymbol}`
      logger.error(message)
      res.status(500).json({
        ok: false,
        message: message,
        price_actual: null,
        quantity_actual: null,
      })
    }
  }
)

app.post(
  '/market_data',
  async (req: express.Request, res: express.Response) => {
    const getMarketDataRequest: GetMarketDataRequest = req.body
    try {
      const getMarketDataResponse: GetMarketDataResponse = await getMarketData(
        connection,
        getMarketDataRequest
      )
      res.status(200).json(getMarketDataResponse)
    } catch (error) {
      const message = `Could Not Get Price - ${error}`
      logger.error(message)
      res.status(500).json({
        ok: false,
        message: message,
        midpointPrice: null,
        bestBidPrice: null,
        asks: [],
        bids: [],
        askLiquidity: null,
        bidLiquidity: null,
      })
    }
  }
)

server.listen(PORT, () => {
  logger.info(
    `💫 [gradient-gargantuan::serum] started on port: ${PORT}`
  )
})
