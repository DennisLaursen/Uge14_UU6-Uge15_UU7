import requests
import polars as pl
import io

response = request.get('https://example.com/path/to/data').content
raw_data = pl.read_csv(io.StringIO(response.decode("utf-8")))