# Filtering, Searching and Ordering for /api/books/

## Filtering
- Exact match: `?publication_year=2022`
- Filter by author: `?author=1`
- Range filters (if filterset_class enabled): `?publication_year__gte=2018&publication_year__lte=2022`

## Searching
- Use `?search=term` to search `title` and `author__name`
  Example: `/api/books/?search=tolkien`

## Ordering
- Use `?ordering=publication_year` or `?ordering=-title`
  Example: `/api/books/?ordering=-publication_year`

## Combined Example
`/api/books/?search=deep&publication_year__gte=2018&ordering=-publication_year`
