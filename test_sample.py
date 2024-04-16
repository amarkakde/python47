from sample import remove_spaces

def test_remove_spaces():
    assert remove_spaces('ada ajdoa aiodjoa') in ['adaajdoaaiodjoa']
    