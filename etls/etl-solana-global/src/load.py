import logging 
import datetime 
from typing import Any, List
from src.utils import safe_cast as cast
from influxdb_client import Point, WritePrecision


class SolscanLoader:

    def price_and_volume_usdt(data: Any) -> List[Point]:
        points: List[Point] = []

        point = Point("price_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .tag("base_symbol", "SOL") \
            .tag("quote_symbol", "USDT") \
            .field("value", data["price_usdt"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .tag("base_symbol", "SOL") \
            .tag("quote_symbol", "USDT") \
            .field("value", data["volume_usdt"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        return points


class CoinGeckoLoader:


    def token_info(data: Any) -> List[Point]:

        points: List[Point] = []

        # sentiment votes up percentage 
        point = Point("sentiment_upvotes_pct") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["sentiment_votes_up_percentage"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        #sentiment votes down percentage
        point = Point("sentiment_downvotes_pct") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["sentiment_votes_down_percentage"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # market cap rank
        point = Point("market_cap_rank") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["market_cap_rank"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # coingecko rank
        point = Point("coingecko_rank") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["coingecko_rank"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # coingecko score
        point = Point("coingecko_score") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["coingecko_score"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # developer score
        point = Point("developer_score") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["developer_score"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # community score
        point = Point("community_score") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["community_score"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # liquidity score
        point = Point("liquidity_score") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["liquidity_score"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # public interest score
        point = Point("public_interest_score") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["public_interest_score"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price_usdt
        point = Point("price_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_usdt"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # total value locked
        point = Point("total_value_locked") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["total_value_locked"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)
        
        # market cap to total value locked ratio
        point = Point("mcap_to_tvl_ratio") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["mcap_to_tvl_ratio"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # market cap to total value locked ratio
        point = Point("fdv_to_tvl_ratio") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["fdv_to_tvl_ratio"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # fully diluted value to total value locked ratio
        point = Point("fdv_to_tvl_ratio") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["fdv_to_tvl_ratio"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # return on investment
        point = Point("roi") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["roi"], float)) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # ath price usdt
        point = Point("price_ath_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_ath_usdt"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # ath pct change
        point = Point("price_ath_pct_change_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_ath_pct_change"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price atl price usdt
        point = Point("price_ath_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_ath_usdt"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price atl pct change
        point = Point("price_atl_pct_change_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_atl_pct_change"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # market cap
        point = Point("market_cap_usdt") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["market_cap"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # total volume
        point = Point("volume_total") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["total_volume"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price_ath_24h
        point = Point("price_ath_usdt_24h") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_high_24h"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price_atl_24h
        point = Point("price_atl_usdt_24h") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_low_24h"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price pct change 24h
        point = Point("price_pct_change_24h") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_change_24h"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price pct change 7d
        point = Point("price_pct_change_7d") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_pct_change_7d"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price pct change 14d
        point = Point("price_pct_change_14d") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_pct_change_14d"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price pct change 30d
        point = Point("price_pct_change_30d") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_pct_change_30d"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price pct change 60d
        point = Point("price_pct_change_60d") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_pct_change_60d"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price pct change 60d
        point = Point("price_pct_change_200d") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_pct_change_200d"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # price pct change 1y
        point = Point("price_pct_change_1y") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["price_pct_change_1y"], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # total supply
        # point = Point("supply_total") \
        #     .tag("dataset", "solana") \
        #     .tag("model", "global") \
        #     .field("value", cast(data["supply_total"], float))\
        #     .time(datetime.datetime.utcnow(), WritePrecision.NS)
        # points.append(point)


        # circulating supply
        # point = Point("supply_circulating") \
        #     .tag("dataset", "solana") \
        #     .tag("model", "global") \
        #     .field("value", cast(data["supply_total"], float))\
        #     .time(datetime.datetime.utcnow(), WritePrecision.NS)
        # points.append(point)

        # facebook likes
        point = Point("facebook_likes") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["facebook_likes"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # twitter followers
        point = Point("twitter_followers") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["twitter_followers"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # reddit_av_posts_24h
        point = Point("reddit_av_posts_24h") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["reddit_av_posts_24h"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # reddit_subscribers
        point = Point("reddit_subscribers") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["reddit_subscribers"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # reddit_active_accounts_48h
        point = Point("reddit_active_accounts_48h") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["reddit_active_accounts_48h"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)


        # reddit_active_accounts_48h
        point = Point("reddit_active_accounts_48h") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["reddit_active_accounts_48h"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # telegram_channel_user_count
        point = Point("telegram_channel_user_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["telegram_channel_user_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git fork count
        point = Point("git_fork_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_fork_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git star count
        point = Point("git_star_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_star_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git subscriber count
        point = Point("git_subscriber_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_subscriber_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git total issue count
        point = Point("git_total_issue_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_total_issue_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git closed issue count
        point = Point("git_closed_issue_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_closed_issue_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git pull request merged count
        point = Point("git_pull_requests_merged_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_pull_requests_merged_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git pull request contributor count
        point = Point("git_pull_request_contributor_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_pull_request_contributor_count"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git pull request line addition count 4w
        point = Point("git_code_line_additions_count_4w") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_code_line_additions_count_4w"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git pull request line deletion count 4w
        point = Point("git_code_line_deletions_count_4w") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_code_line_deletions_count_4w"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git pull request line deletion count 4w
        point = Point("git_commit_count_4w") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["git_commit_count_4w"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git pull request line deletion count 4w
        point = Point("alexa_rank") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["alexa_rank"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # git pull request line deletion count 4w
        point = Point("bing_matches") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data["bing_matches"], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # logging.info("Num of Exchanges: {}".format(
        #     len(data['exchanges'])
        # ))

        for exchange in data['exchanges']:

            # Exchange Volume
            point = Point("volume_usdt") \
                .tag("dataset", "solana") \
                .tag("model", "exchanges") \
                .tag("name", exchange["name"]) \
                .tag("base_symbol", exchange['base_symbol']) \
                .tag("quote_symbol", exchange['quote_symbol']) \
                .field("value", cast(exchange['volume_usdt'], float))\
                .time(datetime.datetime.utcnow(), WritePrecision.NS)
            points.append(point)

            # Exchange Price 
            point = Point("price_usdt") \
                .tag("dataset", "solana") \
                .tag("model", "exchanges") \
                .tag("name", exchange["name"]) \
                .tag("base_symbol", exchange['base_symbol']) \
                .tag("quote_symbol", exchange['quote_symbol']) \
                .field("value", cast(exchange['price_usdt'], float))\
                .time(datetime.datetime.utcnow(), WritePrecision.NS)
            points.append(point)

            # Exchange Trust Score 
            point = Point("trust_score") \
                .tag("dataset", "solana") \
                .tag("model", "exchanges") \
                .tag("name", exchange["name"]) \
                .tag("base_symbol", exchange['base_symbol']) \
                .tag("quote_symbol", exchange['quote_symbol']) \
                .field("value", cast(exchange['trust_score'], str))\
                .time(datetime.datetime.utcnow(), WritePrecision.NS)
            points.append(point)

            # Bid/Ask Spread
            point = Point("bid_ask_pct_spread") \
                .tag("dataset", "solana") \
                .tag("model", "exchanges") \
                .tag("name", exchange["name"]) \
                .tag("base_symbol", exchange['base_symbol']) \
                .tag("quote_symbol", exchange['quote_symbol']) \
                .field("value", cast(exchange['bid_ask_pct_spread'], float))\
                .time(datetime.datetime.utcnow(), WritePrecision.NS)
            points.append(point)

        # logging.info("Parsed Coingecko::token_lists successfully. Found: {} Tokens".format(
        #     len(points)
        # ))

        return points



class SolanaBlockExplorerLoader:

    def supply(data: Any) -> List[Point]:
        points: List[Point] = []

        # slot number
        point = Point("slot_number") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['slot'], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # circulating supply
        point = Point("supply_circulating") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['circulating'], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # noncirculating supply
        point = Point("supply_noncirculating") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['non_circulating'], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # total supply 
        point = Point("supply_total") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['total'], float))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)
    
        return points



    def epoch_info(data: Any) -> List[Point]:
        
        points: list[Point] = []

        # epoch absolute slot
        point = Point("epoch_absolute_slot_number") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['absolute_slot'], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # epoch block height
        point = Point("epoch_block_height") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['block_height'], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # epoch slot index
        point = Point("epoch_slot_index") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['slot_index'], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # slots in epoch count
        point = Point("epoch_slot_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['slots_in_epoch'], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        # epoch transaction count
        point = Point("epoch_transaction_count") \
            .tag("dataset", "solana") \
            .tag("model", "global") \
            .field("value", cast(data['transaction_count'], int))\
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        return points

