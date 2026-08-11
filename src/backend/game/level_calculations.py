
# ! remove the basic 250 XP rule and replace it by a square-function or multiply the XP times 1.05

class LevelAPI:
    def get_current_level(xp: int):
        return xp // 250

    def get_xp_for_next_level(xp: int):
        return xp % 250

    def get_xp_max_for_current_level(xp: int):
        return (LevelAPI.get_current_level(xp) + 1) * 250
    
    def get_xp_percentage(xp: int):
        xpbf = LevelAPI.get_xp_for_next_level(xp)
        xpbf = xpbf / 250 if xpbf else 0
        #xpbf *= 100
        return xpbf