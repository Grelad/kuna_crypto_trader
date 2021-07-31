# -*- coding: utf-8 -*-

"""Console script for kuna."""
from time import sleep

from api_handler import KunaAPI
import settings


def main(args=None):
    """Console script for kuna."""
    api_handler = KunaAPI(access_key=settings.access_key, secret_key=settings.secret_key)
    api_handler.get_recent_market_data(','.join(settings.MARKET_PAIRS_TO_GRYVNA))


if __name__ == "__main__":
    while True:
        main()
        sleep(60)
