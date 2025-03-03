schema_add_to_cart = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "productId": {
      "type": "integer"
    },
    "quantity": {
      "type": "integer"
    }
  },
  "required": [
    "productId",
    "quantity"
  ]
}

schema_get_suggestions = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "suggestions": {
      "type": "array",
      "items": {}
    },
    "totalCount": {
      "type": "integer"
    }
  },
  "required": [
    "suggestions",
    "totalCount"
  ]
}