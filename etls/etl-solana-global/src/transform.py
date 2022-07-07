import logging
from typing import Any, List
from src.utils import safe_get as get


class SolscanTransformer:

    def price_and_volume_usdt(data: Any) -> Any:
        data = get(data, 'data')
        return {
            'price_usdt': get(data, 'priceUsdt', cast=float),
            'volume_usdt': get(data, 'volumeUsdt', cast=float)
        }

class CoinGeckoTransformer:

    def token_info(data: Any) -> Any:

        market_data: Any = get(data, "market_data")
        community_data: Any = get(data, "community_data")
        developer_data: Any = get(data, "community_data")
        public_interest_stats: Any = get(data, "public_interest_stats")
        exchange_data: List[Any] = get(data, "tickers")

        transformed_exchange_data: List[Any] = []
        
        for exchange in exchange_data:

                base_symbol: str = get(exchange, 'base')
                quote_symbol: str = get(exchange, 'target')
                name: str = get(get(exchange, 'market'), 'name')
                identifier: str = get(get(exchange, 'market'), 'identifier')
                has_trading_incentive: bool = get(get(exchange, 'market'), 'has_trading_incentive')
                price_usdt: float = get(get(exchange, 'converted_last'), 'usd')
                volume_usdt: float = get(get(exchange, 'converted_volume'), 'usd')
                trust_score: str = get(exchange, 'trust_score')
                bid_ask_pct_spread: float = get(exchange, "bid_ask_spread_percentage")

                transformed_exchange_data.append({
                    "base_symbol": base_symbol,
                    "quote_symbol": quote_symbol,
                    "name": name,
                    "identifier": identifier,
                    "has_trading_incentive": has_trading_incentive,
                    "price_usdt": price_usdt,
                    "volume_usdt": volume_usdt,
                    "trust_score": trust_score,
                    "bid_ask_pct_spread": bid_ask_pct_spread
                })

        return {
            "twitter": get(get(data, "links"), "twitter_screen_name"),
            "sentiment_votes_up_percentage": get(data, "sentiment_votes_up_percentage"),
            "sentiment_votes_down_percentage": get(data, "sentiment_votes_down_percentage"),
            "market_cap_rank": get(data, "market_cap_rank"),
            "coingecko_rank": get(data, "coingecko_rank"),
            "coingecko_score": get(data, "coingecko_score"),
            "developer_score": get(data, "developer_score"),
            "community_score": get(data, "community_score"),
            "liquidity_score": get(data, "liquidity_score"),
            "public_interest_score": get(data, "public_interest_score"),
            "price_usdt": get(get(market_data, "current_price"), "usd"),
            "total_value_locked": get(market_data, "total_value_locked"),
            "mcap_to_tvl_ratio": get(market_data, "mcap_to_tvl_ratio"),
            "fdv_to_tvl_ratio": get(market_data, "fdv_to_tvl_ratio"),
            "roi": get(market_data, "roi"),
            "price_ath_usdt": get(get(market_data, "ath"), "usd"),
            "price_ath_pct_change": get(get(market_data, "ath_change_percentage"), "usd"),
            "price_atl_usdt": get(get(market_data, "atl"), "usd"),
            "price_atl_pct_change": get(get(market_data, "atl_change_percentage"), "usd"),
            "market_cap": get(get(market_data, "market_cap"), "usd"),
            "total_volume": get(get(market_data, "total_volume"), "usd"),
            "price_high_24h": get(get(market_data, "high_24h"), "usd"),
            "price_low_24h": get(get(market_data, "low_24h"), "usd"),
            "price_change_24h": get(market_data, "price_change_24h"),
            "price_pct_change_24h": get(market_data, "price_change_percentage_24h"),
            "price_pct_change_7d": get(market_data, "price_change_percentage_7d"),
            "price_pct_change_14d": get(market_data, "price_change_percentage_14d"),
            "price_pct_change_30d": get(market_data, "price_change_percentage_30d"),
            "price_pct_change_60d": get(market_data, "price_change_percentage_60d"),
            "price_pct_change_200d": get(market_data, "price_change_percentage_200d"),
            "price_pct_change_1y": get(market_data, "price_change_percentage_1y"),
            "total_supply": get(market_data, "total_supply"),
            "max_supply": get(market_data, "max_supply"),
            "circulating_supply": get(market_data, "circulating_supply"),
            "facebook_likes": get(community_data, "facebook_likes"),
            "twitter_followers": get(community_data, "twitter_followers"),
            "reddit_av_posts_24h": get(community_data, "reddit_av_posts_24h"),
            "reddit_subscribers": get(community_data, "reddit_subscribers"),
            "reddit_active_accounts_48h": get(community_data, "reddit_accounts_active_48h"),
            "telegram_channel_user_count": get(community_data, "telegram_channel_user_count"),
            "git_fork_count": get(developer_data, "forks"),
            "git_star_count": get(developer_data, "stars"),
            "git_subscriber_count": get(developer_data, "subscribers"),
            "git_total_issue_count": get(developer_data, "total_issues"),
            "git_closed_issue_count": get(developer_data, "closed_issues"),
            "git_pull_requests_merged_count": get(developer_data, "pull_requests_merged"),
            "git_pull_request_contributor_count": get(developer_data, "pull_request_contributors"),
            "git_code_line_additions_count_4w": get(get(developer_data, "code_additions_deletions_4_weeks"),"additions"),
            "git_code_line_deletions_count_4w": get(get(developer_data, "code_additions_deletions_4_weeks"),"deletions"),
            "git_commit_count_4w": get(developer_data, "commit_count_4_weeks"),
            "alexa_rank": get(public_interest_stats, "alexa_rank"),
            "bing_matches": get(public_interest_stats, "bing_matches"),
            "exchanges": transformed_exchange_data
        }


class SolanaBlockExplorerTransformer:

    def supply(data: Any) -> Any:
        result: Any = get(data, 'result') 
        context: Any = get(result, "context")
        value: Any = get(result, "value")
        return {
            "slot": get(context, "slot"),
            "circulating": get(value, "circulating"),
            "non_circulating": get(value, "nonCirculating"),
            "total": get(value, "total")
        }


    def epoch_info(data: Any) -> Any:
        result = get(data, 'result')
        return {
            "absolute_slot": get(result, "absoluteSlot"),
            "block_height": get(result, "blockHeight"),
            "epoch": get(result, "epoch"),
            "slot_index": get(result, "slot_index"),
            "slots_in_epoch": get(result, "slotsInEpoch"),
            "transaction_count": get(result, 'transactionCount')
        }

