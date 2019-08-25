def reward(block_height):
    rewards = []
    reward = 50
    for i in range(34):
        rewards.append(reward)
        reward /= 2
    return rewards[int(block_height // 210000)]


def total_fee(block):
    coin_base_tx = block['tx'][0]
    total = 0
    for vout in coin_base_tx['vout']:
        total += vout['value']

    total -= reward(block['height'])
    return total


def average_fee(block):
    return total_fee(block) / block['nTx']
