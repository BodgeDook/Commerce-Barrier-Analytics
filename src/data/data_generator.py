import pandas as pd
import numpy as np
import random


def define_parameters():
    NUM_ROWS = 5000

    random.seed(42)
    np.random.seed(42)

    products = [
        'Диван "Комфорт"', 'Шкаф-купе "Лофт"', 'Кровать двуспальная',
        'Стол обеденный', 'Кресло офисное',
        'Тумба прикроватная', 'Стеллаж деревянный', 'Комод с зеркалом'
    ]

    chat_vocab = {
        1: ['дорого', 'цена', 'стоимость', 'скидка', 'рассрочка'],
        2: ['размер', 'габариты', 'ширина', 'высота', 'глубина'],
        3: ['сборка', 'инструкция', 'инструмент', 'установка'],
        4: ['качество', 'гарантия', 'отзывы', 'доверие'],
        5: ['возврат', 'обмен', 'не подошло', 'как вернуть']
    }

    neutral_words = ['здравствуйте', 'подскажите', 'пожалуйста']

    return NUM_ROWS, products, chat_vocab, neutral_words


def generate_chat_text(barrier, chat_vocab, neutral_words):
    main_words = random.sample(chat_vocab[barrier], k=2)
    extra = random.sample(neutral_words, k=random.randint(0, 1))
    msg = main_words + extra
    random.shuffle(msg)
    return " ".join(msg)


def generate_data(NUM_ROWS, products, chat_vocab, neutral_words):
    barriers = np.repeat([1, 2, 3, 4, 5], NUM_ROWS // 5)
    np.random.shuffle(barriers)

    rows = []

    for i in range(NUM_ROWS):
        barrier = int(barriers[i])

        row = {
            "user_id": 1000 + i,
            "product_name": random.choice(products),
            "x1_views": np.random.randint(1, 10),
            "x2_chars_pdf": np.random.randint(0, 7),
            "x3_ship_page": 0,
            "x4_calc_used": int(barrier == 1),
            "x4_ship_cost": round(np.random.uniform(500, 3000), 2) if barrier == 1 else 0,
            "x5_assembly_page": int(barrier == 3),
            "x6_warranty": int(barrier == 4),
            "x7_return_page": int(barrier == 5),
            "x8_email_clicks": np.random.randint(0, 5),
            "x9_chat_text": generate_chat_text(barrier, chat_vocab, neutral_words),
            "x10_reviews": np.random.randint(0, 6),
            "Barrier_Class": barrier
        }
        rows.append(row)

    return pd.DataFrame(rows)


def main():
    NUM_ROWS, products, chat_vocab, neutral_words = define_parameters()
    df = generate_data(NUM_ROWS, products, chat_vocab, neutral_words)
    df.to_csv("synthetic_data/synthetics_furniture_barriers.csv", index=False)
    print("Synthetic dataset generated")


if __name__ == "__main__":
    main()