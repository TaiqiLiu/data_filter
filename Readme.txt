An /api/posts route that handles the following query parameters:
  tags: any number of comma-separated strings
  sortBy: one of “id”, “reads”, “likes”, “popularity”
  direction: one of “asc”, “desc”, defaults to “asc”
----------------------------------------------------
host="localhost", port=5000
----------------------------------------------------
Run server command:
python main.py
----------------------------------------------------
Test command:
python -m pytest
----------------------------------------------------

Made by Taiqi Liu
