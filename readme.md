# Job Title: Expert Developer Needed for StockX API Integration with Bot Protection Bypass

## Project Overview
We need an expert developer to create a reliable solution for fetching price data from StockX's GraphQL API while handling their PerimeterX bot protection system. The current implementation is being blocked by PerimeterX's security measures.

## Reference Implementation
There is an existing commercial implementation available at [CommercialStockXAPI](https://github.com/Sting-Lee/CommercialStockXAPI/) that successfully handles these challenges. The developer should study this implementation as a reference, particularly their approach to:
- Handling PerimeterX protection
- Managing authentication tokens
- Implementing the GraphQL queries
- Handling session management

The project requires integration with two specific StockX API endpoints:

1. Product Size Ask List API:
   - Endpoint: `https://stockxapi.dataspiderhub.com/docs#/stockx/i_product_size_ask_list_api_stockx_product_size_ask_list_get`
   - Purpose: Retrieve ask (sell) prices for specific product sizes

2. Product Size Bid List API:
   - Endpoint: `https://stockxapi.dataspiderhub.com/docs#/stockx/i_product_size_bid_list_api_stockx_product_size_bid_list_get`
   - Purpose: Retrieve bid (buy) prices for specific product sizes

These endpoints will be used to fetch real-time pricing data for StockX products, which is the core functionality of this integration.

## Existing Implementation Reference
A working implementation exists for a related StockX API endpoint:
- API: Product Search by GTIN
- Endpoint: `https://stockxapi.dataspiderhub.com/docs#/stockx/i_search_product_by_gtin_api_stockx_search_product_by_gtin_get`
- Implementation: See `demo.py` for a complete Python implementation
- Status: Successfully integrated and working

This existing implementation serves as a reference for the authentication and API integration patterns. However, the current challenge lies in implementing the two endpoints mentioned above (Product Size Ask List and Bid List APIs), which require additional handling of authentication and request parameters.


## Technical Requirements

### Core Technologies
- Node.js /Python
- GraphQL
- Experience with bot protection bypass techniques

### Specific Tasks
1. Implement a robust solution to bypass PerimeterX protection on StockX
2. Create a reliable method to obtain and maintain valid authentication tokens
3. Successfully fetch price data from StockX's GraphQL API endpoint
4. Handle CAPTCHA challenges when they occur
5. Implement proper browser fingerprinting and anti-detection measures

### Technical Details
- Target URL: https://gateway.stockx.com/api/graphql
- Required Headers: (These can be found in the IOS or Andriod app. Not sure from where my developer has got these. Please check if you can find these from ios or android. If not, I can provide you with the credentials)
  - x-api-key
  - x-px-authorization
  - apollographql-client-name
  - Other standard headers

### Test Data
We will provide multiple variant IDs for testing, including:
- 9b3a25dd-6862-4b64-b328-901b1d9366e4 (Sample ID for testing)
- Additional variant IDs will be provided for comprehensive testing

The solution should be able to:
1. Handle multiple variant IDs in sequence
2. Process different product types (shoes, clothing, etc.)
3. Handle various size variations
4. Manage different currency and country combinations

### GraphQL Query Details
The solution should implement the following GraphQL query structure, which will be tested with multiple variant IDs:

```graphql
query GetVariantPriceLevels(
  $product_uuid: String!,  # This will be the variant ID we provide
  $transactionType: TransactionType!,
  $country: String!,
  $currency_code: CurrencyCode!,
  $page: Int
) {
  variant(id: $product_uuid) {
    market(currencyCode: $currency_code) {
      priceLevels(
        country: $country,
        page: $page,
        transactionType: $transactionType
      ) {
        edges {
          node {
            amount
            count
            variant {
              id
              traits {
                size
              }
            }
          }
        }
        pageInfo {
          page
          count
          total
          hasNextPage
        }
      }
    }
  }
}
```

### Testing Requirements
The solution will be tested with:
1. Multiple variant IDs provided by us
2. Different transaction types (ASK/BID)
3. Various country and currency combinations
4. Different page numbers for pagination
5. Edge cases and error scenarios

### Expected Response Format
The API should return data in the following structure for each variant ID:
```json
{
    "code": 200,
    "msg": "success",
    "data": {
      "data": {
        "variant": {
          "market": {
            "priceLevels": {
              "edges": [
                {
                  "node": {
                    "amount": "80",
                    "count": 1,
                    "variant": {
                      "id": "9b3a25dd-6862-4b64-b328-901b1d9366e4",
                      "traits": {
                        "size": "8.5"
                      }
                    }
                  }
                }
                // ... more price levels
              ],
              "pageInfo": {
                "page": 1,
                "count": 50,
                "total": 6,
                "hasNextPage": false
              }
            }
          }
        }
      }
    }
}
```

### Current Challenges
1. PerimeterX bot protection blocking requests
2. Dynamic x-px-authorization token requirements
3. Need for proper session management
4. CAPTCHA handling
5. Browser fingerprinting detection

### Deliverables
1. Working Node.js script that can:
   - Successfully bypass PerimeterX protection
   - Maintain valid authentication
   - Fetch price data reliably for multiple variant IDs
   - Handle CAPTCHA challenges
   - Process multiple requests in sequence
2. Documentation explaining the solution
3. Error handling and logging
4. Testing results showing successful API calls for all provided variant IDs
5. A simple way to input and test new variant IDs

### Required Skills
- Strong experience with Puppeteer
- Understanding of bot protection systems
- Experience with GraphQL APIs
- Knowledge of browser fingerprinting
- Experience with CAPTCHA handling
- Understanding of session management

### Additional Information
- The solution should be maintainable and well-documented
- Code should include proper error handling
- Solution should be scalable and reliable
- Must work consistently without frequent failures
- Should be more cost-effective than the commercial solution
- Must be self-hostable
- Should have proper documentation
- Must be maintainable and scalable

## Budget
[You can specify your budget range here]

## Timeline
[Specify your expected timeline]

## How to Apply
Please provide:
1. Relevant experience with similar projects
2. Examples of previous work with bot protection bypass
3. Your approach to solving this specific challenge
4. Estimated timeline for completion
5. Your rate/budget requirements

## Note
This project requires expertise in handling sophisticated bot protection systems. Please only apply if you have proven experience in this area. Thank you!