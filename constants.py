from concurrent.futures import ThreadPoolExecutor

MAX_RECORD_SIZE_PER_PAGE = 120
MAX_WORKERS = 10
NO_RECORD_FOUND = object()
PENDING_FETCH = object()
PROCESS_EXECUTOR = ThreadPoolExecutor(max_workers=MAX_WORKERS)


COLLECTIONS = {
    'NEW_FREE': 'topselling_new_free',
    'NEW_PAID': 'topselling_new_paid',
    'TOP_FREE': 'topselling_free',
    'TOP_PAID': 'topselling_paid',
    'TOP_GROSSING': 'topgrossing',
    'TRENDING': 'movers_shakers'
}

CATEGORIES = {
    "GAME": "GAME",
    "GAME_ACTION": "GAME_ACTION",
    "GAME_ADVENTURE": "GAME_ADVENTURE",
    "GAME_ARCADE": "GAME_ARCADE",
    "GAME_BOARD": "GAME_BOARD",
    "GAME_CARD": "GAME_CARD",
    "GAME_CASINO": "GAME_CASINO",
    "GAME_CASUAL": "GAME_CASUAL",
    "GAME_EDUCATIONAL": "GAME_EDUCATIONAL",
    "GAME_MUSIC": "GAME_MUSIC",
    "GAME_PUZZLE": "GAME_PUZZLE",
    "GAME_RACING": "GAME_RACING",
    "GAME_ROLE_PLAYING": "GAME_ROLE_PLAYING",
    "GAME_SIMULATION": "GAME_SIMULATION",
    "GAME_SPORTS": "GAME_SPORTS",
    "GAME_STRATEGY": "GAME_STRATEGY",
    "GAME_TRIVIA": "GAME_TRIVIA",
    "GAME_WORD": "GAME_WORD"
}