# Libs for work:

import pandas as pd
import numpy as np
import random

# 1. Parameters and Vocab:
def define_parameters():
    '''Initializes core configuration parameters for synthetic dataset generation.'''
    
    NUM_ROWS = 5000
    random.seed(42)
    np.random.seed(42)

    products = [
        'Диван "Комфорт"', 'Шкаф-купе "Лофт"', 'Кровать двуспальная',
        'Стол обеденный', 'Кресло офисное',
        'Тумба прикроватная', 'Стеллаж деревянный', 'Комод с зеркалом'
    ]

    # Words specific to each barrier:
    chat_vocab = {
        1: ['дорого', 'цена', 'стоимость', 'акция', 'скидка', 'рассрочка',
            'подешевле', 'не по карману', 'слишком высокая цена', 'нет скидок'],
        2: ['размер', 'габариты', 'ширина', 'высота', 'глубина', 'не помещается',
            'подскажите размеры', 'влезет ли', 'комната маленькая', 'замеры'],
        3: ['сборка', 'инструкция', 'сложно собрать', 'мастер', 'инструмент',
            'шурупы', 'детали', 'нет инструкции', 'как закрепить', 'установка'],
        4: ['качество', 'гарантия', 'отзывы', 'надежность', 'сертификация',
            'страшно покупать', 'сломается', 'подделка', 'нет доверия', 'риск'],
        5: ['возврат', 'обмен', 'вернуть товар', 'не подошло', 'срок возврата',
            'условия', 'хочу вернуть', 'денег не вернули', 'процедура', 'как вернуть']
    }

    neutral_words = ['здравствуйте', 'подскажите', 'пожалуйста', 'интересует', 'вопрос', 'нужно уточнить']

    return NUM_ROWS, products, chat_vocab, neutral_words

# 2. Chat Generator:
def generate_chat_text(barrier_type, chat_vocab, neutral_words) -> list:
    """
    We are generating a short but informative chat:
    - minimum 2-5 words
    - thematic words + neutral words
    - correct noise level
    """
    main_words = random.sample(chat_vocab[barrier_type], k=random.randint(2, 3))
    extra_neutral = random.sample(neutral_words, k=random.randint(0, 2))

    msg = main_words + extra_neutral
    random.shuffle(msg)

    return " ".join(msg)

# 3. Data Generator:
def generate_data(NUM_ROWS, products, chat_vocab, neutral_words):

    # Balanced labels:
    barriers_balanced = np.repeat([1,2,3,4,5], NUM_ROWS // 5)
    np.random.shuffle(barriers_balanced)

    # If division left remainder (not expected for 5000), pad:
    while len(barriers_balanced) < NUM_ROWS:
        barriers_balanced = np.append(barriers_balanced, random.randint(1, 5))

    data = []

    for i in range(NUM_ROWS):
        barrier = int(barriers_balanced[i])

        user_id = 1000 + i
        product = random.choice(products)

        # Default values:
        x1_views = np.random.randint(1, 4)
        x2_chars = np.random.poisson(1)
        x3_ship_page = 0
        x4_calc_used = 0
        x4_ship_cost = 0
        x5_assembly = 0
        x6_warranty = 0
        x7_return = 0
        x8_email = np.random.randint(0, 3)
        x10_reviews = np.random.poisson(1)

        # Correlations:
        if barrier == 1:  # PRICE
            x1_views = np.random.randint(2, 8)
            x4_calc_used = 1
            x4_ship_cost = round(np.random.uniform(800, 3500), 2)
            x8_email = np.random.randint(1, 6)

        elif barrier == 2: # SIZE
            x1_views = np.random.randint(4, 12)
            x2_chars = np.random.randint(3, 8)

        elif barrier == 3: # ASSEMBLY
            x5_assembly = 1
            x2_chars = np.random.randint(1, 5)

        elif barrier == 4: # TRUST
            x10_reviews = np.random.randint(3, 10)
            x6_warranty = 1

        elif barrier == 5: # REFUND
            x7_return = 1
            x6_warranty = random.randint(0, 1)

        # Chay Text:
        chat_text = generate_chat_text(barrier, chat_vocab, neutral_words)

        # Random Noise (5%):
        if random.random() < 0.05:
            x7_return = 1

        row = {
            'user_id': user_id,
            'product_name': product,
            'x1_views': x1_views,
            'x2_chars_pdf': x2_chars,
            'x3_ship_page': x3_ship_page,
            'x4_calc_used': x4_calc_used,
            'x4_ship_cost': x4_ship_cost,
            'x5_assembly_page': x5_assembly,
            'x6_warranty': x6_warranty,
            'x7_return_page': x7_return,
            'x8_email_clicks': x8_email,
            'x9_chat_text': chat_text,
            'x10_reviews': x10_reviews,
            'Barrier_Class': barrier
        }

        data.append(row)

    return pd.DataFrame(data)


# 4. MAIN FUNCTION:
def main():
    NUM_ROWS, products, chat_vocab, neutral_words = define_parameters()
    df = generate_data(NUM_ROWS, products, chat_vocab, neutral_words)

    df.to_csv('synthetic_furniture_barriers.csv', index=False)
    print('Synthetics done: 5000 examples of barriers were generated successfully!')

if __name__ == '__main__':
    main()