import requests
from typing import Optional, Dict, Any
import json
from datetime import datetime

class StockXHistoricalAPI:
    def __init__(self):
        self.x_api_key = 'HIDDEN'
        self.apollographql_client_name = 'stockx-ios-prod'
        self.x_px_authorization = 'HIDDEN'
        self.base_url = 'https://gateway.stockx.com/api/graphql'
        self.session = requests.Session()
        self.session.headers.update(self._get_headers())

    def _get_headers(self) -> Dict[str, str]:
        return {
            'Content-Type': 'application/json',
            'x-api-key': self.x_api_key,
            'apollographql-client-name': self.apollographql_client_name,
            'x-px-authorization': self.x_px_authorization,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Origin': 'https://stockx.com',
            'Referer': 'https://stockx.com/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }

    def get_variant_price_levels(
        self,
        product_uuid: str,
        transaction_type: str,  # This will be "BID" to get bids
        country: str = "US",
        currency_code: str = "USD",
        page: int = 1
    ) -> Optional[Dict[str, Any]]:
        """
        Fetch price levels (bid or ask levels) for a specific product variant.
        transaction_type: "BID" for bids, "ASK" for asks.
        """
        query = """
        query GetVariantPriceLevels(
          $product_uuid: String!,
          $transactionType: TransactionType!,
          $country: String!,
          $currency_code: CurrencyCode!,
          $page: Int
        ) {
          variant(id: $product_uuid) {
            __typename
            market(currencyCode: $currency_code) {
              __typename
              priceLevels(
                country: $country,
                page: $page,
                transactionType: $transactionType
              ) {
                __typename
                edges {
                  __typename
                  node {
                    __typename
                    amount
                    count
                    variant {
                      __typename
                      id
                      traits {
                        __typename
                        size
                      }
                    }
                  }
                }
                pageInfo {
                  __typename
                  page
                  count
                  total
                  hasNextPage
                }
              }
            }
          }
        }
        """

        variables = {
            "product_uuid": product_uuid,
            "transactionType": transaction_type,
            "country": country,
            "currency_code": currency_code,
            "page": page
        }

        data = {
            "query": query,
            "variables": variables
        }

        try:
            # It's good practice to refresh cookies if they might expire or if required by the API
            self.session.get('https://stockx.com', timeout=10)
            response = self.session.post(
                self.base_url,
                json=data,
                timeout=30
            )

            print("--------------------------------")
            print(response.status_code)
            print(response.text)
            print(response.json())
            print("--------------------------------")
            response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price levels: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status: {e.response.status_code}")
                print(f"Response text: {e.response.text[:500]}") # Log part of the response
            return None
        except Exception as e: # Catch other potential errors like JSONDecodeError if response isn't JSON
            print(f"An unexpected error occurred: {str(e)}")
            return None

    
    def search_by_gtin(self, gtin: str) -> Optional[Dict[str, Any]]:
        """
        Search for a product by GTIN (Global Trade Item Number)
        """
        query = """
        query FetchVariantsFromGTIN($gtin: String!, $currencyCode: CurrencyCode, $country: String!, $market: String) {
          variants(gtin: $gtin) {
            __typename
            id
            sizeChart {
              __typename
              baseSize
              baseType
              displayOptions {
                __typename
                size
                type
              }
            }
            product {
              __typename
              id
              primaryCategory
              primaryTitle
              secondaryTitle
              styleId
              title
              productCategory
              listingType
              defaultSizeConversion {
                __typename
                name
                type
              }
              brand
              uuid
              urlKey
              media {
                __typename
                imageUrl
                smallImageUrl
              }
              traits {
                __typename
                format
                name
                value
                visible
              }
            }
            market(currencyCode: $currencyCode) {
              __typename
              state(country: $country, market: $market) {
                __typename
                lowestAsk {
                  __typename
                  amount
                }
                highestBid {
                  __typename
                  amount
                }
              }
            }
            traits {
              __typename
              sizeDescriptor
              size
            }
          }
        }
        """

        variables = {
            "gtin": str(gtin),
            "currencyCode": "USD",
            "country": "US",
            "market": "US"
        }

        data = {
            "query": query,
            "variables": variables
        }

        try:
            # First, visit the main page to get cookies
            self.session.get('https://stockx.com')
            
            # Then make the API request
            response = self.session.post(
                self.base_url,
                json=data,
                timeout=30
            )
            
            # Check response status
            response.raise_for_status()
            
            # Get the response content
            try:
                json_response = response.json()
                print("Response data:", json_response)
                return json_response
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON response: {str(e)}")
                print(f"Response content type: {response.headers.get('content-type', 'unknown')}")
                print(f"Response encoding: {response.encoding}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Request error: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status: {e.response.status_code}")
                print(f"Response headers: {e.response.headers}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None