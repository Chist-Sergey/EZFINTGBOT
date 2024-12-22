DB = 'db/db.txt'
TR = 'db/transactions.txt'

def write(category: str, amount: int) -> None:
    """
    (Update) Add AMOUNT to a CATEGORY AMOUNT.
    (Create) If CATEGORY is not in DB, add it with current AMOUNT.
    """
    data: list = open(DB, 'r').readlines()

    for row in data:

        if category in data:
            row = add_amount(row, amount)
            break

    else:
        data.append(f'{category} {amount}')

    open(DB, 'w').write('\n'.join(data))


def read() -> str:
    """
    (Read) Read DB and return it as a string.
    """
    return open(DB, 'r').readlines()


def remove(category: str ) -> None:
    """
    (Delete) Remove CATEGORY and its amount from DB.
    """
    data: list = open(DB, 'r').readlines()

    for row in data:

        if category in row:
            data.remove(row)
            break

    open(DB, 'w').write('\n'.join(data))


def merge(category_from: str, category_to: str) -> None:
    """
    Add CATEGORY_FROM amount to CATEGORY_TO amount.
    Remove CATEGORY_FROM from DB.
    """
    data: list = open(DB, 'r').readlines()
    amount: int
    # handles 'category_to' if it gets sooner than 'category_from'
    # this allows using only a single 'for' loop
    early_encounter_index: int

    for row in data:

        if category_from in row:

            if early_encounter_index:
                row = data[early_encounter_index]
                row = add_amount(row, amount)
                break

            amount = int(row.split()[1])
            data.remove(row)
            break

        if category_to in row:

            if amount:
                row = add_amount(row, amount)
                break

            early_encounter_index = data.index(row)

    open(DB, 'w').write('\n'.join(data))


def cancel() -> None:
    """
    Substract amount from category amount based on recient changes.
    """
    data: list = open('transactions.txt', 'r').readlines()

def add_transaction(category: str, amount: int) -> None:
    open(TR, 'a')

def add_amount(row: str, amount: int) -> str:
    """
    Add category AMOUNT to AMOUNT.
    Not meant to be used outside of this file.
    """
    category = row.split()[0]
    amount = int(row.split()[1] + amount)

    return f'{category} {amount}'