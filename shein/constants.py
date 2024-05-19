import os

# Setup
DOMAIN = "shein.com"  # For checking if the URL is from the same domain
DEBUG = True  # Set to True to limit to 1 page
USE_DB = True  # True = MongoDB, False = JSON
URLS = [
    "https://us.shein.com/Pet-Supplies-c-2400.html?sort=10",
]

# Database
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
DATABASE_URL = f"mongodb://{MONGO_HOST}:27017/"
DATABASE_NAME = "shein"
COLLECTION_INDEX = {
    "product_urls": [
        {
            "keys": "url",
            "unique": True,
        }
    ],
    "product_details": [
        {
            "keys": "title",
            "unique": False,
        },
        {
            "keys": "url",
            "unique": True,
        },
        {
            "keys": "product_id",
            "unique": True,
        },
    ],
    "product_reviews": [
        {
            "keys": "product_id",
            "unique": False,
        }
    ],
}

# JSON
PATH_OUT_JSON = "data/raw/products_urls.json"

# Text processing
BLACKLISTED_WORDS = [
    "/user/auth/login",
    # "About",
    "bonus",
    "campaign",
    "campaigns",
    "contact",
    "Copyright",
    "copyright",
    "coupon-a",
    "daily-new",
    "facebook.com",
    "How-to",
    "how-to",
    "Imprint",
    "imprint",
    "instagram.com",
    "javascript:",
    "mailto:",
    "New-in-Trends",
    "New-in-Trends",
    "pinterest.com",
    "prime",
    "Privacy",
    "privacy",
    "promotion",
    "refund",
    "sale",
    "shein.com/beauty",
    "shein.com/cart",
    "shein.com/curve-plus-size",
    "shein.com/flashsale",
    "shein.com/home",
    "shein.com/kids",
    "shein.com/member-image-list",
    "shein.com/men",
    "shein.com/other",
    "shein.com/plussize",
    "shein.com/Return-Policy",
    "shein.com/style",
    "shein.com/women",
    "Shipping-Info",
    "SUPPLY-CHAIN-TRANSPARENCY",
    "tel:",
    "Terms",
    "terms",
    "tiktok.com",
    "track",
    "twitter.com",
    "weekly-picks",
    "youtube.com",
]
LIMIT_TO_3_MAX_REVIEW_PAGES = False
RETRIES = 3
