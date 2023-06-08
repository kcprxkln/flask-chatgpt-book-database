import rating_scraping 

def test_scrape_rating() -> None:
    rating = float(rating_scraping.scrape_rating("rich dad poor dad"))
    assert 0 < rating < 5 