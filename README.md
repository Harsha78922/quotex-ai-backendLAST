# Quotex AI Backend (Real Model)

## How to Use

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run backend:
   ```
   python app.py
   ```

3. POST data to /predict with:
```json
{
  "ohlcv": [[open, high, low, close, volume], ... (50 rows)]
}
```

Returns: `Buy` or `Sell` with confidence score.