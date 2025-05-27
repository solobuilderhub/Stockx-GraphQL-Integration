# Job Title: Expert Developer Needed for StockX API Integration with Bot Protection Bypass

[Previous sections remain the same until Technical Details...]

### Technical Details
- Target URL: https://gateway.stockx.com/api/graphql
- Required Headers:
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

[Rest of the job description remains the same...]