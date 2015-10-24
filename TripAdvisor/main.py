from reviews import get_hotel_reviews


def hotel_csv():
    df = get_hotel_reviews()
    df.to_csv('data/hotel_reviews.csv', encoding='utf-8')
    return df


def main():
    df = hotel_csv()
    df = 0


if __name__ == '__main__':
    main()
