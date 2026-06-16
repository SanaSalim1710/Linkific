# API Documentation

| Method | Purpose         | Example              |
|--------|-----------------|----------------------|
| GET    | Retrieve data   | Get list of items    |
| POST   | Create data     | Add a new item  to the list|
| PUT    | Update data     | Update the value of an existing item|
| DELETE | Remove data     | Delete an item      

## API Endpoints
### GET all items
```
GET /api/items
Through browser: /items
```
Returns all items in the list

**Display**
```json
[
  {"name": "Mango"},
  {"name": "Banana"},
  {"name": "Durian"}
]
```

---

### GET specific item
```
GET /api/items/<item_name>
Through browser: GET /items/<item_name>
```
Returns the item's name if it exists 

**Example**
```
GET /api/items/mango
```

**Display**
```json
{"name": "Mango"}
```

**Error**
```json
{"error": "Item not found"}
```

### POST new item
```
POST /api/add
Through browser: POST /add
```
Add a new item to the list

**Example Request**
```json
{"name": "Guava"}
```

**Error** (missing name)
```json
{"error": "Must include name"}
```

### PUT update item
```
PUT /api/update/<item_name>
```
Updates the name of an existing item

**Example**
```
PUT /api/update/banana
Through browser: /update/banana
```

**Request Body**
```json
{"name": "Guava"}
```

**Display**
```json
{
  "message": "Item updated",
  "item": {"name": "Guava"}
}
```

**Error** 
```json
{"error": "Didn't receive JSON data"}
```

**Error**
```json
{"error": "Item not found"}
```

### DELETE — Remove Item
```
DELETE /api/remove/<item_name>
Through browser: /remove/<item_name>
```
Deletes specific item

**Example**
```
DELETE /api/remove/durian
```

**Display**
```json
{"message": "Item deleted"}
```

**Error**
```json
{"error": "Item not found"}
```
```
