from typing import Any


class MagicEdenTransformer:

    def volume(data: Any) -> Any:
        return {
            'total': data['total'],
            '24hr': data['last24Hrs'],
            '7d': data['last7Days'],
            '30d': data['last30Days']
        }
