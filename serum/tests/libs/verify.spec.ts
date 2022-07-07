// @ts-nocheck

import assert from 'assert'
import { Connection, PublicKey } from '@solana/web3.js'
import { buyTradeCanFill, sellTradeCanFill } from '../../src/libs/verify'
import { ExecutorRequest } from '../../src/types'
import { SOLANA_RPC_URL } from '../../src/config'
import { Market, Orderbook } from '@project-serum/serum'

const connection: Connection = new Connection(SOLANA_RPC_URL, 'singleGossip')

describe('BuyTradeCanFill', function () {
  it('Should Fill Buy Trade', async function () {
    const executorRequest: ExecutorRequest = {
      uuid: '8250bbb4-adf2-4018-a4cb-5c2ef5c5be49',
      pair_name: 'soETH-USDC',
      token_a: 'soETH',
      token_b: 'USDC',
      buy_market: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      buy_serum_market: '',
      buy_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      buy_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      buy_base_vault: 'EmQSvut2daR6DBxRynsWt64U9Qyz2B3dBV1YTvvfTcX3',
      buy_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      buy_quote_vault: '',
      buy_amount_quoted: 0,
      buy_source: 'serum',
      buy_price: 99999,
      buy_quantity: 1,
      buy_liquidity: 1808151.127193,
      buy_liquidity_pct_change_24_hr: -37.53360112610514,
      buy_last_trade: '2022-01-29T20:31:53.000Z',
      buy_volume_24_hr: 0,
      buy_volume_pct_change_24_hr: 0,
      buy_owner: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      sell_market: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
      sell_serum_market: '',
      sell_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      sell_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      sell_base_vault: '7Nw66LmJB6YzHsgEGQ8oDSSsJ4YzUkEVAvysQuQw7tC4',
      sell_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      sell_quote_vault: '',
      sell_amount_quoted: 0,
      sell_source: 'serum',
      sell_price: 1,
      sell_quantity: 1,
      sell_liquidity: 12444503.116978,
      sell_liquidity_pct_change_24_hr: 21.934635921469766,
      sell_last_trade: '2022-02-07T04:01:42.000Z',
      sell_volume_24_hr: '',
      sell_volume_pct_change_24_hr: '',
      sell_owner: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
    }
    const marketAddress: PublicKey = new PublicKey(executorRequest.buy_market)
    const programId: PublicKey = new PublicKey(executorRequest.buy_program_id)
    const options = { skipPreflight: false }
    const market: Market = await Market.load(
      connection,
      marketAddress,
      options,
      programId
    )
    const asks: Orderbook = await market.loadAsks(connection)
    const buyCanFill: boolean = buyTradeCanFill(executorRequest, asks)
    assert.equal(buyCanFill, true)
  })
  it('Should Not Fill Buy Trade', async function () {
    const executorRequest: ExecutorRequest = {
      uuid: '8250bbb4-adf2-4018-a4cb-5c2ef5c5be49',
      pair_name: 'soETH-USDC',
      token_a: 'soETH',
      token_b: 'USDC',
      buy_market: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      buy_serum_market: '',
      buy_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      buy_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      buy_base_vault: 'EmQSvut2daR6DBxRynsWt64U9Qyz2B3dBV1YTvvfTcX3',
      buy_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      buy_quote_vault: '',
      buy_amount_quoted: 0,
      buy_source: 'serum',
      buy_price: 1,
      buy_quantity: 1,
      buy_liquidity: 1808151.127193,
      buy_liquidity_pct_change_24_hr: -37.53360112610514,
      buy_last_trade: '2022-01-29T20:31:53.000Z',
      buy_volume_24_hr: 0,
      buy_volume_pct_change_24_hr: 0,
      buy_owner: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      sell_market: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
      sell_serum_market: '',
      sell_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      sell_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      sell_base_vault: '7Nw66LmJB6YzHsgEGQ8oDSSsJ4YzUkEVAvysQuQw7tC4',
      sell_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      sell_quote_vault: '',
      sell_amount_quoted: 0,
      sell_source: 'serum',
      sell_price: 1,
      sell_quantity: 1,
      sell_liquidity: 12444503.116978,
      sell_liquidity_pct_change_24_hr: 21.934635921469766,
      sell_last_trade: '2022-02-07T04:01:42.000Z',
      sell_volume_24_hr: '',
      sell_volume_pct_change_24_hr: '',
      sell_owner: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
    }
    const marketAddress: PublicKey = new PublicKey(executorRequest.buy_market)
    const programId: PublicKey = new PublicKey(executorRequest.buy_program_id)
    const options = { skipPreflight: false }
    const market: Market = await Market.load(
      connection,
      marketAddress,
      options,
      programId
    )
    const asks: Orderbook = await market.loadBids(connection)
    const buyCanFill: boolean = buyTradeCanFill(executorRequest, asks)
    assert.equal(buyCanFill, false)
  })
})

describe('SellTradeCanFill', function () {
  it('Should Fill Sell Trade', async function () {
    const executorRequest: ExecutorRequest = {
      uuid: '8250bbb4-adf2-4018-a4cb-5c2ef5c5be49',
      pair_name: 'soETH-USDC',
      token_a: 'soETH',
      token_b: 'USDC',
      buy_market: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      buy_serum_market: '',
      buy_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      buy_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      buy_base_vault: 'EmQSvut2daR6DBxRynsWt64U9Qyz2B3dBV1YTvvfTcX3',
      buy_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      buy_quote_vault: '',
      buy_amount_quoted: 0,
      buy_source: 'serum',
      buy_price: 99999,
      buy_quantity: 1,
      buy_liquidity: 1808151.127193,
      buy_liquidity_pct_change_24_hr: -37.53360112610514,
      buy_last_trade: '2022-01-29T20:31:53.000Z',
      buy_volume_24_hr: 0,
      buy_volume_pct_change_24_hr: 0,
      buy_owner: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      sell_market: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
      sell_serum_market: '',
      sell_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      sell_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      sell_base_vault: '7Nw66LmJB6YzHsgEGQ8oDSSsJ4YzUkEVAvysQuQw7tC4',
      sell_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      sell_quote_vault: '',
      sell_amount_quoted: 0,
      sell_source: 'serum',
      sell_price: 1,
      sell_quantity: 1,
      sell_liquidity: 12444503.116978,
      sell_liquidity_pct_change_24_hr: 21.934635921469766,
      sell_last_trade: '2022-02-07T04:01:42.000Z',
      sell_volume_24_hr: '',
      sell_volume_pct_change_24_hr: '',
      sell_owner: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
    }
    const marketAddress: PublicKey = new PublicKey(executorRequest.buy_market)
    const programId: PublicKey = new PublicKey(executorRequest.buy_program_id)
    const options = { skipPreflight: false }
    const market: Market = await Market.load(
      connection,
      marketAddress,
      options,
      programId
    )
    const bids: Orderbook = await market.loadAsks(connection)
    const sellCanFill: boolean = buyTradeCanFill(executorRequest, bids)
    assert.equal(sellCanFill, true)
  })
  it('Should Not Fill Sell Trade', async function () {
    const executorRequest: ExecutorRequest = {
      uuid: '8250bbb4-adf2-4018-a4cb-5c2ef5c5be49',
      pair_name: 'soETH-USDC',
      token_a: 'soETH',
      token_b: 'USDC',
      buy_market: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      buy_serum_market: '',
      buy_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      buy_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      buy_base_vault: 'EmQSvut2daR6DBxRynsWt64U9Qyz2B3dBV1YTvvfTcX3',
      buy_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      buy_quote_vault: '',
      buy_amount_quoted: 0,
      buy_source: 'serum',
      buy_price: 99999,
      buy_quantity: 1,
      buy_liquidity: 1808151.127193,
      buy_liquidity_pct_change_24_hr: -37.53360112610514,
      buy_last_trade: '2022-01-29T20:31:53.000Z',
      buy_volume_24_hr: 0,
      buy_volume_pct_change_24_hr: 0,
      buy_owner: '69MgRpghk9tJBzqUfg2mBnGP2q2xB66MNHhm6XSquJ6g',
      sell_market: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
      sell_serum_market: '',
      sell_program_id: '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
      sell_base_mint: '2FPyTwcZLUg1MDrwsyoP4D6s1tM7hAkHYRjkNb5w6Pxk',
      sell_base_vault: '7Nw66LmJB6YzHsgEGQ8oDSSsJ4YzUkEVAvysQuQw7tC4',
      sell_quote_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      sell_quote_vault: '',
      sell_amount_quoted: 0,
      sell_source: 'serum',
      sell_price: 99999999,
      sell_quantity: 1,
      sell_liquidity: 12444503.116978,
      sell_liquidity_pct_change_24_hr: 21.934635921469766,
      sell_last_trade: '2022-02-07T04:01:42.000Z',
      sell_volume_24_hr: '',
      sell_volume_pct_change_24_hr: '',
      sell_owner: '4tSvZvnbyzHXLMTiFonMyxZoHmFqau1XArcRCVHLZ5gX',
    }
    const marketAddress: PublicKey = new PublicKey(executorRequest.buy_market)
    const programId: PublicKey = new PublicKey(executorRequest.buy_program_id)
    const options = { skipPreflight: false }
    const market: Market = await Market.load(
      connection,
      marketAddress,
      options,
      programId
    )
    const bids: Orderbook = await market.loadBids(connection)
    const sellCanFill: boolean = sellTradeCanFill(executorRequest, bids)
    assert.equal(sellCanFill, false)
  })
})
