# API Views Documentation

## BookListView
- Path: /api/books/
- Method: GET
- Description: Returns list of all books. Supports search & ordering if enabled.

## BookDetailView
- Path: /api/books/<pk>/
- Method: GET
- Description: Returns detailed info for a single book.

## BookCreateView
- Path: /api/books/create/
- Method: POST
- Permissions: Authenticated users only
- Description: Creates a new Book. Validates publication_year via serializer.

## BookUpdateView
- Path: /api/books/<pk>/update/
- Method: PUT/PATCH
- Permissions: Authenticated users only

## BookDeleteView
- Path: /api/books/<pk>/delete/
- Method: DELETE
- Permissions: Authenticated users only
